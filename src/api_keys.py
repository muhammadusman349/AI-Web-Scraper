import streamlit as st
import os


def get_api_keys(api_keys_name):
    if api_keys_name == "OPENAI_API_KEY":
        return st.session_state['openai_api_key'] or os.getenv(api_keys_name)
    elif api_keys_name == "GOOGLE_API_KEY":
        return st.session_state['gemini_api_key'] or os.getenv(api_keys_name)
    elif api_keys_name == "GROQ_API_KEY":
        return st.session_state['groq_api_key'] or os.getenv(api_keys_name)
    else:
        return os.getenv(api_keys_name)
