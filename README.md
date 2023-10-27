Certainly! Here's a markdown README for your project:

---

# Ask Your CSV and Multi-File Chat Interface

This project provides a Streamlit application where you can upload CSV files to ask questions directly. Moreover, the project allows for the upload of multiple files and provides a chat interface for interacting with them.

## Table of Contents

- [Setup](#setup)
- [Usage](#usage)
- [File Overview](#file-overview)
- [Contributing](#contributing)
- [License](#license)

## Setup

1. **Environment Variables**: Before running the application, ensure you have set up the necessary environment variables. Particularly the OpenAI API key. You can use `.env` files with the `dotenv` package to manage your secret and environment variables.

2. **Dependencies**: Install the required dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the Streamlit application using the following command to run for PDF:

```bash
streamlit run app.py
```

Run the Streamlit application using the following command to run for CSV:

```bash
streamlit run csvmain.py
```

1. **Upload PDF/CSV**: Use the "Upload a CSV file / PDF " option to upload your CSV.
2. **Ask Questions**: Once uploaded, you can ask questions about the CSV in the provided input box.
3. **Multi-File Upload and Chat**: You can also upload multiple files (PDF, DOCX, TXT, CSV, XLSX) and then ask questions related to their content in the chat interface.

## File Overview

1. **csvmain**: Contains the main logic to upload a CSV and ask questions about it using OpenAI.
2. **app.py**: This is the main Streamlit application file that provides the interface for multi-file uploads and chat interactions.
3. **main.py**: Manages the document loading for multiple file formats and runs the chat interface for them.

### csvmain

Main file for the CSV querying feature. It uses the `langchain` library in combination with OpenAI to understand and answer questions about the uploaded CSV.

### app.py

Streamlit interface for the application. Provides multi-file upload capabilities and a simple chat interface.

### main.py

Processes different file formats such as PDFs, DOCX, TXT. Breaks down the documents and uses the `langchain` library for interacting with them.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

[MIT License](https://opensource.org/licenses/MIT)
