rag-qa-system/
│
|
├── main.py              # FastAPI entry point
├── api.py               # API routes
├── ingest.py            # Background ingestion job
├── rag.py               # Retrieval + Generation logic
├── vectorstore.py       # FAISS vector store handling
├── schemas.py           # Pydantic models
├── rate_limiter.py      # Basic rate limiting
│
├── data/
│   └── uploads/             # Uploaded documents
│
├── requirements.txt
├── README.md
└── .env
