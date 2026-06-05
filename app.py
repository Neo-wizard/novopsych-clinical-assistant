import streamlit as st
from privacy import redact_pii
from openai import OpenAI

# Initialize client (Ensure you have your key in Streamlit Secrets)
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("🧠 NovoBridge: Clinical Synthesis")

# Sidebar for Psychometric Selection
metric = st.sidebar.selectbox("Select Psychometric Track", ["DASS-21 (Depression/Anxiety)", "ADHD Adult Scale"])

transcript = st.text_area("Paste Transcript:")

if st.button("Generate Insight"):
    # 1. Redact
    safe_text = redact_pii(transcript)
    
    # 2. Analyze against metric
    with st.spinner("Mapping to psychometric indicators..."):
        prompt = f"""
        You are a clinical assistant. Analyze this transcript for markers related to {metric}.
        Transcript: {safe_text}
        
        Output:
        1. List relevant symptoms found.
        2. Draft a SOAP note snippet.
        """
        
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        
        st.write(response.choices.message.content)
