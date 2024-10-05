from django.contrib import admin
from django.urls import path
from myproject.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', base, name='base'),
    path('profilepage/', profilepage, name='profilepage'),
    path('createdjob/', createdjob, name='createdjob'),
    path('searchJob/', searchJob, name='searchJob'),
    path('mainprofile/<int:id>', mainprofile, name='mainprofile'),
    path('deletejob/<int:id>', deletejob, name='deletejob'),
    path('deleteedu/<int:id>', deleteedu, name='deleteedu'),
    path('deletexp/<int:id>', deletexp, name='deletexp'),
    path('addEducation/', addEducation, name='addEducation'),
    path('editedu/<int:id>', editedu, name='editedu'),
    path('editexp/<int:id>', editexp, name='editexp'),
    path('addExp/', addExp, name='addExp'),
    path('updateprofile/<int:id>', updateprofile, name='updateprofile'),
    path('changepassword/', changepassword, name='changepassword'),
    path('editjob/<int:id>', editjob, name='editjob'),
    path('jobfeed/', jobfeed, name='jobfeed'),
    path('appliedjob/', appliedjob, name='appliedjob'),
    path('', loginpage, name='loginpage'),
    path('registerpage/', registerpage, name='registerpage'),
    path('logoutpage/', logoutpage, name='logoutpage'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
