#!/usr/bin/env python3
"""
Test the Google Gemini API key
"""

import os
import sys
import google.generativeai as genai
from dotenv import load_dotenv

def test_api_key():
    """Test the Google Gemini API key."""
    # Get the project root directory
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Load environment variables from .env file
    env_file = os.path.join(project_root, ".env")
    if os.path.exists(env_file):
        load_dotenv(env_file)
        print(f"Loaded environment variables from {env_file}")
    else:
        print(f"Error: {env_file} not found")
        print("Please create a .env file with your Google Gemini API key")
        print("You can use the update_api_key.py script to create it")
        sys.exit(1)
    
    # Get the API key
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("Error: GOOGLE_API_KEY environment variable not set")
        print("Please set the GOOGLE_API_KEY environment variable")
        sys.exit(1)
    
    # Test the API key
    try:
        print(f"Testing API key: {api_key[:5]}...{api_key[-4:]}")
        
        # Configure the Gemini API
        genai.configure(api_key=api_key)
        
        # List available models
        models = [m.name for m in genai.list_models()]
        print(f"Available models: {models}")
        
        # Test the API with a simple query
        model = genai.GenerativeModel('gemini-1.5-pro')
        response = model.generate_content("Hello, what can you do?")
        
        print("\nAPI test successful!")
        print("Response from Gemini:")
        print(response.text)
    except Exception as e:
        print(f"Error testing API key: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    test_api_key()