import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_postgres import PGVector

load_dotenv()
PDF_PATH = os.getenv("PDF_PATH")


def ingest_pdf():
    loader = PyPDFLoader(PDF_PATH)
    documents=loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    chunks = text_splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings(model=os.getenv("OPENAI_EMBEDDING_MODEL"))
    db = PGVector(
        embeddings=embeddings,
        collection_name=os.getenv("PG_VECTOR_COLLECTION_NAME"),
        connection=os.getenv("DATABASE_URL")
    )
    db.add_documents(chunks)
if __name__ == "__main__":
    ingest_pdf()