from langchain_ollama.llms import OllamaLLM                 # Import the Ollama LLM to use a locally running language model 
from langchain_core.prompts import ChatPromptTemplate       # Import the class used to create and manage prompt templates 
from vector import retriever                                # Import the retriever defined in vector.py to search for relevant reviews

# Initializing the Llama 3.1:8b model using Ollama
model = OllamaLLM(model="llama3.1:8b")


# Define the prompt that will be sent to the LLM, it contains the retrieved reviews and the user's question
template = """
You are an exeprt in answering questions about a pizza restaurant
Here are some relevant reviews: {reviews}
Here is the question to answer: {question}
"""

# Create a prompt template from the text above
prompt = ChatPromptTemplate.from_template(template)

# Connect the prompt to the LLM to create a processing chain
chain = prompt | model


def ask_question(question):
    # Search the vector database for reviews relevant to the question
    reviews = retriever.invoke(question)        # Sends the user's question to the retriever, Searches the vector database, Returns relevant reviews

    # Send the retrieved reviews and question to the LLM
    # The LLM uses the reviews as context to generate its answer
    result = chain.invoke({ "reviews": reviews, "question": question })     # Passes the actual reviews and question to the chain, Fills the template placeholders, Sends the resulting prompt to the LLM

    return result