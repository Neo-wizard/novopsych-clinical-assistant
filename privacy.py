import re

def redact_pii(text):
    # This redacts anything that looks like an email OR a name-like pattern 
    # (Capitalized words followed by Capitalized words)
    # It also redacts basic phone/digit patterns.
    
    # Redact Emails
    text = re.sub(r'\S+@\S+', '[EMAIL_REDACTED]', text)
    
    # Redact Phone numbers (simple pattern)
    text = re.sub(r'\d{3}-\d{3}-\d{4}', '[PHONE_REDACTED]', text)
    
    # REDACT NAMES: Look for Capitalized Words (e.g., John Doe)
    # Note: This is a simple heuristic for your prototype
    text = re.sub(r'\b[A-Z][a-z]+\s[A-Z][a-z]+\b', '[NAME_REDACTED]', text)
    
    return text
