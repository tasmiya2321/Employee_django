
from django import template

register = template.Library()

@register.filter(name='resourcetype_to_string')
def resourcetype_to_string(value):
    # Define your mapping
    mapping = {
        1: "Employee",
        2: "Part-time",
        3: "Consultant",
    }
    # Check if value is None and handle it
    if value is None:
        return "Not specified"  # Or whatever default value you deem appropriate

    # Convert value to int if it's not already, to ensure the lookup works
    try:
        value_int = int(value)
    except (ValueError, TypeError):
        # If conversion fails, return the value as is or some default string
        return "Invalid"  # Or return "Unknown" or any placeholder here
    
    # Return the string representation if found, else "Unknown"
    return mapping.get(value_int, "Unknown")