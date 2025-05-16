#!/usr/bin/env python3
"""
Test script to verify environment variables are loaded correctly
"""

import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
env_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
if os.path.exists(env_file):
    load_dotenv(env_file)
    print(f"Loaded environment variables from {env_file}")
    api_key = os.getenv("GOOGLE_API_KEY")
    if api_key:
        print(f"API key loaded: {api_key[:5]}...{api_key[-4:]}")
    else:
        print("API key not found in .env file")
else:
    print(f".env file not found at {env_file}")

# Try to configure Gemini API
try:
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    print("Successfully configured Gemini API")
    
    # Try to list models
    models = [m.name for m in genai.list_models()]
    print(f"Available models: {models}")
    
    # Try to get embeddings
    try:
        result = genai.embed_content(
            model="models/embedding-001",
            content="Hello, world!",
            task_type="retrieval_document"
        )
        print("Successfully got embeddings")
        print(f"Embedding dimension: {len(result['embedding'])}")
    except Exception as e:
        print(f"Error getting embeddings: {e}")
except Exception as e:
    print(f"Error configuring Gemini API: {e}")