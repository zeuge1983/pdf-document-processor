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
   - **IMPORTANT**: Make sure to use a valid API key from [Google AI Studio](https://aistudio.google.com/app/apikey)
   - The API key should have access to the following Gemini models:
     - `models/text-embedding-004` (for embeddings)
     - `models/gemini-1.5-pro-001` (for text generation)
   - If you encounter API key errors, verify that:
     - The key is correctly copied without any extra spaces
     - The key is active and has not expired
     - You have sufficient quota for the Gemini API

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

## Troubleshooting

### API Key Issues

If you encounter errors related to the API key:

1. **Invalid API Key Error**: 
   - Verify that your API key is correctly copied into the `.env` file
   - Make sure there are no extra spaces or characters
   - Get a new API key from [Google AI Studio](https://aistudio.google.com/app/apikey) if needed

2. **Environment Variable Not Found**:
   - Check that the `.env` file exists in the project root directory
   - Ensure the file contains the line `GOOGLE_API_KEY=your_api_key_here` with your actual API key
   - Try setting the environment variable directly in your terminal:
     ```bash
     export GOOGLE_API_KEY=your_api_key_here
     ```

3. **Model Access Issues**:
   - Ensure your API key has access to the required models
   - Check your quota limits in the Google AI Studio dashboard

### PDF Processing Issues

1. **No PDF Files Found**:
   - Verify that your PDF files are placed in the `Document` folder in the project root
   - Check that the files have a `.pdf` extension

2. **Error Processing PDFs**:
   - Make sure the PDF files are not corrupted or password-protected
   - Try with a simpler PDF file to test

### ChromaDB Issues

1. **ChromaDB Connection Errors**:
   - Ensure that ChromaDB is properly installed
   - Check for any firewall or permission issues

### Running the Test Scripts

To verify that your environment is set up correctly, run the test scripts:

1. Test environment variables:
   ```bash
   python test_env.py
   ```
   This will check if your API key is properly set in the environment.

2. Test Gemini API models:
   ```bash
   python test_gemini.py
   ```
   This will verify that your API key can access the required Gemini models:
   - `models/text-embedding-004` for embeddings
   - `models/gemini-1.5-pro-001` for text generation

If you encounter any errors with the test scripts, make sure:
- Your API key is correctly set in the `.env` file
- Your API key has access to the required models
- You have sufficient quota for the Gemini API

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.