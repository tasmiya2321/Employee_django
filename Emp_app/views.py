from ast import Module
from distutils.sysconfig import project_base
from django.core import paginator
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
import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404



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
def admin_module(request):
    employees = EmpDetails.objects.all()
    return render(request, "Emp_app/admin_module.html", {'employees': employees})

@login_required
def employee(request, emp_id=None):
    if request.user.is_staff:
        if not emp_id:
            return redirect('employee')  
        emp_details = get_object_or_404(EmpDetails, emp_id__iexact=emp_id)
    else:
        emp_details = get_object_or_404(EmpDetails, username=request.user.username)
    
    return render(request, 'Emp_app/employee.html', {'employee': emp_details})
  

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
            emp_details.center = request.POST.get('center')
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
            

            emp_details.save()

            messages.success(request, 'Employee details updated successfully!')
           
            return redirect('employee', emp_id=emp_id)  
        except EmpDetails.DoesNotExist:
            messages.error(request, 'Employee not found.')
            return redirect('employee') 
        except Exception as e:
            messages.error(request, f'Failed to update employee details: {e}')
            return redirect('employee', emp_id=emp_id) 
    else:
        
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

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if user.is_staff:
                return redirect('admin_module') 
            else:
                return redirect('home')  

        else:
            return render(request, 'registration/login.html', {'error_message': 'Incorrect username and/or password.'})

    else:
        return render(request, 'registration/login.html')


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
    # Start with all programs, ordered by 'date' in descending order
    programs = Program.objects.all().order_by('-date')  # Adjust the query here
    
    resources=EmpDetails.objects.values('resource_type').distinct()
    project_names = Xref.objects.values('project_name').distinct()
    program_names = Xref.objects.values("program_name").distinct()
    centers = Program.objects.values('center_type').distinct()
    trainers = Program.objects.values('trainer_type').distinct()

    if request.method == 'POST':
        data = json.loads(request.body)
        program_filter = data.get('program')
        project_filter = data.get('project')
        center_filter = data.get('center')
        trainer_filter = data.get('trainer')

        if program_filter:
            programs = programs.filter(pgm_id__program_name=program_filter)
        if project_filter:
            programs = programs.filter(xref__project_name=project_filter)
        if center_filter:
            programs = programs.filter(center_type=center_filter)
        if trainer_filter:
            programs = programs.filter(trainer_type=trainer_filter)

        # Ensure the filtered queryset is also ordered
        programs = programs.order_by('-date')

        programs_data = list(programs.values())
        return JsonResponse({'programs': programs_data})
    else:
        from_date_str = request.GET.get('from_date')
        to_date_str = request.GET.get('to_date')
        if from_date_str and to_date_str:
            from_date = datetime.strptime(from_date_str, '%Y-%m-%d').date()
            to_date = datetime.strptime(to_date_str, '%Y-%m-%d').date()
            programs = programs.filter(date__range=(from_date, to_date))

        paginator = Paginator(programs, 10)  # Apply pagination to the ordered queryset
        page_number = request.GET.get('page')
        try:
            programs_page = paginator.page(page_number)
        except PageNotAnInteger:
            programs_page = paginator.page(1)
        except EmptyPage:
            programs_page = paginator.page(paginator.num_pages)

        context = {
            'resources':resources,
            'programs': programs_page,
            'program_names': program_names,
            'project_names': project_names,
            'centers': centers,
            'trainers': trainers,
            'total_count': paginator.count
        }

        return render(request, 'Emp_app/Session_main.html', context)



# def save_session(request):
#     try:
       
#         new_session = Program()

#         # Assign form values to the Session object
#         new_session.date = request.POST.get('date')
#         new_session.resource_name = request.POST.get('ResourceName')
#         new_session.program = request.POST.get('Program')
#         new_session.project = request.POST.get('Project')
#         new_session.center_type = request.POST.get('CentreType')
#         new_session.activity = request.POST.get('Activity')
#         new_session.session_number = request.POST.get('Sessionnumber')
#         new_session.trainer_type = request.POST.get('Trainer_Type')
#         new_session.duration = request.POST.get('Duration')
#         new_session.status = request.POST.get('Status')
#         new_session.beneficiaries = request.POST.get('Beneficiaries')
#         new_session.category = request.POST.get('Category')
#         new_session.comment = request.POST.get('Action')

       
#         new_session.save()

       
#         return redirect('Session_main')  

#     except Exception as e:
       
#         print(e)
#         return redirect('createpage')





    








def save_session(request):
    if request.method == "POST":
        
        employee_name = request.POST.get("username")
        resource_type = request.POST.get("resourceType")
        date = request.POST.get("date") 
        program_name = request.POST.get("Program")
        project_name = request.POST.get("Project")
        activity = request.POST.get("Activity")
        center_type = request.POST.get("CentreType")
        session_number = request.POST.get("Session_number")
        trainer_type = request.POST.get("Trainer_Type")
        duration = request.POST.get("Duration")
        status = request.POST.get("Status")
        beneficiaries = request.POST.get("Beneficiaries")
        category = request.POST.get("Category")
        comment = request.POST.get("Comment")
        sponsor = request.POST.get("Sponsor")

       
        new_emp_details = EmpDetails(fullname=employee_name, resource_type=resource_type)
        new_emp_details.save()

        # Create Xref instance
        new_xref = Xref(
            date=date, 
            program_name=program_name, 
            project_name=project_name
        )
        new_xref.save()

       
        new_program = Program(
            emp=new_emp_details,
            xref=new_xref, 
            date=date,  
            activity=activity,
            center_type=center_type,
            trainer_type=trainer_type,
            sponsor=sponsor,
            beneficiaries=beneficiaries,
            category=category,
            duration=duration,
            status=status,
            comments=comment,
        )
        new_program.save()

        messages.success(request, "Session saved successfully.")
        return redirect('Session_main') 
    return render(request, "Emp_app/createpage.html") 








