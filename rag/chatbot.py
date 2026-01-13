import streamlit as st
from PyPDF2 import PdfReader

from langchain_community.chat_models import ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings

from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_classic.chains import RetrievalQA

from config.settings import load_env, get_openai_api_key

# Load environment variables and get API key
load_env()
OPENAI_API_KEY = get_openai_api_key()

# upload PDF files
st.header("My First Chatbot")

with st.sidebar:
    st.title("Your documents")
    file = st.file_uploader("Upload a PDF file and start asking questions", type="pdf")

# Extract the text
if file is not None:
    pdfReader = PdfReader(file)
    # text = ""
    # for page in pdfReader.pages:
    #     text += page.extract_text()
    text = "".join([page.extract_text() for page in pdfReader.pages])


    # Break it into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n"],
        chunk_size=500,
        chunk_overlap=50,
        length_function=len
    )
    chunks = text_splitter.split_text(text)

    # RAG SETUP: Generate embeddings for semantic search
    # Embeddings convert text chunks into numerical vectors for similarity search
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

    # RAG SETUP: Create vector store (FAISS) for efficient similarity search
    # This stores the document chunks as vectors, enabling fast retrieval
    vector_store = FAISS.from_texts(chunks, embeddings)

    # Get user question
    question = st.text_input("Type your question here")

    # =================================================
    # RAG PIPELINE: Retrieval, Augmentation, Generation
    # =================================================
    if question:
        # RETRIEVAL: Search for relevant document chunks from the vector store
        # This retrieves the most similar text chunks to the user's question
        match = vector_store.similarity_search(question)

        # Initialize the LLM for generation
        llm = ChatOpenAI(
            openai_api_key=OPENAI_API_KEY,
            temperature=0.8,
            max_tokens=500,
            model_name="gpt-3.5-turbo"
        )
        
        # AUGMENTATION + GENERATION: RetrievalQA chain combines retrieval, augmentation, and generation
        # - Retrieval: Uses the retriever to fetch relevant chunks (handled internally)
        # - Augmentation: Combines retrieved documents with the query into a prompt
        # - Generation: LLM generates the final answer based on the augmented prompt
        chain = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=vector_store.as_retriever(),
            chain_type="stuff"
        )
        
        # Execute the RAG pipeline: retrieval -> augmentation -> generation
        output = chain.run(input_documents=match, query=question)
        st.write(output)
