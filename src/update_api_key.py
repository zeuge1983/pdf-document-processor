#!/usr/bin/env python3
"""
Update the Google API key in the .env file
"""

import os
import sys

def update_api_key():
    """Update the Google API key in the .env file."""
    # Get the project root directory
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Path to the .env file
    env_file = os.path.join(project_root, ".env")
    
    # Check if .env.template exists
    template_file = os.path.join(project_root, ".env.template")
    if not os.path.exists(template_file):
        print("Error: .env.template file not found")
        sys.exit(1)
    
    # Get the API key from the user
    print("Please enter your Google Gemini API key:")
    print("(You can get one from https://aistudio.google.com/app/apikey)")
    api_key = input("> ").strip()
    
    if not api_key:
        print("Error: API key cannot be empty")
        sys.exit(1)
    
    # Create or update the .env file
    try:
        with open(env_file, "w") as f:
            f.write(f"# Google Gemini API Key\n")
            f.write(f"GOOGLE_API_KEY={api_key}\n")
        
        print(f"API key updated successfully in {env_file}")
    except Exception as e:
        print(f"Error updating API key: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    update_api_key()