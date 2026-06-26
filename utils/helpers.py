def extract_domain(company: str) -> str:
    """Simple extraction: e.g., 'Microsoft' -> 'microsoft.com'"""
    return f"{company.lower().replace(' ', '')}.com"

def format_status(status: str) -> str:
    return f"*{status}*"