from django import template
from django.db.models.fields.json import KeyTransformEndsWith 

register = template.Library()  
@register.filter(name='program_to_string')
def program_to_string(value):
    program_names = {
        1: "Bridge Course",
        2: "Academics",
        3: "After School Program",
        4: "Awareness Sessions",
        5: "Camps(Summer/Winter)",
        6: "Career Guidance",
        7: "Computer Coaching - Advanced",
        8: "Computer Coaching - Basics with Typing",
        9: "Computer Coaching - Basics without Typing",
        10: "Computer Coaching - Typing",
        11: "Counselling",
        12: "E2E(Education to Employability)",
        13: "Emotional Management",
        14: "Exam Readiness",
        15: "Gender Sensitivity",
        16: "Internship",
        17: "Integrated Program",
        18: "Kannada",
        19: "Lifeskills",
        20: "Office Assistant",
        21: "Parental Guidance",
        22: "Personality Development",
        23: "Softskills",
        24: "Software Program",
        25: "Spoken English",
        26: "Tailoring",
        27: "Tailoring - Tassel Typing",
        28: "Tally",
        29: "Teacher Development",
        30: "TTT",
        31: "Well being",
        32: "Women Development",
        33: "WSD"
    }
    return program_names.get(value, f"{value}")


@register.filter()
def centertype_to_string(value):
    centertype_names = {
        1: "DJ_halli 1",
        2: "DJ_halli 2",
        3: "Bagalur",
        4: "Mylanahalli",
        5: "Kannur",
        6: "Koramangala"
    }
    return centertype_names.get(value, f"{value}")

@register.filter()
def Sponser_to_string(value):
    Sponser_names = {
        1: "Vajira",
        2: "Bridge",
        3: "Taste master",
        4: "LICT"
       
    }
    return Sponser_names.get(value, f"{value}")

@register.filter()
def TrainerType_to_string(value):
    TrainerType_names = {
        1: "Lead",
        2: "CO-Facilator",
        3: "Volunteer Type",
      
    }
    return TrainerType_names.get(value, f"{value}")

@register.filter()
def Catagory_to_string(value):
     Category_names = {
        1: "Consultant",
        2: "Employee",
        3: "Internship",
        4: "New Volunteer",
        5: "EX-Volunteer"
       
    }
     return Category_names.get(value, f"{value}")

 
@register.filter()
def Status_to_string(value):
     Status_names = {
        1: "Start",
        2: "On-going",
        3: "On-Hold",
        4: "Completed",
        5: "Travel",
        6: "Orientation"
       
    }
     return Status_names.get(value, f"{value}")

 
