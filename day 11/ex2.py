import re

def extract_dates(text):
    # Regex to match DD-MM-YYYY or DD/MM/YYYY
    pattern = r"\b\d{2}[-/]\d{2}[-/]\d{4}\b"
    return re.findall(pattern, text)


# Example usage
sample_text = "Important dates: 12-08-2025, 21/08/2025, and 05-09-2023."
print(extract_dates(sample_text))
