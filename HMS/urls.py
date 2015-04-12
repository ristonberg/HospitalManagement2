from django.conf.urls import patterns, url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from HMS import views
from django.contrib import admin
admin.autodiscover()

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
    url(r'calendarHome', views.cal_home, name='cal_home'),
    url(r'^swingtime/events/type/([^/]+)/$', views.event_type, name='Hospital-event'),
    (r'^swingtime/', include('swingtime.urls')),
    url(r'^account/confirm/(?P<activation_key>\w+)/', ('HMS.views.register_confirm')),
    (r'^accounts/', include('allauth.urls')),
)

urlpatterns += staticfiles_urlpatterns()
