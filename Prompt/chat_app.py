
import streamlit as st
import sys
from pathlib import Path

# -------------------------------
# IMPORT MODEL
# -------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

sys.path.insert(0, str(BASE_DIR / "ChatModels"))

from tinyllama_model import load_tinyllama


# -------------------------------
# PAGE CONFIGURATION
# -------------------------------

st.set_page_config(
    page_title="TinyChat AI",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 TinyChat AI")
st.caption("Your personal AI assistant powered by TinyLlama")


# -------------------------------
# LOAD MODEL ONLY ONCE
# -------------------------------

@st.cache_resource(show_spinner="Loading TinyLlama...")
def get_llm():
    return load_tinyllama()


llm = get_llm()


# -------------------------------
# INITIALIZE CHAT HISTORY
# -------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# -------------------------------
# SIDEBAR
# -------------------------------

with st.sidebar:

    st.header("🤖 TinyChat AI")

    st.success("TinyLlama 1.1B")

    st.caption("Running locally on your computer.")

    st.divider()

    st.write(f"Messages: {len(st.session_state.messages)}")

    if st.button("🗑️ Clear Conversation", use_container_width=True):

        st.session_state.messages = []

        st.rerun()


# -------------------------------
# SYSTEM PROMPT
# -------------------------------

SYSTEM_PROMPT = """
You are TinyChat, a helpful AI assistant.

Instructions:
- Answer the user's actual question.
- Use simple and clear English.
- Give relevant and useful information.
- Keep answers organized.
- Do not repeat the question unnecessarily.
- If you do not know an answer, admit it.
- Never invent facts intentionally.
"""


# -------------------------------
# DISPLAY WELCOME MESSAGE
# -------------------------------

if not st.session_state.messages:

    with st.chat_message("assistant"):

        st.markdown(
            "Hello! 👋 I'm TinyChat AI.\n\n"
            "Ask me anything. How can I help you today?"
        )


# -------------------------------
# DISPLAY CHAT HISTORY
# -------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# -------------------------------
# CHAT INPUT
# -------------------------------

user_prompt = st.chat_input("Message TinyChat AI...")


if user_prompt:

    # Display user message
    with st.chat_message("user"):

        st.markdown(user_prompt)

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_prompt
    })

    # Keep the latest 10 messages
    recent_messages = st.session_state.messages[-10:]

    # Build TinyLlama chat prompt
    conversation = f"<|system|>\n{SYSTEM_PROMPT}</s>\n"

    for message in recent_messages:

        role = message["role"]
        content = message["content"]

        conversation += f"<|{role}|>\n{content}</s>\n"

    conversation += "<|assistant|>\n"

    # Generate response
    with st.chat_message("assistant"):

        with st.spinner("TinyLlama is thinking..."):

            try:

                response = llm.invoke(conversation)

                response = response.strip()

                if not response:
                    response = "I couldn't generate a response. Please try again."

                st.markdown(response)

                # Save AI response
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": response
                })

            except Exception as e:

                st.error(f"Something went wrong: {e}")
