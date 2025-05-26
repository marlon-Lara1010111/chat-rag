# 🤖 ChatRAG PDF Bot

> **Transforme seus documentos PDF em assistentes inteligentes que respondem suas dúvidas na hora!**

---

## ✨ Visão Geral

Você já imaginou poder conversar com qualquer documento importante da sua empresa, universidade ou projeto, como se fosse um especialista?  
O **ChatRAG PDF Bot** faz exatamente isso! Envie perguntas sobre o conteúdo de um PDF e receba respostas precisas e rápidas, geradas a partir do próprio texto do documento.

Além disso, ele:

- 👋 Reconhece e responde saudações com simpatia, tornando a interação mais humana.  
- 🤔 Identifica quando a pergunta não está relacionada ao conteúdo do PDF e responde de forma genérica e elegante.  
- 🔄 Atualiza automaticamente seu banco de vetores para refletir qualquer mudança ou atualização no seu documento.

---

## 🛠 Tecnologias Usadas

| Tecnologia             | Função                                   |
|-----------------------|-----------------------------------------|
| **Python 3.10+**       | Linguagem principal                      |
| **Flask**              | Criação da API web                       |
| **Langchain**          | Orquestração do pipeline de RAG         |
| **FAISS**              | Banco de vetores para buscas rápidas    |
| **HuggingFace Embeddings** | Transformação do texto em vetores     |
| **Ollama**             | Execução local do modelo de linguagem   |
| **PyPDF2**             | Leitura e extração do conteúdo PDF      |

---

## 🎯 Por que criei este projeto?

No dia a dia, muitas vezes precisamos acessar informações importantes guardadas em PDFs — contratos, manuais, relatórios, documentos legais, e muito mais.  
Mas vasculhar páginas e páginas manualmente é cansativo e ineficiente. Com este projeto, a ideia é:

- **Tornar o acesso à informação mais rápido e intuitivo** — qualquer dúvida respondida na hora, sem precisar perder tempo procurando.  
- **Democratizar o conhecimento** dentro das organizações, permitindo que qualquer pessoa tire dúvidas sem depender de especialistas.  
- **Explorar o potencial da Recuperação Aumentada por Geração (RAG)** para unir o melhor de duas tecnologias: a busca inteligente por vetores e a geração natural de linguagem.

---

## 🚀 Como executar localmente

### 1. Pré-requisitos

- Instale o [Ollama](https://ollama.com/) e rode o modelo `llama3` localmente:

```bash
ollama run llama3
