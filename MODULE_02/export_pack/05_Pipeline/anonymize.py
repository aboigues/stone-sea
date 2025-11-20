import re, sys
from pathlib import Path

def anonymize_text(text, patterns, repl):
    for p in patterns:
        text = re.sub(p, repl, text)
    return text

def main(input_path, output_path, repl='[ANON]'):
    text = Path(input_path).read_text(errors='ignore')
    patterns = [
        r'\b[0-9]{2}\s?[A-Z]{2}\s?[0-9]{3}\b',
        r'\b\d{2}/\d{2}/\d{4}\b',
        r'(?i)(nom|prénom|email|tél)\s*:.*$'
    ]
    redacted = anonymize_text(text, patterns, repl)
    Path(output_path).write_text(redacted)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
