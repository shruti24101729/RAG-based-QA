# RAG QA System (Retrieval-Augmented Generation)

## 📌 Project Overview
This project is a **Retrieval-Augmented Generation (RAG) based Question Answering system**. Users can upload their own documents (PDF or text files) and ask questions based on the content of those documents. The system retrieves relevant information from the documents and uses a Large Language Model (LLM) to generate accurate answers.

---

## 🧠 High-Level Architecture
1. **Document Upload API** – Upload PDF/Text documents
2. **Ingestion Pipeline** – Load documents → split into chunks → generate embeddings
3. **Vector Store (FAISS)** – Store document embeddings
4. **Question API** – Accept user questions
5. **Retriever + LLM** – Fetch relevant chunks and generate answers

---

## 🗂️ Project Structure
```
rag-qa-system/
│── main.py              # FastAPI application entry point
│── api.py               # API routes (/upload, /ask)
│── ingest.py            # Document ingestion logic
│── rag.py               # RAG-based question answering logic
│── vectorstore.py       # FAISS vector store handling
│── schemas.py           # Pydantic request/response schemas
│── rate_limiter.py      # API rate limiting configuration
│── requirements.txt     # Python dependencies
│── .env                 # Environment variables
│
└── data/
    ├── uploads/          # Uploaded documents
    └── faiss_index/      # Stored FAISS index
```

---

## ⚙️ Step-by-Step Project Workflow

### 1️⃣ Environment Setup
- A Python virtual environment is created
- All required dependencies are listed in `requirements.txt`
- The OpenAI API key is stored in a `.env` file

```env
OPENAI_API_KEY=your_api_key_here
```

---

### 2️⃣ FastAPI Application (`main.py`)
- FastAPI app is initialized
- Global rate limiter middleware is configured
- API routes from `api.py` are registered

---

### 3️⃣ Document Upload API (`/upload`)
**File:** `api.py`

- Users upload PDF or text files
- Files are saved in the `data/uploads/` directory
- A background ingestion task is triggered
- Rate limit applied: **5 requests per minute**

---

### 4️⃣ Document Ingestion (`ingest.py`)
- Appropriate loader is selected based on file type
  - PDF → `PyPDFLoader`
  - Text → `TextLoader`
- Documents are split into chunks using a text splitter
  - `chunk_size = 500`
  - `chunk_overlap = 100`
- These chunks are sent for embedding generation

---

### 5️⃣ Vector Store Creation (`vectorstore.py`)
- OpenAI embeddings are generated for each chunk
- FAISS vector database is created
- The vector index is saved locally in `data/faiss_index/`

---

### 6️⃣ Question Answer API (`/ask`)
**File:** `api.py`

- Users send questions in JSON format
- Request validation is handled using Pydantic schemas
- Rate limit applied: **10 requests per minute**

Example request:
```json
{
  "question": "What is cloud computing?"
}
```

---

### 7️⃣ RAG Pipeline (`rag.py`)
- FAISS vector store is loaded
- Top-3 most relevant document chunks are retrieved
- A custom prompt is created with retrieved context
- The LLM generates an answer strictly based on the provided context

---

## 🔐 Rate Limiting
- Implemented using **SlowAPI**
- Upload endpoint: `5 requests/minute`
- Question endpoint: `10 requests/minute`

---

## 🚀 How to Run the Project
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

The API will be available at:
```
http://localhost:8000
```

---

## ✅ Key Features
- RAG-based accurate question answering
- Supports PDF and text documents
- FAISS-powered vector similarity search
- OpenAI LLM integration
- Rate-limited APIs
- Background document ingestion

---

## 📌 Future Enhancements
- Support for multiple documents per user
- Chat history and conversational memory
- Web UI (React or Streamlit)
- Authentication and user-based document isolation

---

✨ **This project demonstrates a complete end-to-end RAG system using FastAPI, LangChain, FAISS, and OpenAI.**

