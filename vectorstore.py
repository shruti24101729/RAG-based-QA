import os
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

VECTOR_DB_PATH = "data/faiss_index"

embeddings = OpenAIEmbeddings()

def save_vectorstore(docs):
    vectorstore = FAISS.from_documents(docs, embeddings)
    vectorstore.save_local(VECTOR_DB_PATH)

def load_vectorstore():
    if not os.path.exists(VECTOR_DB_PATH):
        return None
    return FAISS.load_local(VECTOR_DB_PATH, embeddings, allow_dangerous_deserialization=True)
