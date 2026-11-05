# 🍕 Local Restaurant AI Agent with RAG

A local AI-powered chatbot built with **LangChain, Ollama, ChromaDB, and Streamlit**. It allows users to ask questions about pizza restaurant and receive answers based on real customer reviews.

The project uses **Retrieval-Augmented Generation (RAG)** to retrieve relevant restaurant reviews from a vector database and provide them as context to a local LLM before generating an answer.

Everything runs locally using Ollama, without requiring an external LLM API key.

## 🚀 Features

- **Local LLM:** Uses Llama 3.1:8b through Ollama to generate answers.
- **Document Embeddings:** Converts restaurant reviews into vector representations using `mxbai-embed-large`.
- **Vector Database:** Stores and manages review embeddings using ChromaDB.
- **Semantic Search:** Retrieves the 5 most relevant reviews based on the user's question.
- **RAG Pipeline:** Combines retrieved reviews with the user's question to generate context-aware answers.
- **Chat Interface:** Provides an interactive chatbot using Streamlit.
- **Persistent Storage:** Saves the vector database locally to avoid recreating it every time.

## 🏗️ Project Architecture

```text
LocalRestaurantAIAgentWithRAG/
│
├── app.py                         # Streamlit chat interface
├── main.py                        # LLM and RAG chain logic
├── vector.py                      # Embeddings and vector database
├── realistic_restaurant_reviews.csv # Restaurant reviews dataset
├── requirements.txt               # Python dependencies
├── README.md                      # Project documentation
│
└── chrome_langchain_db/           # Generated Chroma vector database
```

### How does it work?

1. **Load Data:** Restaurant reviews are loaded from the CSV file.
2. **Generate Embeddings:** The embedding model converts review texts into numerical vectors.
3. **Store Documents:** The vectors and associated metadata are stored in ChromaDB.
4. **Retrieve Reviews:** When a user asks a question, the retriever searches for the 5 most relevant reviews.
5. **Generate Answer:** The retrieved reviews and the user's question are passed to Llama 3.1 through a LangChain chain.
6. **Display Response:** Streamlit displays the generated answer in the chatbot interface.

### Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| LangChain | Builds the RAG pipeline |
| Ollama | Runs LLMs locally |
| Llama 3.1 (8B) | Generates answers |
| mxbai-embed-large | Generates text embeddings |
| ChromaDB | Stores and retrieves vectors |
| Pandas | Loads and processes CSV data |
| Streamlit | Builds the chatbot interface |

## ⚙️ Installation and Setup

Follow these steps to install and run the project locally.

### 1. Install Ollama

First, download and install Ollama:

https://ollama.com/download

Ollama allows you to run large language models locally on your machine.

After installation, open a terminal and verify that Ollama is available:

```powershell
ollama --version
```

### 2. Download the Required Models

This project requires two models.

**A. Llama 3.1 (8B)**

The language model responsible for generating answers.

```powershell
ollama pull llama3.1:8b
```

**B. mxbai-embed-large**

The embedding model responsible for converting restaurant reviews into vectors.

```powershell
ollama pull mxbai-embed-large
```

Verify that both models are installed:

```powershell
ollama list
```

Make sure Ollama is running in the background before starting the application.

### 3. Clone the Repository

Clone the project from GitHub:

```powershell
git clone https://github.com/Abdou022/LocalRestaurantAIAgentWithRAG.git
```

Navigate to the project directory:

```powershell
cd LocalRestaurantAIAgentWithRAG
```

### 4. Create a Virtual Environment

Create a Python virtual environment:

```powershell
python -m venv venv
```

Activate the virtual environment:

```powershell
.\venv\Scripts\Activate.ps1
```

You should now see `(venv)` at the beginning of your terminal prompt.

### 5. Install Dependencies

The project dependencies are listed in `requirements.txt`:

```text
langchain
langchain-ollama
langchain-chroma
pandas
streamlit
```

Install all required packages with:

```powershell
pip install -r .\requirements.txt
```

### 6. Create the Chroma Vector Database

Before running the application for the first time, initialize the vector database.

Execute:

```powershell
python -c "import vector"
```

This command imports `vector.py`, which automatically:

- Loads the restaurant reviews from the CSV file.
- Generates embeddings using `mxbai-embed-large`.
- Creates the ChromaDB collection.
- Stores the documents and their embeddings in `chrome_langchain_db/`.

**Note:** The database is created only if its directory does not already exist. On subsequent runs, the existing database is reused instead of adding all documents again.

The initial creation may take some time depending on the size of the dataset and your hardware.

### 7. Run the Application

Once the vector database is initialized, start the Streamlit application:

```powershell
streamlit run app.py
```

Streamlit will start the application and provide a local URL, usually:

```text
http://localhost:8501
```

Open this URL in your browser to interact with the chatbot.

## 💬 Example Questions

You can ask questions such as:

- What do customers think about the restaurant?
- What are the most common complaints?
- Are customers satisfied with the food quality?
- What do customers say about the restaurant's service?
- What is the overall customer experience?

The chatbot retrieves relevant reviews and uses them as context to generate its answers.

## 📌 Important Notes

- Make sure Ollama is installed and running before launching the application.
- Both required models must be downloaded before using the RAG pipeline.
- Keep `realistic_restaurant_reviews.csv` in the project root directory.
- The ChromaDB database is generated locally and does not need to be downloaded from GitHub.
- If you modify the CSV dataset and want to rebuild the vector database, remove the existing `chrome_langchain_db` directory and initialize it again using the command from Step 6.

## 👨‍💻 Author

Developed as a learning project to explore **Large Language Models (LLMs), LangChain, embeddings, vector databases, and Retrieval-Augmented Generation (RAG)**.