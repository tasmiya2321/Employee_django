from django import template

register = template.Library()

@register.filter(name='fullname_to_string')
def fullname_to_string(value):
    mapping = {
        1: "Preethi",
        2: "Sonia",
        3: "Jimmy Cherian",
        4: "Smitha",
        5: "Sujeeth",
    }
    if value is None:
        return "Not specified"

    try:
        value_int = int(value)
    except (ValueError, TypeError):
        return "Invalid" 
    
    return mapping.get(value_int, "Unknown")

@register.filter(name='sponsor_to_string')
def sponsor_to_string(value):
    mapping = {
        1: "Vajra",
        2: "Bridge",
        3: "Taste Master",
        4: "LICT",
        5: "Others",
    }
    return mapping.get(value, "Unknown")


@register.filter(name='category_to_string')
def category_to_string(value):
    mapping = {
        1: "Consultant",
        2: "Employee",
        3: "Internship",
        4: "NewVolunteer",
        5: "ExVolunteer",
    }
    return mapping.get(value, "Unknown")

@register.filter(name='status_to_string')
def status_to_string(value):
    mapping = {
        1: "Start",
        2: "OnGoing",
        3: "OnHold",
        4: "Completed",
        5: "Orientation",
        6: "Travel",
    }
    return mapping.get(value, "Unknown")


# @register.filter(name='centertype_to_string')
# def centertype_to_string(value):
#     centertype_names = {
#         1: "DJ_halli 1",
#         2: "DJ_halli 2",
#         3: "Bagalur",
#         4: "Mylanahalli",
#         5: "Kannur",
#         6: "Koramangala"
#     }
#     return centertype_names.get(value, f"{value}")

