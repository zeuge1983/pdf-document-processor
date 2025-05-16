"""
Utility functions for the PDF Document Processor
"""

import os
import sys
import logging
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

def check_environment():
    """
    Check if the environment is properly set up.
    Returns True if the environment is ready, False otherwise.
    """
    # Load environment variables from .env file
    env_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".env")
    if os.path.exists(env_file):
        load_dotenv(env_file)
        logger.info("Loaded environment variables from .env file")
    
    # Check if GOOGLE_API_KEY is set
    if not os.getenv("GOOGLE_API_KEY"):
        display_message("GOOGLE_API_KEY environment variable not set", "error")
        display_message("Please set the GOOGLE_API_KEY environment variable.", "info")
        display_message("You can create a .env file with your API key or run:", "info")
        display_message("export GOOGLE_API_KEY=your_api_key", "code")
        return False
    
    return True

def display_header():
    """Display the application header."""
    header = """
╔════════════════════════════════════════════════════════╗
    ║                                                        ║
    ║   PDF Document Processor with Gemini                   ║
    ║                                                        ║
    ║   - Upload PDFs to the Document folder                 ║
    ║   - Ask questions about your documents                 ║
    ║   - Get AI-powered answers using Google Gemini         ║
    ║                                                        ║
    ╚════════════════════════════════════════════════════════╝
"""
    print(header)

def display_message(message, message_type="info"):
    """
    Display a formatted message.
    
    Args:
        message (str): The message to display
        message_type (str): The type of message (info, success, warning, error, code)
    """
    if message_type == "info":
        print(message)
    elif message_type == "success":
        print(f"\033[92m{message}\033[0m")  # Green
    elif message_type == "warning":
        print(f"\033[93m{message}\033[0m")  # Yellow
    elif message_type == "error":
        print(f"\033[91m{message}\033[0m")  # Red
    elif message_type == "code":
        print(f"\033[96m{message}\033[0m")  # Cyan

def get_user_input(prompt):
    """
    Get input from the user.
    
    Args:
        prompt (str): The prompt to display
    
    Returns:
        str: The user input
    """
    try:
        return input(prompt + " ")
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)
    except EOFError:
        print("\nExiting...")
        sys.exit(0)