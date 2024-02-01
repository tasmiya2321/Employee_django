from ast import Module
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
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import authenticate, login
from django.db.models import Q


@login_required
def home(request):
    programs = Program.objects.exclude(date__isnull=True).order_by('pgm_id')[:10]

    for program in programs:
        print(program.date)

    return render(request, "Emp_app/home.html", {'programs': programs})

def admin_module(request):
     return render(request, "Emp_app/admin_module.html")

def forgetpassword(request):
     return render(request, "Emp_app/forgetpassword.html")


    
def index(request):
    return render(request, "Emp_app/index.html")



@login_required
def employee(request):
    if request.method == 'GET':
        return render(request, "Emp_app/employee.html")
    else:
        emp_id = request.POST.get("data","")
        emp_id = emp_id[:-1]
        emp_id = emp_id.strip()
    
        strfilter = 'username__username__iexact' 
        emp_details = EmpDetails.objects.filter(**{strfilter: emp_id})


        my_dict = {}

        if emp_details.exists():
            my_dict = model_to_dict(emp_details.first(), fields=['fullname', 'emp_id', 'address', 'dob', 'phone_number', 'email_id', 'gender', 'center', 'designation', 'date_of_joining', 'education_qualification', 'status', 'resource_type', 'date_of_resigning', 'bank_name', 'name_as_per_bank', 'account_number', 'ifsc', 'branch', 'account_type'])

        return JsonResponse({"info": json.dumps(my_dict)})

@login_required
def saveemployee(request):
     if request.method == 'POST':
        emp_id = request.POST.get('employeeId')
        try:
            emp_details = EmpDetails.objects.get(emp_id=emp_id)

            emp_details.fullname = request.POST.get('fullname')
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
            return HttpResponseRedirect('/employee/')

        except EmpDetails.DoesNotExist:
                messages.error(request, 'Employee not found.')
        except Exception as e:
                messages.error(request, 'Failed to update employee details: {}'.format(e))
     else:
        return render(request, "Emp_app/employee.html")
     

def userlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if user.is_staff:
                return redirect('admin_module')  # Redirect to the admin module for admin users
            else:
                return redirect('home')  # Redirect to the home page for regular users

        else:
            # Authentication failed, handle the error or display a message
            return render(request, 'registration/login.html', {'error_message': 'Incorrect username and/or password.'})

    else:
        # Handle GET requests, if needed
        return render(request, 'registration/login.html')

    
def login(request):
     return render(request, "Registration/login.html")

def reset_password(request):
     return render(request, "Emp_app/reset_password.html")

def email(request):
     return render(request, "Emp_app/email.html")


def subject_email(request):
     return render(request, "Emp_app/subject_email.txt")

# @login_required    
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('home')
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
        
        from_date_str = request.GET.get('from_date')
        to_date_str = request.GET.get('to_date')
        from_date = datetime.strptime(from_date_str, '%Y-%m-%d').date() if from_date_str else None
        to_date = datetime.strptime(to_date_str, '%Y-%m-%d').date() if to_date_str else None
        return render(request, 'Emp_app/Session_main.html', context)



def save_session(request):
    try:
       
        new_session = Program()

        # Assign form values to the Session object
        new_session.date = request.POST.get('date')
        new_session.resource_name = request.POST.get('ResourceName')
        new_session.program = request.POST.get('Program')
        new_session.project = request.POST.get('Project')
        new_session.center_type = request.POST.get('CentreType')
        new_session.activity = request.POST.get('Activity')
        new_session.session_number = request.POST.get('Sessionnumber')
        new_session.trainer_type = request.POST.get('Trainer_Type')
        new_session.duration = request.POST.get('Duration')
        new_session.status = request.POST.get('Status')
        new_session.beneficiaries = request.POST.get('Beneficiaries')
        new_session.category = request.POST.get('Category')
        new_session.comment = request.POST.get('Action')

       
        new_session.save()

       
        return redirect('Session_main')  

    except Exception as e:
       
        print(e)
        return redirect('createpage')