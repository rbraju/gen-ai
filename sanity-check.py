import sys
print(sys.version)

import streamlit as st
from PyPDF2 import PdfReader

from langchain_community.chat_models import ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings

from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_classic.chains import RetrievalQA

print("ALL IMPORTS OK")
