from distutils.sysconfig import project_base
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .models import Program ,Xref
from .models import EmpDetails 
from django.contrib import messages
import json
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
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
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from .models import Program  # Make sure to import your actual Program model
from django.core.serializers import serialize
from django.contrib.auth.decorators import login_required


@login_required
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
     
# @login_required    
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('Login')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request,'change_password.html',{
        'form': form
    })

def login_base(request):
    return render(request, "login_base.html")


def createpage(request):
    return render(request, "createpage.html")

    
def Session_main(request):
    programs = Program.objects.all()  # Fetch all program records from the database
    project_names = Xref.objects.values('project_name').distinct()
    program_names = Xref.objects.values("program_name").distinct()
    centers = Program.objects.values('center_type').distinct()  # Adjusted to 'center_type'
    trainers = Program.objects.values('trainer_type').distinct()
    context = {'programs': programs, 'program_names':program_names,'project_names': project_names,'centers': centers,
        'trainers': trainers}
    if request.method == 'POST':
        # Get the filter values from the request
        data = json.loads(request.body)
        program_filter = data.get('program')
        project_filter = data.get('project')
        center_filter = data.get('center')
        trainer_filter = data.get('trainer')
        
        # Filter your programs based on the provided values
        programs = Program.objects.all()
        if program_filter:
            programs = programs.filter(pgm_id__program_name=program_filter)
        if project_filter:
            programs = programs.filter(xref__project_name=project_filter)
        if center_filter:
            programs = programs.filter(center_type=center_filter)
        if trainer_filter:
            programs = programs.filter(trainer_type=trainer_filter)

        # Serialize your programs data into a format that can be sent as JSON
        programs_data = list(programs.values())  # Adjust as needed to serialize your data

        return JsonResponse({'programs': programs_data})  # Send the filtered data back to the front end

    else:
         # Your existing code for handling GET requests
        # ...
      from_date_str = request.GET.get('from_date')
      to_date_str = request.GET.get('to_date')
      from_date = datetime.strptime(from_date_str, '%Y-%m-%d').date() if from_date_str else None
      to_date = datetime.strptime(to_date_str, '%Y-%m-%d').date() if to_date_str else None
    
      return render(request, 'Emp_app/Session_main.html', context)






 
