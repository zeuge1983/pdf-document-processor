#!/usr/bin/env python3
"""
Run script for the PDF Document Processor
"""

import os
import sys
import subprocess
from dotenv import load_dotenv

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

def main():
    """Run the PDF Document Processor."""
    # Get the directory of this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Path to the main.py file
    main_py = os.path.join(script_dir, "src", "main.py")
    
    # Check if main.py exists
    if not os.path.exists(main_py):
        print(f"Error: {main_py} not found")
        sys.exit(1)
    
    # Make main.py executable
    try:
        os.chmod(main_py, 0o755)
    except Exception as e:
        print(f"Warning: Could not make {main_py} executable: {str(e)}")
    
    # Run main.py
    try:
        # Pass the current environment variables to the subprocess
        env = os.environ.copy()
        subprocess.run([sys.executable, main_py], check=True, env=env)
    except subprocess.CalledProcessError as e:
        print(f"Error running {main_py}: {str(e)}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)

if __name__ == "__main__":
    main()