import os
import sys
from langchain.document_loaders import PyPDFLoader
from langchain.document_loaders import Docx2txtLoader
from langchain.document_loaders import TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.text_splitter import (
    CharacterTextSplitter,
    RecursiveCharacterTextSplitter,
)
from langchain.document_loaders.csv_loader import CSVLoader

from dotenv import load_dotenv

from langchain.document_loaders import UnstructuredExcelLoader
import pandas as pd

# Create a List of Documents from all of our files in the ./docs folder
load_dotenv()

openai_api_key = os.getenv("OPENAI_KEY")


def run_chat(query, chat_history):
    documents = []

    for file in os.listdir("docs"):
        if file.endswith(".pdf") or file.endswith(".PDF"):
            pdf_path = "./docs/" + file
            loader = PyPDFLoader(pdf_path)
            print("loader ", pdf_path)
            documents.extend(loader.load())
            print("DOCSSS--------------------------------> ", documents)
        elif file.endswith(".docx") or file.endswith(".doc"):
            doc_path = "./docs/" + file
            loader = Docx2txtLoader(doc_path)
            documents.extend(loader.load())
        elif file.endswith(".txt"):
            text_path = "./docs/" + file
            loader = TextLoader(text_path)
            documents.extend(loader.load())
        elif file.endswith(".csv"):
            csv_path = "./docs/" + file
            loader = CSVLoader(csv_path)
            documents.extend(loader.load())
        elif file.endswith(".xlsx"):
            xls_path = "./docs/" + file
            data = pd.read_excel(xls_path, engine="openpyxl")

            # Save the data as a CSV file
            data.to_csv("./docs/analisis.csv", index=False)
            csv_path = "./docs/analisis.csv"
            loader = CSVLoader(csv_path)
            documents.extend(loader.load())

    # Split the documents into smaller chunks
    # CharacterTextSplitter
    # text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    # documents = text_splitter.split_documents(documents)

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    documents = text_splitter.split_documents(documents)
    print("AGAAAAAAAIN", documents)
    # Recursive text splitter
    #
    vectordb = Chroma.from_documents(
        documents,
        embedding=OpenAIEmbeddings(openai_api_key=openai_api_key),
        persist_directory="./data",
    )
    vectordb.persist()

    pdf_qa = ConversationalRetrievalChain.from_llm(
        ChatOpenAI(
            temperature=0.8,
            model_name="gpt-3.5-turbo-16k",
            openai_api_key=openai_api_key,
        ),
        retriever=vectordb.as_retriever(search_kwargs={"k": 5}),
        return_source_documents=True,
        verbose=False,
    )

    result = pdf_qa({"question": query, "chat_history": chat_history})
    chat_history.extend([(query, result["answer"])])
    print(result["answer"], chat_history)
    return result["answer"], chat_history
