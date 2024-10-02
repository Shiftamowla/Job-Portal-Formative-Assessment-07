from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from myapp.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


def base(req):
    return render(req, 'base.html')

def changepassword(req):
    current_user=req.user
    if req.method == 'POST':
        currentpassword = req.POST.get("currentpassword")
        newpassword = req.POST.get("newpassword")
        confirmpassword = req.POST.get("confirmpassword")

        if check_password(currentpassword,req.user.password):
            if newpassword==confirmpassword:
                current_user.set_password(newpassword)
                current_user.save()
                update_session_auth_hash(req,current_user)




    return render(req, 'changepassword.html')


def jobfeed(req):
    data=JobModel.objects.all()

    context = {
        'data': data
    }
    return render(req,'jobfeed.html',context)

def deletejob(req,id):
    job=JobModel.objects.filter(id=id)
    job.delete()
    return redirect('profilepage')

def deletexp(req,id):
    job=Experience_Model.objects.filter(id=id)
    job.delete()
    return redirect('profilepage')

def deleteedu(req,id):
    job=Education_Model.objects.filter(id=id)
    job.delete()
    return redirect('profilepage')

def editjob(req,id):
    current_user=req.user
    job=JobModel.objects.filter(id=id)

    if current_user.user_type == "recruiter":
        if req.method == 'POST':
            job=JobModel()
            id=req.POST.get('id')
            Qualifications=req.POST.get('Qualifications')
            job_title=req.POST.get('job_title')
            company_type=req.POST.get('company_type')
            company_logo=req.FILES.get('company_logo')
            location=req.POST.get('location')
            company_name=req.POST.get('company_name')
            description=req.POST.get('description')
            salary=req.POST.get('salary')
            application_deadline=req.POST.get('application_deadline')
            posted_on=req.POST.get('posted_on')
            company_logo_old=req.POST.get('company_logo_old')


            job=JobModel(
                id=id,
                user=current_user,
                job_title=job_title,
                Qualifications=Qualifications,
                company_type=company_type,
                location=location,
                company_name=company_name,
                description=description,
                salary=salary,
                application_deadline=application_deadline,
                posted_on=posted_on
            )
            if company_logo:
                 job.company_logo=company_logo
                 job.save()
            return redirect('createdjob')

    return render (req,'editjob.html',{'job':job})



def appliedjob(req):
    current_user=req.user
    if current_user.user_type == "recruiter":
        if req.method == 'POST':
            job=JobModel()
            job.user=current_user
            job.job_title=req.POST.get('job_title')
            job.company_type=req.POST.get('company_type')
            job.company_logo=req.FILES.get('company_logo')
            job.location=req.POST.get('location')
            job.company_name=req.POST.get('company_name')
            job.description=req.POST.get('description')
            job.salary=req.POST.get('salary')
            job.application_deadline=req.POST.get('application_deadline')
            job.posted_on=req.POST.get('posted_on')
            job.save()
            
            return redirect('jobfeed')

    return render(req, 'appliedjob.html')

def editedu(req,id):
    alledu=Education_Model.objects.get(id=id)
    edu=intermediate_Educationmodel.objects.all()
    
    current_user = req.user
    
    if req.method=='POST':
            edu_id = req.POST.get("edu_id")
            
            MyObj = get_object_or_404(intermediate_Educationmodel, id=edu_id)
            
            skill = Education_Model(
                id=id,
                user=current_user,
                type=MyObj.type,  
            )
            skill.save()
            return redirect("profilepage")
    
    context={
        "alledu":alledu,
        "edu":edu,
    }

    return render(req,'editedu.html',context)



def editexp(req,id):
    alledu=Experience_Model.objects.get(id=id)
    edu=intermediate_Experiencemodel.objects.all()
    
    current_user = req.user
    
    if req.method=='POST':
            exp_id = req.POST.get("exp_id")
            
            MyObj = get_object_or_404(intermediate_Experiencemodel, id=exp_id)
            
            skill = Experience_Model(
                id=id,
                user=current_user,
                title=MyObj.title,  
            )
            skill.save()
            return redirect("profilepage")
    
    context={
        "alledu":alledu,
        "edu":edu,
    }

    return render(req,'editexp.html',context)

