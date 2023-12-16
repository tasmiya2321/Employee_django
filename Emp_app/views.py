
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .models import Program 
from .models import EmpDetails 

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