import streamlit as st
from PyPDF2 import PdfReader
from langchain.chains.question_answering import load_qa_chain
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain_community.chat_models import ChatOpenAI

OPENAI_API_KEY = "<OPEN_API_KEY>"

# upload PDF files
st.header("My First Chatbot")

with st.sidebar:
    st.title("Your documents")
    file = st.file_uploader("Upload a PDF file and start asking questions", type="pdf")

# Extract the text
if file is not None:
    pdfReader = PdfReader(file)
    text = ""
    for page in pdfReader.pages:
        text += page.extract_text()

    # Break it into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n"],
        chunk_size=500,
        chunk_overlap=50,
        length_function=len
    )
    chunks = text_splitter.split_text(text)

    # Generate embeddings
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

    # Create vector store
    vector_store = FAISS.from_texts(chunks, embeddings)

    # Get user question
    question = st.text_input("Type your question here")


    # Do similarity search
    if question:
        match = vector_store.similarity_search(question)

        # Output results
        llm = ChatOpenAI(
            openai_api_key=OPENAI_API_KEY,
            temperature=0.8,
            max_tokens=500,
            model_name="gpt-3.5-turbo"
        )
        chain = load_qa_chain(llm, chain_type="stuff")
        output = chain.run(input_documents=match, question=question)
        st.write(output)
