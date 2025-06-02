
# 🤖 ChatRAG PDF Bot

**Transforme seus documentos PDF em assistentes inteligentes que respondem suas dúvidas na hora!**

---

![image](https://github.com/user-attachments/assets/de3e3126-0f7f-4170-b068-a3499bf951c9)


## ✨ Visão Geral

> **Atenção:** Este projeto utiliza como exemplo o arquivo `empresa_info.pdf`, baseado em um material do SENAI, pois sou estudante da instituição.  
> Sinta-se à vontade para **substituí-lo por qualquer outro PDF**! O bot se adapta automaticamente ao conteúdo que você fornecer. 📄✨

Você já imaginou poder conversar com qualquer documento importante da sua empresa, universidade ou projeto, como se fosse um especialista?  
O **ChatRAG PDF Bot** faz exatamente isso! Envie perguntas sobre o conteúdo de um PDF e receba respostas precisas e rápidas, geradas a partir do próprio texto do documento.

Além disso, ele:

- 👋 Reconhece e responde saudações com simpatia, tornando a interação mais humana.  
- 🤔 Identifica quando a pergunta não está relacionada ao conteúdo do PDF e responde de forma genérica e elegante.  
- 🔄 Atualiza automaticamente seu banco de vetores para refletir qualquer mudança ou atualização no seu documento.

---

## 🛠 Tecnologias Usadas

| Tecnologia                 | Função                                      |
|---------------------------|---------------------------------------------|
| **Python 3.10+**          | Linguagem principal                         |
| **Flask**                 | Criação da API web                          |
| **Langchain**             | Orquestração do pipeline de RAG            |
| **FAISS**                 | Banco de vetores para buscas rápidas       |
| **HuggingFace Embeddings**| Transformação do texto em vetores           |
| **Ollama**                | Execução local do modelo de linguagem      |
| **PyPDF2**                | Leitura e extração do conteúdo do PDF      |

---



## 🎯 Por que criei este projeto?

No dia a dia, muitas vezes precisamos acessar informações importantes guardadas em PDFs — contratos, manuais, relatórios, documentos legais e muito mais.  
Mas vasculhar páginas e páginas manualmente é cansativo e ineficiente.

Com este projeto, a ideia é:

- ⚡ **Tornar o acesso à informação mais rápido e intuitivo** — qualquer dúvida respondida na hora, sem precisar perder tempo procurando.  
- 🧠 **Democratizar o conhecimento** dentro das organizações, permitindo que qualquer pessoa tire dúvidas sem depender de especialistas.  
- 🔍 **Explorar o potencial da Recuperação Aumentada por Geração (RAG)** — unindo a busca inteligente por vetores com a geração natural de linguagem.

---

## 🚀 Como executar localmente

Rodar o **ChatRAG PDF Bot** no seu computador é simples — em poucos minutos você terá um assistente inteligente pronto para conversar com seus documentos! 😄

### 🔧 Passos para rodar localmente:

#### 1. Instale o [Ollama](https://ollama.com/) e rode o modelo `llama3:8b`:

```bash
ollama pull llama3:8b
ollama run llama3:8b
```
> ⚠️ Esse modelo será responsável por gerar as respostas baseadas no conteúdo do PDF.  
> Mantenha este processo rodando em um terminal separado.

#### 2. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/chatrag-pdf-bot.git
cd chatrag-pdf-bot
```

#### 3. Crie e ative um ambiente virtual (opcional, mas altamente recomendado):

- No Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

- No macOS/Linux:

```bash
python -m venv venv
source venv/bin/activate
```

#### 4. Instale as dependências:

```bash
pip install -r requirements.txt
```

> Ou, se preferir instalar manualmente:

```bash
pip install flask langchain faiss-cpu PyPDF2
```

#### 5. Coloque seu PDF na pasta do projeto

> 💡 O repositório já vem com um arquivo de exemplo chamado `empresa_info.pdf`, baseado em um material do SENAI que utilizei para testes.  
> Você pode substituir por qualquer PDF que quiser — o bot irá se adaptar automaticamente ao conteúdo do seu documento!

#### 6. Execute o bot:

```bash
python app.py
```

> 🚀 A aplicação será iniciada e você poderá interagir com o chatbot via terminal ou API, conforme a implementação atual.
