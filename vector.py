from langchain_ollama import OllamaEmbeddings           # Import the embedding model from Ollama
from langchain_chroma import Chroma                     # Import Chroma, the vector database used to store and search documents
from langchain_core.documents import Document           # Import Document to structure text and its associated metadata
import os
import pandas as pd


# Load restaurant reviews from the CSV file into a DataFrame
df = pd.read_csv("realistic_restaurant_reviews.csv")

# Initialize the embedding model, it converts text into numerical vectors (embeddings)
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

# Define the directory where the Chroma database will be stored
db_location = "./chrome_langchain_db"

# Check if the database directory already exists
# If it doesn't exist, we need to add the documents for the first time
add_documents = not os.path.exists(db_location)

# Prepare the documents and their IDs if the database doesn't exist
if add_documents:
    documents = []
    ids = []

    # Iterate through each row of the CSV file
    for i, row in df.iterrows():
        
        # Create a Document containing the review text and its metadata
        document = Document(
            page_content=row["Title"] + " " + row["Review"],            # Main text used for embedding
            metadata={"rating": row["Rating"], "date": row["Date"]},    # Additional informations
            id=str(i) # Unique document identifier
        )
        # Store the document ID and the document itself
        ids.append(str(i))
        documents.append(document)

# Initialize the Chroma vector database        
vector_store = Chroma(
    collection_name="restaurant_reviews",       # Name of the collection
    persist_directory=db_location,              # Directory used to save the database
    embedding_function=embeddings               # Model used to generate embeddings
)

# Add documents to Chroma only during the initial setup
if add_documents:
    vector_store.add_documents(documents=documents, ids=ids)

# Create a retriever to search for relevant documents
retriever = vector_store.as_retriever(
    search_kwargs={"k": 5}      # Return the 5 most relevant reviews
)