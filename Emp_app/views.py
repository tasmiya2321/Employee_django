from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .models import Program 
from .models import EmpDetails 
from django.contrib import messages
import json
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect


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
    try:
        Value = request.POST.get('fullname')
        emp_details = EmpDetails.objects.get(fullname=Value)
        emp_details.address = request.POST.get('address')
        emp_details.dob = request.POST.get('dob')
        emp_details.phone_number = request.POST.get('phonenumber') 
        emp_details.email_id = request.POST.get('emailId') 
        emp_details.gender = request.POST.get('gender')
        emp_details.employeeId = request.POST.get('employeeId') 
        emp_details.centre = request.POST.get('centre')
        emp_details.designation = request.POST.get('designation')
        emp_details.date_of_joining = request.POST.get('dateofJoining')  
        emp_details.education_qualification = request.POST.get('educationQualification') 
        emp_details.status = request.POST.get('status')
        emp_details.date_of_resigning = request.POST.get('dateofResigning') 
        emp_details.resource_type = request.POST.get('resourceType') 
        emp_details.bank_name = request.POST.get('bankName') 
        emp_details.name_as_per_bank = request.POST.get('nameAsPerBank')  
        emp_details.account_number = request.POST.get('accountNumber')  
        emp_details.ifsc = request.POST.get('ifscCode') 
        emp_details.branch = request.POST.get('branchName') 
        emp_details.account_type = request.POST.get('accountType') 

        # Save the changes to the database
        emp_details.save()
        messages.success(request, 'Employee details updated successfully!')

    except EmpDetails.DoesNotExist:
        messages.error(request, 'Employee not found.')
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
    
def Session_main(request):
    programs = Program.objects.all()  # Fetch all program records from the database
    context = {'programs': programs}
    return render(request, 'Emp_app/Session_main.html', context)




def filter_programs(request):
   
    filter_value = request.GET.get('filter_value', None)

   
    if filter_value:
       
        filtered_programs = Program.objects.filter(xref__program_name=filter_value)
    else:
        filtered_programs = Program.objects.all()

  
    data = list(filtered_programs.values('pgm_id', 'emp__name', 'xref__program_name', 'date', 'activity', ...)) 

    return JsonResponse(data, safe=False)
