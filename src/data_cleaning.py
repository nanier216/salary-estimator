import re

def clean_text(text):
    if not isinstance(text, str):
        return ""
    
    text = text.lower()
    text = re.sub(r"<[^>]+>", " ", text)  # remove HTML tags
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)  # remove punctuation
    text = re.sub(r"\s+", " ", text)  # remove extra spaces
    return text.strip()

