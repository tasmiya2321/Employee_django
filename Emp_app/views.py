
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .models import Program 
from .models import EmpDetails 



from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'Emp_app/reset_password.html'
    email_template_name = 'Emp_app/email.html'
    subject_template_name ='Emp_app/subject_email'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('index')
    


def home(request):
    programs = Program.objects.exclude(date__isnull=True).order_by('pgm_id')[:10]
    
    # Debugging: Print each program's date
    for program in programs:
        print(program.date)

    return render(request, "Emp_app/home.html", {'programs': programs})





def forgetpassword(request):
     return render(request, "Emp_app/forgetpassword.html")


    
def index(request):
    return render(request, "Emp_app/index.html")

    
def employee(request):
    return render(request, "Emp_app/employee.html")

def reset_password(request):
     return render(request, "Emp_app/reset_password.html")

def email(request):
     return render(request, "Emp_app/email.html")

def subject_email(request):
     return render(request, "Emp_app/subject_email.txt")

# def employee(request):
#         # Query the EmpDetails model for all records
#     emp_details = EmpDetails.objects.all()

#     # Pass the queried data to the template
#     context = {
#         'emp_details': emp_details
#     }
#     return render(request, "Emp_app/employee.html", context)



def userlogin(request):

      if request.method == 'POST':
       
        username = request.POST['username']
        password = request.POST['password']
       
        user = authenticate(username=username, password=password)
        if user is not None:
            
            login(request, user)
            
            return render(request, 'index.html')
        else:
           
            return render(request, 'login.html', {'error_message': 'Incorrect username and / or password.'})
      else:
        
         return render(request, 'login.html') 