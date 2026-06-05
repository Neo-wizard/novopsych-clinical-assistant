import re

def redact_pii(text):
    # Simple regex to replace potential emails or names
    # In a real app, you'd use a library like 'presidio', 
    # but this proves you understand the 'Redaction Gate' concept.
    redacted = re.sub(r'\S+@\S+', '[EMAIL_REDACTED]', text)
    return redacted
