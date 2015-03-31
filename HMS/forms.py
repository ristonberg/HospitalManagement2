from django import forms
from django.forms import ModelForm
from HMS.models import MyUser, Nurse, Doctor, Patient
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib import auth
from django.core.context_processors import csrf
from django.core.mail import send_mail
import hashlib, datetime, random
from django.utils import timezone

class PatientCreationForm(ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'E-mail address'}))

    class Meta:
        model = Patient
        fields = ('email', 'first_name', 'last_name', 'birth_date', 'gender',
                  'marital_Status', 'phone_number')

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            Patient._default_manager.get(email=email)
        except MyUser.DoesNotExist:
            return email
        raise forms.ValidationError('duplicate email')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        Patient = super(PatientCreationForm, self).save(commit=False)
        Patient.email = self.cleaned_data['email']
        Patient.set_password(self.cleaned_data["password1"])
        if commit:
            Patient.save()
               # Send email with activation key
        
        return Patient



class PatientChangeForm(ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Patient
        fields = ('email', 'password', 'first_name', 'birth_date', 'last_name', 'is_active', 'is_admin',
        'is_content_manager')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

class DoctorCreationForm(ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Doctor
        fields = ('email', 'first_name', 'last_name', 'specialty')

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            Doctor._default_manager.get(email=email)
        except MyUser.DoesNotExist:
            return email
        raise forms.ValidationError('duplicate email')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        Doctor = super(DoctorCreationForm, self).save(commit=False)
        Doctor.email = self.cleaned_data['email']
        Doctor.set_password(self.cleaned_data["password1"])
        if commit:
            Doctor.save()
        return Doctor



class DoctorChangeForm(ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Doctor
        fields = ('email', 'password', 'first_name', 'last_name','specialty', 'is_active', 'is_admin',
        'is_content_manager')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

class NurseCreationForm(ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Nurse
        fields = ('email', 'first_name', 'last_name', 'department')

    def clean_email(self):
        email = self.cleaned_data["email"]

        try:
            Nurse._default_manager.get(email=email)
        except MyUser.DoesNotExist:
            return email
        raise forms.ValidationError('duplicate email')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        Nurse = super(NurseCreationForm, self).save(commit=False)
        Nurse.email = self.cleaned_data['email']
        Nurse.set_password(self.cleaned_data["password1"])
        if commit:
            Nurse.save()
        return Nurse


class NurseChangeForm(ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Nurse
        fields = ('email', 'password', 'first_name', 'last_name','department', 'is_active', 'is_admin',
        'is_content_manager')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

class UserCreationForm(ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('email', 'first_name', 'last_name', 'birth_date')

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            MyUser._default_manager.get(email=email)
        except MyUser.DoesNotExist:
            return email
        raise forms.ValidationError('duplicate email')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        MyUser = super(UserCreationForm, self).save(commit=False)
        MyUser.set_password(self.cleaned_data["password1"])
        if commit:
            MyUser.save()
               # Send email with activation key
        return MyUser



class UserChangeForm(ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('email', 'password', 'first_name', 'birth_date', 'last_name', 'is_active', 'is_admin',
        'is_content_manager')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
  
