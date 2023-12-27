from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .models import Program 
from .models import EmpDetails 
from django.contrib import messages
from django.http import HttpResponseServerError
import json

from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
# class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
#     template_name = 'Emp_app/reset_password.html'
#     email_template_name = 'Emp_app/email.html'
#     subject_template_name ='Emp_app/subject_email'
#     success_message = "We've emailed you instructions for setting your password, " \
#                       "if an account exists with the email you entered. You should receive them shortly." \
#                       " If you don't receive an email, " \
#                       "please make sure you've entered the address you registered with, and check your spam folder."
#     success_url = reverse_lazy('index')
    

def custom_502_view(request, exception=None):
    """Custom view to handle 502 Bad Gateway errors."""
    return HttpResponseServerError('A problem occurred with our server. We\'re working on it!')


def home(request):
    programs = Program.objects.exclude(date__isnull=True).order_by('pgm_id')[:10]

    for program in programs:
        print(program.date)

    return render(request, "Emp_app/home.html", {'programs': programs})



def forgetpassword(request):
     return render(request, "Emp_app/forgetpassword.html")


    
def index(request):
    return render(request, "Emp_app/index.html")




@login_required
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
                  'name_as_per_bank', 'account_number', 'ifsc', 'branch','account_type'])
          
           return JsonResponse( {"info": json.dumps(my_dict)} )
          # return render(request, "Emp_app/employee.html",{"info":emp_details})
   
@login_required
def saveemployee(request):
     Value=request.POST.get('fullname')
     emp_details = EmpDetails.objects.get(fullname=Value)
     Value=request.POST.get('address')
     emp_details.address =Value
     Value=request.POST.get('dob')
     emp_details.dob=Value  
     Value=request.POST.get('phonenumber')
     emp_details.phonenumber=Value  
     Value=request.POST.get('emailId')
     emp_details.emailId=Value  
     Value=request.POST.get('gender')
     emp_details.gender=Value   
     Value=request.POST.get('employeeId')
     emp_details.employeeId=Value  
     Value=request.POST.get('center')
     emp_details.center=Value  
     Value=request.POST.get('designation')
     emp_details.designation=Value   
     Value=request.POST.get('dateofJoining')
     emp_details.dateofJoining=Value   
     Value=request.POST.get('educationQualification')
     emp_details.educationQualification=Value    
     Value=request.POST.get('status')
     emp_details.status=Value  
     Value=request.POST.get('dateofResigning')
     emp_details.dateofResigning=Value  
     Value=request.POST.get('resourceType')
     emp_details.resourceType=Value   
     Value=request.POST.get('bankName')
     emp_details.bankName=Value  
     Value=request.POST.get('nameAsPerBank')
     emp_details.nameAsPerBank=Value  
     Value=request.POST.get('accountNumber')
     emp_details.accountNumber=Value  
     Value=request.POST.get('ifscCode')
     emp_details.ifscCode=Value  
     Value=request.POST.get('branchName')
     emp_details.branchName=Value  
     Value=request.POST.get('accountType')
     emp_details.accountType=Value  
     
    
     emp_details.save()
     
     try:
 
       messages.success(request, 'Employee details updated successfully!')
     except Exception as e:

       messages.error(request, 'Failed to update employee details: {}'.format(e))

    
     return render(request, "Emp_app/employee.html")


def login(request):
     return render(request, "Registration/login.html")

def reset_password(request):
     return render(request, "Emp_app/reset_password.html")

def email(request):
     return render(request, "Emp_app/email.html")


def subject_email(request):
     return render(request, "Emp_app/subject_email.txt")





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
     
@login_required    
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

def CreatePage(request):
     return render(request, "Emp_app/createpage.html")
    