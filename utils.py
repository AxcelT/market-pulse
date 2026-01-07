from typing import Optional, Union

def safe_fmt(value: Optional[float], suffix: str = "") -> str:
    """
    Formats a numeric value into a string with 2 decimal places.
    If the value is None, it returns 'N/A'.
    
    The function accepts an optional suffix (like '%') to append 
    only when the value is valid.
    """
    if value is None:
        return "N/A"
    
    return f"{value:.2f}{suffix}"