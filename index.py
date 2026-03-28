import streamlit as st
from transformers import pipeline

# --- UI/UX CONFIGURATION ---
st.set_page_config(page_title="Zenith AI", page_icon="🤖")

# Custom CSS for a modern Chat UX
st.markdown("""
    <style>
    .stChatFloatingInputContainer { background-color: rgba(0,0,0,0); }
    .stChatMessage { border-radius: 15px; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- AI BACKEND (The Model) ---
@st.cache_resource
def load_chatbot():
    # Using 'Blenderbot', a high-quality conversational AI by Meta
    return pipeline("conversational", model="facebook/blenderbot-400M-distill")

chatbot = load_chatbot()

# --- CHAT HISTORY STORAGE ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- UI LAYOUT ---
st.title("🤖 Zenith AI")
st.caption("A lightweight conversational assistant powered by Blenderbot.")

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Message Zenith AI..."):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            from transformers import Conversation
            # Create conversation object for the model
            conversation = Conversation(prompt)
            result = chatbot(conversation)
            response = result.generated_responses[-1]
            st.markdown(response)
    
    # Add assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": response})
