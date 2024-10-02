from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class Custom_user(AbstractUser):
    USER=[
        ('recruiter','Recruiter'),
        ('jobseeker','Jobseeker')
    ]
    Gender=[
        ('male','Male'),
        ('female','Female'),
        ('other','Other')
    ]
    user_type=models.CharField(choices=USER,max_length=100,null=True)
    city=models.CharField(max_length=25, null=True)
    gender=models.CharField(choices=Gender,max_length=100,null=True)
    profile_picture=models.ImageField(upload_to='company_logos/', null=True)

    def  __str__(self):
        return f"{self.username}-{self.first_name}-{self.last_name}-{self.user_type}"
    
class JobModel(models.Model):
    JOB_TYPE_CHOICES = [
        ('fulltime', 'Full-time'),
        ('parttime', 'Part-time'),
    ]

    user = models.ForeignKey(Custom_user, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=255, null=True)
    company_type = models.CharField(max_length=10, choices=JOB_TYPE_CHOICES, null=True)
    company_logo = models.ImageField(upload_to='company_logos/', null=True)
    company_name = models.CharField(max_length=255, null=True)
    location = models.CharField(max_length=255, null=True)
    Qualifications = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    salary = models.CharField(max_length=255, null=True)
    posted_on = models.DateField(default=timezone.now, null=True)
    application_deadline = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.job_title} at {self.job_title} ({self.user.first_name})"
    
class resume(models.Model):
    user = models.ForeignKey(Custom_user, on_delete=models.CASCADE)
    contact=models.CharField(max_length=100, null=True)
    designation=models.CharField(max_length=100, null=True)
    img=models.ImageField(upload_to='Media/img',null=True)
    def __str__(self):
        return f"{self.user.first_name}-{self.designation}"
    

class Education_Model(models.Model):
    user=models.ForeignKey(Custom_user,null=True,on_delete=models.CASCADE)
    type=models.CharField(max_length=100, null=True)
    def  __str__(self):
        return f"{self.user.first_name}-{self.type}"
    

class Experience_Model(models.Model):
    user=models.ForeignKey(Custom_user,null=True,on_delete=models.CASCADE)
    title=models.CharField(max_length=100, null=True)

    def  __str__(self):
        return f"{self.user.first_name}-{self.title}"
    
class intermediate_Educationmodel(models.Model):
    type=models.CharField(max_length=100,null=True)
    def  __str__(self):
        return f"{self.type}"
    
class intermediate_Experiencemodel(models.Model):
    title=models.CharField(max_length=100,null=True)
    def  __str__(self):
        return f"{self.title}"