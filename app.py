import streamlit as st
from privacy import redact_pii

st.title("Clinical AI Prototype")
transcript = st.text_area("Paste Session Transcript:")

if st.button("Process Securely"):
    if transcript:
        safe_text = redact_pii(transcript)
        st.write("Processing (PII Redacted):", safe_text)
        # Your AI logic goes here
