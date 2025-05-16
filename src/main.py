#!/usr/bin/env python3
"""
PDF Document Processor with Gemini
---------------------------------
This application processes PDF documents using Llama Index, ChromaDB, and Google Gemini API.
It allows users to upload PDFs and ask questions about the content through a chat interface.
"""

import os
import sys
import logging
import google.generativeai as genai
from llama_index.core import SimpleDirectoryReader
from llama_index.core.node_parser import SentenceSplitter
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core.storage.storage_context import StorageContext
from llama_index.core import VectorStoreIndex
from llama_index.core.embeddings import BaseEmbedding
import chromadb
import numpy as np
from typing import List, Optional

from utils import check_environment, display_header, display_message, get_user_input



# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

class CustomGeminiEmbedding(BaseEmbedding):
    """Custom embedding class using Google's Generative AI API."""
    
    def __init__(self, api_key, model_name="models/embedding-001"):
        """Initialize with Google API key and model name."""
        super().__init__(model_name=model_name)
        self.api_key = api_key
        genai.configure(api_key=api_key)
        self.embed_model = genai.embed_content
        self.embedding_dimension = 768  # Default embedding dimension for Gemini
        
    def _get_query_embedding(self, query: str) -> list:
        """Get embedding for a query string."""
        try:
            result = self.embed_model(
                model=self.model_name,
                content=query,
                task_type="retrieval_query"
            )
            return result["embedding"]
        except Exception as e:
            logger.error(f"Error getting query embedding: {e}")
            # Return a zero vector as fallback
            return [0.0] * self.embedding_dimension
            
    def _get_text_embedding(self, text: str) -> list:
        """Get embedding for a text string."""
        try:
            result = self.embed_model(
                model=self.model_name,
                content=text,
                task_type="retrieval_document"
            )
            return result["embedding"]
        except Exception as e:
            logger.error(f"Error getting text embedding: {e}")
            # Return a zero vector as fallback
            return [0.0] * self.embedding_dimension
            
    def _get_text_embeddings(self, texts: list) -> list:
        """Get embeddings for multiple text strings."""
        embeddings = []
        for text in texts:
            embeddings.append(self._get_text_embedding(text))
        return embeddings

class PDFProcessor:
    """
    A class to process PDF documents using Llama Index, ChromaDB, and Google Gemini API.
    """
    def __init__(self):
        """Initialize the PDFProcessor with necessary components."""
        self.api_key = os.getenv("GOOGLE_API_KEY")
        if not self.api_key:
            raise ValueError("GOOGLE_API_KEY environment variable not set")
        
        logger.info(f"Attempting to initialize with API key: {self.api_key[:5]}...{self.api_key[-4:]}")
        
        # Initialize Gemini API
        genai.configure(api_key=self.api_key)
        
        # Log available models
        models = [m.name for m in genai.list_models()]
        logger.info(f"Available models: {models}")
        
        # Initialize ChromaDB
        self.chroma_client = chromadb.Client()
        self.chroma_collection = self.chroma_client.get_or_create_collection("pdf_documents")
        logger.info("ChromaDB collection 'pdf_documents' initialized")
        
        # Initialize embedding model
        self.embed_model = CustomGeminiEmbedding(
            model_name="models/embedding-001",
            api_key=self.api_key
        )
        
        # Initialize vector store
        self.vector_store = ChromaVectorStore(chroma_collection=self.chroma_collection)
        self.storage_context = StorageContext.from_defaults(vector_store=self.vector_store)
        
        # Document directory
        self.document_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "Document")
        
        # Initialize index
        self.index = None
        
    def load_documents(self):
        """Load PDF documents from the Document directory."""
        # Check if Document directory exists
        if not os.path.exists(self.document_dir):
            os.makedirs(self.document_dir)
            logger.info(f"Created Document directory at {self.document_dir}")
            return False
        
        # Check if there are PDF files in the Document directory
        pdf_files = [f for f in os.listdir(self.document_dir) if f.lower().endswith('.pdf')]
        if not pdf_files:
            logger.warning("No PDF files found in the Document directory")
            return False
        
        logger.info(f"Found {len(pdf_files)} PDF files: {', '.join(pdf_files)}")
        
        try:
            # Load documents using SimpleDirectoryReader
            documents = SimpleDirectoryReader(
                self.document_dir
            ).load_data()
            
            # Split documents into chunks
            parser = SentenceSplitter(chunk_size=1024, chunk_overlap=20)
            nodes = parser.get_nodes_from_documents(documents)
            
            # Create index
            self.index = VectorStoreIndex(
                nodes, 
                storage_context=self.storage_context,
                embed_model=self.embed_model
            )
            
            logger.info(f"Successfully loaded and stored {len(documents)} documents")
            return True
        except Exception as e:
            logger.error(f"Error loading documents: {str(e)}")
            return False
    
    def query_documents(self, query):
        """Query the indexed documents using Gemini API."""
        if not self.index:
            logger.error("No documents indexed. Please load documents first.")
            return "No documents have been indexed. Please add PDF files to the Document directory."
        
        try:
            # Use Gemini directly for better responses
            model = genai.GenerativeModel('gemini-1.5-pro')
            
            # Create a context from the relevant chunks
            retriever = self.index.as_retriever(similarity_top_k=3)
            nodes = retriever.retrieve(query)
            
            # Extract text from nodes
            context = "\n\n".join([node.text for node in nodes])
            
            # Create a prompt with the context and query
            prompt = f"""
            Based on the following information from the document:
            
            {context}
            
            Please answer this question: {query}
            
            If the answer cannot be found in the provided information, please say so.
            """
            
            # Generate response
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            logger.error(f"Error querying documents: {str(e)}")
            return f"Error processing your query: {str(e)}"

def main():
    """Main function to run the PDF Document Processor."""
    # Check environment
    if not check_environment():
        sys.exit(1)
    
    # Display header
    display_header()
    
    # Initialize PDF processor
    try:
        processor = PDFProcessor()
    except ValueError as e:
        display_message(f"Error: {str(e)}", "error")
        display_message("Please set the GOOGLE_API_KEY environment variable.", "info")
        display_message("You can create a .env file with your API key or run:", "info")
        display_message("export GOOGLE_API_KEY=your_api_key", "code")
        sys.exit(1)
    except Exception as e:
        display_message(f"Error initializing PDF processor: {str(e)}", "error")
        sys.exit(1)
    
    # Load documents
    if not processor.load_documents():
        display_message("No PDF files found in the Document directory.", "warning")
        display_message("Please add PDF files to the Document directory and restart the application.", "info")
        display_message(f"Document directory: {processor.document_dir}", "info")
        sys.exit(1)
    
    display_message("\nDocuments loaded and indexed successfully!", "success")
    display_message("You can now ask questions about the content of your PDF documents.", "info")
    display_message("Type 'help' for available commands or 'exit' to quit the application.", "info")
    
    # Chat loop
    while True:
        query = get_user_input("\nYour question:")
        
        if query.lower() == 'exit':
            display_message("Thank you for using the PDF Document Processor!", "info")
            break
        elif query.lower() == 'help':
            display_message("Available commands:", "info")
            display_message("  help - Display this help message", "info")
            display_message("  exit - Exit the application", "info")
            display_message("  Any other input will be treated as a question about your documents", "info")
        elif query.strip():
            display_message("Processing your question...", "info")
            answer = processor.query_documents(query)
            display_message("\nAnswer:", "success")
            print(answer)

if __name__ == "__main__":
    main()