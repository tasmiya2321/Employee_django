from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .models import Program 
from .models import EmpDetails 
import json

def home(request):
    programs = Program.objects.all().order_by('pgm_id')[:10]
    return render(request, 'Emp_app/home.html', {'programs': programs})



def forgetpassword(request):
     return render(request, "Emp_app/forgetpassword.html")


    
def index(request):
    return render(request, "Emp_app/index.html")

@csrf_exempt
def employee(request):
       if request.method=='GET':
   
         return render(request, "Emp_app/employee.html")
       else:
           var=request.POST.get("data")
           var=var[:len(var)-1]
           var=var.strip()
        
           #emp_details = EmpDetails.objects.filter(fullname=var).values()
           variable_column = 'fullname'
           search_type = 'iexact'
           strfilter = variable_column + '__' + search_type
           emp_details=EmpDetails.objects.filter(**{ strfilter:var })

           my_dict = model_to_dict(emp_details[0], fields=['fullname', 'emp_id', 'address', 'dob', 'phone_number','email_id', 'gender', 'center', 'designation','date_of_joining', 'education_qualification', 'status','resource_type', 'date_of_resigning', 'bank_name', 
                  'name_as_per_bank', 'account_number', 'ifsc', 'account_type'])
          
           return JsonResponse( {"info": json.dumps(my_dict)} )
          # return render(request, "Emp_app/employee.html",{"info":emp_details})
           
       

def reset_password(request):
     return render(request, "Emp_app/reset_password.html")




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