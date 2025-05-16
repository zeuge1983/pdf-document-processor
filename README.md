# PDF Document Processor with Gemini

A Python console application that processes PDF documents using Llama Index, ChromaDB, and Google Gemini API. This application allows users to upload PDFs and ask questions about the content through a chat interface.

## Features

- **PDF Upload**: Place your PDF files in the Document folder for processing
- **Document Indexing**: Uses Llama Index for efficient document indexing
- **Vector Storage**: Stores document chunks in ChromaDB for fast retrieval
- **Gemini Embeddings**: Uses Google's Gemini API for high-quality embeddings
- **Chat Interface**: Ask questions about your documents through a simple console interface
- **Smart Answers**: Get AI-powered answers based on the content of your documents

## Requirements

- Python 3.8+
- Google Gemini API key (get one from [Google AI Studio](https://aistudio.google.com/app/apikey))

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/zeuge1983/pdf-document-processor.git
   cd pdf-document-processor
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your Google Gemini API key:
   - Copy the `.env.template` file to `.env`:
     ```bash
     cp .env.template .env
     ```
   - Edit the `.env` file and add your API key:
     ```
     GOOGLE_API_KEY=your_api_key_here
     ```

## Usage

1. Add your PDF files to the `Document` folder in the project root.

2. Run the application:
   ```bash
   ./run.py
   ```
   or
   ```bash
   python src/main.py
   ```

3. The application will:
   - Load and index your PDF files
   - Store the document chunks in ChromaDB
   - Start a chat interface where you can ask questions

4. In the chat interface:
   - Type your questions about the document content
   - Type `help` to see available commands
   - Type `exit` to quit the application

## Example

```
╔════════════════════════════════════════════════════════╗
    ║                                                        ║
    ║   PDF Document Processor with Gemini                   ║
    ║                                                        ║
    ║   - Upload PDFs to the Document folder                 ║
    ║   - Ask questions about your documents                 ║
    ║   - Get AI-powered answers using Google Gemini         ║
    ║                                                        ║
    ╚════════════════════════════════════════════════════════╝

Found 1 PDF files: Machine_Learning_Guide.pdf
Successfully loaded and stored 2 documents

Documents loaded and indexed successfully!
You can now ask questions about the content of your PDF documents.
Type 'help' for available commands or 'exit' to quit the application.

Your question: What are neural networks?

Processing your question...

Answer:
Neural networks are inspired by the human brain and used for complex pattern
recognition.

Your question: exit

Thank you for using the PDF Document Processor!
```

## Project Structure

- `src/main.py`: Main application code
- `src/utils.py`: Utility functions
- `Document/`: Directory for PDF files
- `run.py`: Convenience script to run the application
- `requirements.txt`: List of dependencies
- `.env.template`: Template for environment variables

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.