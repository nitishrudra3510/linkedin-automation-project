"""Simple personalization utilities to clean tone and inject tokens."""
import re


def sanitize_text(text: str) -> str:
    """Remove excessive whitespace and line breaks."""
    if not text:
        return ''
    return re.sub(r"\s+", ' ', text).strip()


def personalize_template(template: str, tokens: dict) -> str:
    """Replace tokens like {{name}} with provided values."""
    result = template
    for k, v in tokens.items():
        result = result.replace(f'{{{{{k}}}}}', str(v or ''))
    return sanitize_text(result)
