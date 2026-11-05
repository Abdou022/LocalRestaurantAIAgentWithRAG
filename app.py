import streamlit as st
from main import ask_question

st.set_page_config(page_title="Restaurant RAG Chatbot", page_icon="🍕")

st.title("🍕 Restaurant Reviews Chatbot")
st.write("Ask me anything about our restaurants!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get user input
question = st.chat_input("Ask your question...")

if question:
    # Display user message
    with st.chat_message("user"):
        st.markdown(question)

    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    # Generate and display assistant response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            result = ask_question(question)
            st.markdown(result)

    st.session_state.messages.append({
        "role": "assistant",
        "content": result
    })