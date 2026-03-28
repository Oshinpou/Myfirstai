import streamlit as st
from transformers import pipeline

# --- 1. PAGE CONFIGURATION (UX) ---
st.set_page_config(
    page_title="Zenith AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Custom CSS to make it look like a modern chat app
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    .stChatMessage { border-radius: 15px; border: 1px solid #30363d; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. THE AI BRAIN (Backend) ---
@st.cache_resource
def load_chatbot():
    # We use Blenderbot-400M because it fits in the 2GB RAM limit of free hosts
    return pipeline("conversational", model="facebook/blenderbot-400M-distill")

chat_pipeline = load_chatbot()

# --- 3. CHAT MEMORY (Logic) ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- 4. THE USER INTERFACE (Frontend) ---
st.title("🤖 Zenith AI")
st.caption("A smart conversational assistant powered by Open Source AI.")

# Display existing chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle new user input
if prompt := st.chat_input("How can I help you today?"):
    # Add user message to UI and State
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate AI Response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            from transformers import Conversation
            
            # Create a conversation object with history
            # This allows the AI to "remember" context
            past_user_inputs = [m["content"] for m in st.session_state.messages if m["role"] == "user"]
            generated_responses = [m["content"] for m in st.session_state.messages if m["role"] == "assistant"]
            
            # Pass the current prompt and history to the model
            conversation = Conversation(
                text=prompt, 
                past_user_inputs=past_user_inputs[:-1], 
                generated_responses=generated_responses
            )
            
            result = chat_pipeline(conversation)
            full_response = result.generated_responses[-1]
            
            st.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
