from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from HMS import views

urlpatterns = patterns('',
    url(r'login', views.login, name='login'),
    url(r'registration', views.registration, name='registration'),
    url(r'patient_home', views.patient_home, name='patient_home'),
    url(r'doctor_home', views.doctor_home, name='doctor_home'),
    url(r'nurse_home', views.nurse_home, name='nurse_home'),
    url(r'admin_home', views.admin_home, name='admin_home'),
    url(r'addNurse', views.add_Nurse, name='add_Nurse'),
    url(r'addDoctor', views.add_Doctor, name='add_Doctor'),
    url(r'addPatient', views.add_Patient, name='add_Patient'),
    url(r'home', views.home, name = 'home'),
    url(r'^patients/(?P<patient_id>[0-9]+)/$', views.patient_detail, name='patdetail'),
    url(r'^doctors/(?P<doctor_id>[0-9]+)/$', views.doctor_detail, name='docdetail'),
    url(r'changePatient', views.change_Patient, name='change_Patient'),
    #Password change
    url(r'^accounts/password_change/$', 
        'django.contrib.auth.views.password_change', 
        {'post_change_redirect' : 'HMS/passwordChanged'}, 
        name="password_change"),
    url(r'passwordChanged', views.passwordChanged, name = 'pChanged'),
   # url(r'^accounts/edit/$', 'django.contrib.auth.views.change_form', name = "edit"), 
)

urlpatterns += staticfiles_urlpatterns()
