from flask import Flask, request, jsonify
from flask_cors import CORS
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
import os
import re
from dotenv import load_dotenv

# Configurações
load_dotenv()
app = Flask(__name__)
CORS(app)

# Modelo de respostas
RESPONSE_TEMPLATES = {
    "greetings": {
        r"(?i)^(oi|olá|ola|e aí|hey|hello)$": "👋 Olá! Sou seu assistente do SENAI. Como posso ajudar?",
        r"(?i)^(quem é você|quem te criou)$": "🤖 Sou um assistente IA especializado em documentos SENAI com RAG (Ollama + LangChain)",
        r"(?i)^(bom dia|boa tarde|boa noite)$": lambda m: f"☀️ {m[0].title()}! Pergunte sobre o documento." if "noite" not in m[0] else f"🌙 {m[0].title()}! Estou aqui para ajudar.",
        r"(?i)^(tchau|até logo|flw|vlw)$": "👋 Até logo! Qualquer dúvida estou aqui!",
        r"(?i)^(obrigado|valeu|agradeço)$": "😊 Por nada! Fico feliz em ajudar!"
    },
    "fallback": """🔍 Não encontrei isso no documento. Posso responder sobre:
- **Estratégias de desenho curricular**
- **Perfis profissionais**
- **Itinerários formativos**

Experimente perguntar sobre um desses tópicos!"""
}

def load_and_split_pdf():
    """Carrega e divide o PDF em chunks."""
    if not os.path.exists(os.getenv('PDF_PATH')):
        raise FileNotFoundError(f"Arquivo {os.getenv('PDF_PATH')} não encontrado")

    text = ""
    with open(os.getenv('PDF_PATH'), "rb") as f:
        pdf = PdfReader(f)
        for page in pdf.pages:
            text += page.extract_text() or ""
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    return text_splitter.split_text(text)

def get_vector_store():
    """Gerencia o banco vetorial FAISS."""
    embeddings = HuggingFaceEmbeddings(model_name=os.getenv('EMBEDDINGS_MODEL'))
    if os.path.exists(os.getenv('VECTOR_STORE_PATH')):
        return FAISS.load_local(
            os.getenv('VECTOR_STORE_PATH'), 
            embeddings, 
            allow_dangerous_deserialization=True
        )
    else:
        chunks = load_and_split_pdf()
        vector_store = FAISS.from_texts(chunks, embeddings)
        vector_store.save_local(os.getenv('VECTOR_STORE_PATH'))
        return vector_store

def init_rag_chain():
    """Inicializa a cadeia RAG."""
    llm = Ollama(model=os.getenv('MODEL_NAME'))
    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=get_vector_store().as_retriever(search_kwargs={"k": 3}),
        return_source_documents=True
    )

rag_chain = init_rag_chain()

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.json
        prompt = data.get("prompt", "").strip()
        
        if not prompt:
            return jsonify({"error": "Prompt vazio"}), 400

        # Verifica saudações
        for pattern, response in RESPONSE_TEMPLATES["greetings"].items():
            if re.fullmatch(pattern, prompt):
                return jsonify({
                    "response": response(re.match(pattern, prompt)) if callable(response) else response,
                    "sources": []
                })

        # Processa com RAG
        result = rag_chain({"query": prompt})
        
        # Verifica resposta irrelevante
        if any(phrase in result["result"].lower() for phrase in ["não sei", "não encontro", "não tenho informações"]):
            return jsonify({
                "response": RESPONSE_TEMPLATES["fallback"],
                "sources": []
            })
        
        return jsonify({
            "response": result["result"],
            "sources": [{"page": i+1} for i, doc in enumerate(result["source_documents"])]
        })

    except Exception as e:
        return jsonify({"error": f"Erro: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)