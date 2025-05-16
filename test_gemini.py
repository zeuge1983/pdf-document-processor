#!/usr/bin/env python3
"""
Test script to verify Gemini API key and models.
"""

import os
import sys
from dotenv import load_dotenv
import google.generativeai as genai

def main():
    """Test Gemini API key and models."""
    # Load environment variables from .env file
    load_dotenv()
    
    # Get API key
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("Error: GOOGLE_API_KEY environment variable not set.")
        print("Please create a .env file with your API key or set it in your environment.")
        sys.exit(1)
    
    # Configure Gemini API
    genai.configure(api_key=api_key)
    
    print("Testing Gemini API key and models...")
    
    # Test embedding model
    try:
        print("\nTesting embedding model (models/text-embedding-004)...")
        result = genai.embed_content(
            model="models/text-embedding-004",
            content="This is a test",
            task_type="RETRIEVAL_DOCUMENT"
        )
        print(f"Embedding model test successful!")
        print(f"Embedding dimension: {len(result.embedding)}")
    except Exception as e:
        print(f"Error testing embedding model: {e}")
    
    # Test generative model
    try:
        print("\nTesting generative model (models/gemini-1.5-pro-001)...")
        model = genai.GenerativeModel('models/gemini-1.5-pro-001')
        response = model.generate_content("Hello, how are you?")
        print(f"Generative model test successful!")
        print(f"Response: {response.text[:100]}...")
    except Exception as e:
        print(f"Error testing generative model: {e}")
    
    print("\nTest complete!")

if __name__ == "__main__":
    main()