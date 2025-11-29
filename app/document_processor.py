from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
import os

class DocumentProcessor:
    def __init__(self):
        self.chunk_size = 1000
        self.chunk_overlap = 100
        self.embedding_model = OllamaEmbeddings(
            model="nomic-embed-text:v1.5"
        )
        self.vectorstore = None
        
    def load_document(self, file_path):
        if not os.path.exists(file_path):
             raise ValueError(f"File not found: {file_path}")
        if file_path.lower().endswith('.pdf'):
            loader = PyPDFLoader(file_path)
        else:
            raise ValueError(f"Unsupported file format: {file_path}")
        return loader.load()
        
    def process_document(self, file_path):
        docs = self.load_document(file_path)
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size, 
            chunk_overlap=self.chunk_overlap
        )
        split_docs = text_splitter.split_documents(docs)
        
        if self.vectorstore is None:
            self.vectorstore = FAISS.from_documents(split_docs, self.embedding_model)
        else:
            self.vectorstore.add_documents(split_docs)
        
    def retrieve_relevant_context(self, query, k=3):
        if self.vectorstore is None:
            return []
            
        return self.vectorstore.similarity_search(query, k=k)
        
    def reset(self):
        self.vectorstore = None