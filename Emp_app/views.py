
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login

def home(request):
     return render(request, "Emp_app/home.html")

# def forgetpassword(request):
#      return render(request, "Emp_app/forgetpassword.html")

    
# def index(request):
#     return render(request, "Emp_app/index.html")


# def employee(request):
#      return render(request, "Emp_app/employee.html")



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