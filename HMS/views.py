from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from HMS.forms import (NurseCreationForm, NurseChangeForm, UserCreationForm,
                       UserChangeForm, DoctorCreationForm, DoctorChangeForm,
                       PatientChangeForm, PatientCreationForm)
from django.core.urlresolvers import reverse
from HMS.models import MyUser, Nurse, Doctor, Patient
from django.contrib import auth
from django.core.context_processors import csrf
from django.core.mail import send_mail
import hashlib, datetime, random
from django.utils import timezone

def login(request):
    return render(request, 'registration/login.html')

def registration(request):
    return render(request, 'HMS/Registration/registration.html')

def patient_home(request):
    #print(request.user.get_Type)
    return render(request, 'HMS/PatientHome/patient_home.html')

def doctor_home(request):
    #print(request.user.get_Type)
    return HttpResponse("Doctor Homepage")

def nurse_home(request):
    #print(request.user.get_Type)
    return render(request, 'HMS/NurseHome/nurse_home.html')


def admin_home(request):
    return HttpResponse("Administrator Homepage")

#HMS/addNurse/
def add_Nurse(request):
    form_class = NurseCreationForm
    template_name = 'HMS/addNurse.html'

    #permitted = request.user.is_content_manager or request.user.is_admin

    #if not permitted:
        #raise PermissionDenied
    args = {}
    args.update(csrf(request))
    if request.method == 'POST':
        form = form_class(request.POST)
        args['form'] = form
        form.instance.content_manager = request.user
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            random_string = str(random.random()).encode('utf8')
            salt = hashlib.sha1(random_string).hexdigest()[:5]
            salted = (salt + email).encode('utf8')
            activation_key = hashlib.sha1(salted).hexdigest()
            key_expires = datetime.datetime.today() + datetime.timedelta(2)
            email_subject = 'Account confirmation'
            email_body = "Hey %s, thanks for signing up. To activate your account, click this link within \
            48hours http://127.0.0.1:8000/accounts/confirm/%s" % (email, activation_key)

            send_mail(email_subject, email_body, 'ristonjbergen@gmail.com',
                [email], fail_silently=False)

            #return HttpResponseRedirect('/accounts/register_success')
            return HttpResponseRedirect('registration/login.html')
        else:
            args['form'] = NurseCreationForm()
            
            return HttpResponseRedirect('HMS/nurse_homepage')
        #else:
            return render(request, template_name, {'form': form})
    else:
        form = form_class()
        return render(request, template_name, {'form': form})

#HMS/addDoctor/
def add_Doctor(request):
    form_class = DoctorCreationForm
    template_name = 'HMS/addDoctor.html'

    #permitted = request.user.is_content_manager or request.user.is_admin

    #if not permitted:
        #raise PermissionDenied

    args = {}
    args.update(csrf(request))
    if request.method == 'POST':
        form = form_class(request.POST)
        args['form'] = form
        form.instance.content_manager = request.user
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            random_string = str(random.random()).encode('utf8')
            salt = hashlib.sha1(random_string).hexdigest()[:5]
            salted = (salt + email).encode('utf8')
            activation_key = hashlib.sha1(salted).hexdigest()
            key_expires = datetime.datetime.today() + datetime.timedelta(2)
            
            email_subject = 'Account confirmation'
            email_body = "Hey %s, thanks for signing up. To activate your account, click this link within \
            48hours http://127.0.0.1:8000/accounts/confirm/%s" % (email, activation_key)

            send_mail(email_subject, email_body, 'ristonjbergen@gmail.com',
                [email], fail_silently=False)

            #return HttpResponseRedirect('/accounts/register_success')
            return HttpResponseRedirect('HMS/Login/login.html') #######CHANGE URL######
        else:
            args['form'] = DoctorCreationForm()
            return HttpResponseRedirect('HMS/doctor_homepage')
       # else:
            return render(request, template_name, {'form': form})
    else:
        form = form_class()
        return render(request, template_name, {'form': form})