def addEducation(req):
    current_user=req.user

    edu=intermediate_Educationmodel.objects.all()


    if req.method=='POST':
        edu_id=req.POST.get('edu_id')

        eduobj=get_object_or_404(intermediate_Educationmodel,id=edu_id)
        if Education_Model.objects.filter(user=current_user,type=eduobj.type).exists():
            return HttpResponse('Education already exist')
        else:
            add=Education_Model(
            user=current_user,
            type=eduobj

        )
        add.save()
        return redirect ('profilepage')
    return render(req,'addEducation.html',{'edu':edu})

def addExp(req):
    current_user=req.user

    exp=intermediate_Experiencemodel.objects.all()


    if req.method=='POST':
        exp_id=req.POST.get('exp_id')

        eduobj=get_object_or_404(intermediate_Experiencemodel,id=exp_id)
        if Experience_Model.objects.filter(user=current_user,title=eduobj.title).exists():
            return HttpResponse('Education already exist')
        else:
            add=Experience_Model(
            user=current_user,
            title=eduobj

        )
        add.save()
        return redirect ('profilepage')
    return render(req,'addExperience.html',{'exp':exp})




@login_required
def profilepage(req):
    current_user=req.user

    Job=JobModel.objects.filter(user=current_user)
    edu=Education_Model.objects.filter(user=current_user)
    exp=Experience_Model.objects.filter(user=current_user)
    resu=resume.objects.filter(user=current_user)
    text={
        'Job':Job,
        'edu':edu,
        'exp':exp,
        'resu':resu,
    }
 
    return render(req,'profilepage.html',text)

def updateprofile(req,id):
    data=resume.objects.filter(id=id)
    if req.method=='POST':
        id=req.POST.get('id')
        contact=req.POST.get('contact')
        designation=req.POST.get('designation')
        img=req.FILES.get('img')
        oldimg=req.POST.get('oldimg')

        user_object=Custom_user.objects.get(id=id)

        add=resume(
            id=id,
            user=user_object,
            contact=contact,
            designation=designation,
        )
        if img:
          add.img=img
          add.save()
        else:
         add.img=oldimg
         add.save()
        return redirect ('profilepage')
    context={
        'data':data
    }
    return render (req,'updateprofile.html',context)

def mainprofile(req,id):
    current_user=req.user

    Job=JobModel.objects.filter(id=id)
    text={
        'Job':Job,
    }
 
    return render(req,'mainprofile.html',text)

def createdjob(req):
    current_user=req.user

    Job=JobModel.objects.filter(user=current_user)
    text={
        'Job':Job,
    }
 
    return render(req,'createdjob.html',text)

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not username or not password:
            messages.warning(request, "Both username and password are required")
            return render(request, "loginPage.html")

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login Successfully")
            return redirect("jobfeed")
        else:
            messages.warning(request, "Invalid username or password")

    return render(request, "loginPage.html")

def registerpage(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        user_type = request.POST.get("usertype")
        city = request.POST.get("city")
        gender = request.POST.get("gender")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        profile_picture = request.FILES.get("profile_picture")

        # Check for required fields
        if not all([username, email, user_type, city, gender, password, confirm_password]):
            messages.warning(request, "All fields are required")
            return render(request, "signupPage.html")

        # Validate email
        try:
            validate_email(email)
        except ValidationError:
            messages.warning(request, "Invalid email format")
            return render(request, "signupPage.html")

        # Check password confirmation
        if password != confirm_password:
            messages.warning(request, "Passwords do not match")
            return render(request, "signupPage.html")

        # Password validation
        if len(password) < 4:
            messages.warning(request, "Password must be at least 8 characters long")
            return render(request, "signupPage.html")

        if not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password):
            messages.warning(request, "Password must contain both letters and numbers")
            return render(request, "signupPage.html")

        # Create user
        try:
            user = Custom_user.objects.create_user(
                username=username,
                email=email,
                user_type=user_type,
                city=city,
                gender=gender,
                password=password,
                profile_picture=profile_picture  # Assuming your model has this field
            )
            messages.success(request, "Account created successfully! Please log in.")
            return redirect("loginpage")
        except IntegrityError:
            messages.warning(request, "Username or email already exists")
            return render(request, "signupPage.html")

    return render(request, "signupPage.html")

def logoutpage(req):
    logout(req)
    return redirect('loginpage')