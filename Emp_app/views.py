
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .models import Program 
from .models import EmpDetails 
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect


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
     
     
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request,'change_password.html',{
        'form': form
    })

def login_base(request):
    return render(request, "login_base.html")