#HMS/addPatient/
def add_Patient(request):
    form_class = PatientCreationForm
    template_name = 'HMS/addPatient.html'

    #permitted = request.user.is_content_manager or request.user.is_admin

    #if not permitted:
        #raise PermissionDenied

    args = {}
    args.update(csrf(request))
    if request.method == 'POST':
        form = form_class(request.POST)
        args['form'] = form
        form.instance.content_manager = request.user
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            random_string = str(random.random()).encode('utf8')
            salt = hashlib.sha1(random_string).hexdigest()[:5]
            salted = (salt + email).encode('utf8')
            activation_key = hashlib.sha1(salted).hexdigest()
            key_expires = datetime.datetime.today() + datetime.timedelta(2)
            email_subject = 'Account confirmation'
            #email_body = "Hey %s, thanks for signing up. To activate your account, click this link within \
            #48hours http://127.0.0.1:8000/accounts/confirm/%s" % (email, activation_key)
            email_body = "Hey %s, thanks for signing up. To activate your account, click this link within \
            48hours http://127.0.0.1:8000/accounts/confirm/%s" % (email, activation_key)

            send_mail(email_subject, email_body, 'ristonjbergen@gmail.com',
                [email], fail_silently=False)

            #return HttpResponseRedirect('/accounts/register_success')
            return HttpResponseRedirect('HMS/Login/login.html')
        else:
            args['form'] = PatientCreationForm()
            return HttpResponseRedirect('HMS/patient_homepage')
       # else:
            return render(request, template_name, {'form': form})
    else:
        form = form_class()
        return render(request, template_name, {'form': form})


def register_confirm(request, activation_key):
    #check if user is already logged in and if he is redirect him to some other url, e.g. home
    if request.MyUser.is_authenticated():
        HttpResponseRedirect('HMS/doctor_homepage')

    # check if there is UserProfile which matches the activation key (if not then display 404)
    user_profile = get_object_or_404(MyUser, activation_key=activation_key)

    #check if the activation key has expired, if it hase then render confirm_expired.html
#    if user_profile.key_expires < timezone.now():
     #   return render_to_response('user_profile/confirm_expired.html')
    #if the key hasn't expired save user and set him as active and render some template to confirm activation
    user = user_profile.MyUser
    MyUser.is_active = True
    MyUser.save()
    return render_to_response('user_profile/confirm.html')

def register_confirm_doctor(request, activation_key):
    #check if user is already logged in and if he is redirect him to some other url, e.g. home
    if request.Doctor.is_authenticated():
        HttpResponseRedirect('HMS/doctor_homepage')

    # check if there is UserProfile which matches the activation key (if not then display 404)
    user_profile = get_object_or_404(Doctor, activation_key=activation_key)

    #check if the activation key has expired, if it hase then render confirm_expired.html
#    if user_profile.key_expires < timezone.now():
     #   return render_to_response('user_profile/confirm_expired.html')
    #if the key hasn't expired save user and set him as active and render some template to confirm activation
    user = user_profile.Doctor
    Doctor.is_active = True
    Doctor.save()
    return render_to_response('user_profile/confirm.html')

def register_confirm_nurse(request, activation_key):
    #check if user is already logged in and if he is redirect him to some other url, e.g. home
    if request.Nurse.is_authenticated():
        HttpResponseRedirect('HMS/nurse_homepage')

    # check if there is UserProfile which matches the activation key (if not then display 404)
    user_profile = get_object_or_404(Nurse, activation_key=activation_key)

    #check if the activation key has expired, if it hase then render confirm_expired.html
#    if user_profile.key_expires < timezone.now():
     #   return render_to_response('user_profile/confirm_expired.html')
    #if the key hasn't expired save user and set him as active and render some template to confirm activation
    user = user_profile.Nurse
    Nurse.is_active = True
    Nurse.save()
    return render_to_response('user_profile/confirm.html')

def register_confirm_patient(request, activation_key):
    #check if user is already logged in and if he is redirect him to some other url, e.g. home
    if request.Patient.is_authenticated():
        HttpResponseRedirect('HMS/doctor_homepage')

    # check if there is UserProfile which matches the activation key (if not then display 404)
    user_profile = get_object_or_404(Patient, activation_key=activation_key)

    #check if the activation key has expired, if it hase then render confirm_expired.html
#    if user_profile.key_expires < timezone.now():
     #   return render_to_response('user_profile/confirm_expired.html')
    #if the key hasn't expired save user and set him as active and render some template to confirm activation
    user = user_profile.Patient
    Patient.is_active = True
    Patient.save()
    return render_to_response('user_profile/confirm.html')
