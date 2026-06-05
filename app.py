import streamlit as st
from privacy import redact_pii

# 1. Initialize the session state variable if it doesn't exist
if 'redacted_text' not in st.session_state:
    st.session_state.redacted_text = ""

st.title("Clinical AI Prototype")
transcript = st.text_area("Paste Session Transcript:")

# 2. When button is clicked, update the session state
if st.button("Secure & Analyze"):
    if transcript:
        st.session_state.redacted_text = redact_pii(transcript)

# 3. Always display whatever is currently in the session state
if st.session_state.redacted_text:
    st.subheader("Redacted Output:")
    st.write(st.session_state.redacted_text)
