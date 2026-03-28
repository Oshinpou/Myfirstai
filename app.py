import streamlit as st
from transformers import pipeline, Conversation

# --- PAGE CONFIG ---
st.set_page_config(page_title="Nova AI", page_icon="✨", layout="centered")

# --- CUSTOM UI/UX (CSS) ---
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    .stChatMessage { border-radius: 10px; border: 1px solid #30363d; }
    </style>
    """, unsafe_allow_html=True)

# --- AI MODEL ENGINE ---
@st.cache_resource
def load_ai():
    # We use a 'Distilled' model because it's faster and smaller for free hosting
    return pipeline("conversational", model="facebook/blenderbot-400M-distill")

chat_engine = load_ai()

# --- SESSION HANDLING ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- HEADER ---
st.title("✨ Nova AI Assistant")
st.info("I am a lightweight AI running on a free server. I can chat, answer questions, and remember our conversation!")

# --- CHAT INTERFACE ---
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask me anything..."):
    # User message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # AI response
    with st.chat_message("assistant"):
        with st.spinner("Processing..."):
            conv = Conversation(prompt)
            # Add past context so the AI "remembers"
            result = chat_engine(conv)
            ai_response = result.generated_responses[-1]
            st.markdown(ai_response)
            
    st.session_state.messages.append({"role": "assistant", "content": ai_response})
