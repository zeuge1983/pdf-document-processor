#!/usr/bin/env python3
"""
Test PDF loading functionality
"""

import os
import sys
from llama_index.core import SimpleDirectoryReader

def test_pdf_loading():
    """Test PDF loading functionality."""
    # Get the project root directory
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Path to the Document directory
    document_dir = os.path.join(project_root, "Document")
    
    # Check if Document directory exists
    if not os.path.exists(document_dir):
        print(f"Error: Document directory not found at {document_dir}")
        print("Creating Document directory...")
        os.makedirs(document_dir)
        print(f"Document directory created at {document_dir}")
        print("Please add PDF files to the Document directory and run this script again")
        sys.exit(1)
    
    # Check if there are PDF files in the Document directory
    pdf_files = [f for f in os.listdir(document_dir) if f.lower().endswith('.pdf')]
    if not pdf_files:
        print(f"Error: No PDF files found in {document_dir}")
        print("Please add PDF files to the Document directory and run this script again")
        print("You can use the create_sample_pdf.py script to create a sample PDF file")
        sys.exit(1)
    
    print(f"Found {len(pdf_files)} PDF files: {', '.join(pdf_files)}")
    
    # Try to load the PDF files
    try:
        print("Loading PDF files...")
        # Load documents using SimpleDirectoryReader
        documents = SimpleDirectoryReader(
            document_dir
        ).load_data()
        
        print(f"Successfully loaded {len(documents)} documents")
        
        # Print some information about the documents
        for i, doc in enumerate(documents):
            print(f"\nDocument {i+1}:")
            print(f"  Filename: {doc.metadata.get('file_name', 'Unknown')}")
            print(f"  Page: {doc.metadata.get('page_label', 'Unknown')}")
            print(f"  Text length: {len(doc.text)} characters")
            print(f"  Text preview: {doc.text[:100]}...")
        
        print("\nPDF loading test successful!")
    except Exception as e:
        print(f"Error loading PDF files: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    test_pdf_loading()