from langchain_openai import ChatOpenAI
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

from vectorstore import load_vectorstore

load_dotenv()
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

def answer_question(query: str):
    vectorstore = load_vectorstore()
    if vectorstore is None:
        return "No documents ingested yet."

    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    # Prompt (LCEL compatible)
    prompt = ChatPromptTemplate.from_template(
        """
        Answer the question using only the provided context.

        Context:
        {context}

        Question:
        {input}
        """
    )

    # Document chain (LLM + prompt)
    document_chain = create_stuff_documents_chain(
        llm=llm,
        prompt=prompt
    )

    # Retrieval chain (Retriever → Document Chain)
    retrieval_chain = create_retrieval_chain(
        retriever=retriever,
        combine_docs_chain=document_chain
    )

    # LCEL invocation
    response = retrieval_chain.invoke({"input": query})

    return response.get("answer") or response.get("output_text")

