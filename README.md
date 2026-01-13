# Simple Chat Bot

A Streamlit-based chatbot application that uses LangChain and OpenAI to answer questions from uploaded PDF documents using RAG (Retrieval-Augmented Generation).

## Prerequisites

- Python 3.11 or higher
- pip (Python package manager)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd gen-ai
```

### 2. Create a Virtual Environment

Create and activate a virtual environment to isolate project dependencies:

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

Install all required packages from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory of the project:

```bash
touch .env
```

Add your OpenAI API key to the `.env` file:

```
OPENAI_API_KEY=your_openai_api_key_here
```

**Note:** Make sure to replace `your_openai_api_key_here` with your actual OpenAI API key. You can obtain one from [OpenAI's website](https://platform.openai.com/api-keys).

### 5. Verify Setup

Run the sanity check script to verify that all imports are working correctly:

```bash
python rag/sanity_check.py
```

You should see output similar to:
```
3.11.x (main, ...) [...]
ALL IMPORTS OK
```

## Running the Application

Start the Streamlit chatbot application:

```bash
python -m streamlit run rag/chatbot.py
```

The application will start and you should see output like:

```
You can now view your Streamlit app in your browser.

Local URL: http://localhost:8501
Network URL: http://192.168.x.x:8501
```

Open your browser and navigate to `http://localhost:8501` to use the chatbot.

### Optional: Install Watchdog for Better Performance

For better file watching performance (especially on macOS), you can install the watchdog module:

**On macOS:**
```bash
xcode-select --install  # Install Xcode command line tools if not already installed
pip install watchdog
```

**On Linux/Windows:**
```bash
pip install watchdog
```

## Usage

1. Open the application in your browser (http://localhost:8501)
2. Use the sidebar to upload a PDF file
3. Once the PDF is uploaded, type your question in the text input field
4. The chatbot will search through the document and provide an answer based on the content

## Project Structure

```
gen-ai/
├── config/              # Configuration files
│   ├── settings.py      # Environment variable loading
│   └── openai_client.py # OpenAI client setup
├── prompt_engineering/  # Prompt engineering examples
├── rag/                 # RAG (Retrieval-Augmented Generation) implementation
│   ├── chatbot.py       # Main Streamlit chatbot application
│   └── sanity_check.py  # Setup verification script
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Troubleshooting

- **Import errors**: Make sure you've activated your virtual environment and installed all dependencies with `pip install -r requirements.txt`
- **API key errors**: Verify that your `.env` file exists in the root directory and contains a valid `OPENAI_API_KEY`
- **Streamlit not found**: Ensure streamlit is installed: `pip install streamlit`
