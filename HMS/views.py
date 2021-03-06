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
import hashlib, random, datetime
from datetime import timedelta
from swingtime import models as swingtime
from django.utils import timezone
from django.views import generic
from django.shortcuts import render_to_response, get_object_or_404

def login(request):
    return render(request, 'registration/login.html')

def home(request):
    return render(request, 'HMS/home.html')

def registration(request):
    return render(request, 'HMS/Registration/registration.html')

def patient_home(request):
    doctor_list = Doctor.objects.order_by('-last_name')[:25]
    context = {'doctor_list': doctor_list}
    return render(request, 'HMS/PatientHome/patient_home.html', context)

def doctor_home(request):
    patient_list = Patient.objects.order_by('-last_name')[:25]
    context = {'patient_list': patient_list}
    return render(request, 'HMS/DoctorHome/doctor_home.html', context)

def cal_home(request):
    return render(request, 'HMS/swingtime/cal_home.html')
    
def nurse_home(request):
    #print(request.user.get_Type)
    return render(request, 'HMS/NurseHome/nurse_home.html')


def admin_home(request):
    return HttpResponse("Administrator Homepage")

def event_type(request, abbr):
    event_type = get_object_or_404(swingtime.EventType, abbr=abbr)
    now = datetime.now()
    occurrences = swingtime.Occurrence.objects.filter(
        event__event_type=event_type,
        start_time__gte=now,
        start_time__lte=now+timedelta(days=+30)
    )
    return render_to_response(
        'HMS/upcoming_by_event_type.html', 
        dict(occurrences=occurrences, event_type=event_type),
        context_instance=RequestContext(request)
    )
    
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
            user_profile = get_object_or_404(Nurse, email=email)
            user = user_profile
            random_string = str(random.random()).encode('utf8')
            salt = hashlib.sha1(random_string).hexdigest()[:5]
            salted = (salt + email).encode('utf8')
            activation_key = hashlib.sha1(salted).hexdigest()
            key_expires = datetime.datetime.today() + datetime.timedelta(2)
            user.activation_key=activation_key
            user.key_expires=key_expires
            user.save()
            
            email_subject = 'Account confirmation'
            email_body = "Hey %s, thanks for signing up. To activate your account, click this link within \
            48hours http://127.0.0.1:8000/HMS/account/confirm/nurse/%s" % (email, activation_key)

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
            user_profile = get_object_or_404(Doctor, email=email)
            user = user_profile
            random_string = str(random.random()).encode('utf8')
            salt = hashlib.sha1(random_string).hexdigest()[:5]
            salted = (salt + email).encode('utf8')
            activation_key = hashlib.sha1(salted).hexdigest()
            key_expires = datetime.datetime.today() + datetime.timedelta(2)
            user.activation_key=activation_key
            user.key_expires=key_expires
            user.save()
            
            email_subject = 'Account confirmation'
            email_body = "Hey %s, thanks for signing up. To activate your account, click this link within \
            48hours http://127.0.0.1:8000/HMS/account/confirm/doctor/%s" % (email, activation_key)

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
            user_profile = get_object_or_404(Patient, email=email)
            user = user_profile
            random_string = str(random.random()).encode('utf8')
            salt = hashlib.sha1(random_string).hexdigest()[:5]
            salted = (salt + email).encode('utf8')
            activation_key = hashlib.sha1(salted).hexdigest()
            key_expires = datetime.datetime.today() + datetime.timedelta(2)
            user.activation_key=activation_key
            user.key_expires=key_expires
            user.save()
            

            email_subject = 'Account confirmation'
            #email_body = "Hey %s, thanks for signing up. To activate your account, click this link within \
            #48hours http://127.0.0.1:8000/accounts/confirm/%s" % (email, activation_key)
            email_body = "Hey %s, thanks for signing up. To activate your account, click this link within \
            48hours http://127.0.0.1:8000/HMS/account/confirm/patient/%s" % (email, activation_key)

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
    # check if there is UserProfile which matches the activation key (if not then display 404)
    user_profile = get_object_or_404(Doctor, activation_key=activation_key)

    #check if the activation key has expired, if it hase then render confirm_expired.html
    if user_profile.key_expires < timezone.now():
        return render_to_response('account/confirm_expired.html')
    #if the key hasn't expired save user and set him as active and render some template to confirm activation
    user = user_profile
    user.is_active = True
    user.save()
    return render(request, 'HMS/account/confirm.html')

def register_confirm_doctor(request, activation_key):
    #check if user is already logged in and if he is redirect him to some other url, e.g. home
    user_profile = get_object_or_404(Doctor, activation_key=activation_key)

    #check if the activation key has expired, if it hase then render confirm_expired.html
    if user_profile.key_expires < timezone.now():
        return render_to_response('account/confirm_expired.html')
    #if the key hasn't expired save user and set him as active and render some template to confirm activation
    user = user_profile
    user.is_active = True
    user.save()
    return render(request, 'HMS/account/confirm.html')

def register_confirm_nurse(request, activation_key):
    #check if user is already logged in and if he is redirect him to some other url, e.g. home
    user_profile = get_object_or_404(Nurse, activation_key=activation_key)

    #check if the activation key has expired, if it hase then render confirm_expired.html
    if user_profile.key_expires < timezone.now():
        return render_to_response('account/confirm_expired.html')
    #if the key hasn't expired save user and set him as active and render some template to confirm activation
    user = user_profile
    user.is_active = True
    user.save()
    return render(request, 'HMS/account/confirm.html')

def register_confirm_patient(request, activation_key):
    #check if user is already logged in and if he is redirect him to some other url, e.g. home
    user_profile = get_object_or_404(Patient, activation_key=activation_key)

    #check if the activation key has expired, if it hase then render confirm_expired.html
    if user_profile.key_expires < timezone.now():
        return render_to_response('account/confirm_expired.html')
    #if the key hasn't expired save user and set him as active and render some template to confirm activation
    user = user_profile
    user.is_active = True
    user.save()
    return render(request, 'HMS/account/confirm.html')
