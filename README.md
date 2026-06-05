# nvovpsych-cllinical-asisstant

NovoBridge: Clinical AI Co-Pilot Prototype
Objective: To bridge the gap between clinical documentation and patient psychometric monitoring, reducing administrative friction for mental health professionals.

Why I Built This
NovoPsych is leading the way in clinical SaaS. I recognized that while AI scribing is powerful, its true potential lies in interactive data synthesis. I designed this prototype to demonstrate how we can safely map session context to psychometric tracking (e.g., DASS-21) while maintaining HIPAA-grade privacy standards.

Key Engineering Decisions
Privacy-First Architecture: Before any text is processed by an LLM, it passes through an in-memory PII-redaction layer to ensure patient anonymity.

Clinician-in-the-Loop: Designed to suggest structured clinical notes (SOAP format) for human expert review, rather than automating final decisions.

Tech Stack: Python, Streamlit (for UI), OpenAI API (for natural language synthesis).

How to Use
Select the relevant psychometric track.

Paste the session transcript.

Click "Secure & Analyze" to generate a PII-scrubbed clinical draft.

https://novopsych-clinical-assistant-pvgkmjoaqdcew9ezxtnvya.streamlit.app/ 
