from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from HMS.models import MyUser, Nurse, Doctor, Patient
from HMS.forms import (NurseCreationForm, NurseChangeForm, UserCreationForm, UserChangeForm,
                       DoctorCreationForm, DoctorChangeForm, PatientChangeForm, PatientCreationForm)

class MyUserAdmin(UserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'first_name', 'last_name', 'is_admin', 'is_content_manager')
    list_filter = ('is_admin', 'is_content_manager')
    fieldsets = (
        ('Basic Info', {'fields': ('email', 'password', 'first_name', 'last_name', 'birth_date',
                                   'phone_number', 'gender', 'marital_Status')}),
        ('Address', {'fields': ('house_number', 'street', 'city', 'state', 'zip_code')}),
        ('Emergency Contact', {'fields': ('name', 'relation', 'primary_Phone', 'secondary_Phone')}),
        ('Permissions', {'fields': ('is_admin', 'is_content_manager')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

class NurseAdmin(UserAdmin):
    # The forms to add and change user instances
    form = NurseChangeForm
    add_form = NurseCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'first_name', 'last_name', 'department', 'is_admin', 'is_content_manager')
    list_filter = ('is_admin', 'is_content_manager')
    fieldsets = (
        ('Basic Info', {'fields': ('email', 'password', 'first_name', 'last_name', 'birth_date',
                                   'phone_number', 'gender', 'marital_Status')}),
        ('Address', {'fields': ('house_number', 'street', 'city', 'state', 'zip_code')}),
        ('Emergency Contact', {'fields': ('name', 'relation', 'primary_Phone', 'secondary_Phone')}),
        #('Nurse Details', {'fields':('department')}),
        ('Permissions', {'fields': ('is_admin', 'is_content_manager')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

class DoctorAdmin(UserAdmin):
    # The forms to add and change user instances
    form = DoctorChangeForm
    add_form = DoctorCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'first_name', 'last_name', 'is_admin', 'is_content_manager')
    list_filter = ('is_admin', 'is_content_manager')
    fieldsets = (
        ('Basic Info', {'fields': ('email', 'password', 'first_name', 'last_name', 'birth_date',
                                   'phone_number', 'gender', 'marital_Status')}),
        ('Address', {'fields': ('house_number', 'street', 'city', 'state', 'zip_code')}),
        ('Emergency Contact', {'fields': ('name', 'relation', 'primary_Phone', 'secondary_Phone')}),
        ('Doctor Details', {'fields': ('degree', 'specialty', 'experience')}),
        ('Permissions', {'fields': ('is_admin', 'is_content_manager')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

class PatientAdmin(UserAdmin):
    # The forms to add and change user instances
    form = PatientChangeForm
    add_form = PatientCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'first_name', 'last_name', 'is_admin', 'is_content_manager')
    list_filter = ('is_admin', 'is_content_manager')
    fieldsets = (
        ('Basic Info', {'fields': ('email', 'password', 'first_name', 'last_name', 'birth_date',
                                   'phone_number', 'gender', 'marital_Status')}),
        ('Address', {'fields': ('house_number', 'street', 'city', 'state', 'zip_code')}),
        ('Emergency Contact', {'fields': ('name', 'relation', 'primary_Phone', 'secondary_Phone')}),
        ('Patient Details', {'fields': ('medical_History', 'insurance_Provider', 'insurance_Policy_Number')}),
        ('Permissions', {'fields': ('is_admin', 'is_content_manager')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

# Now register the new UserAdmin...
admin.site.register(MyUser, MyUserAdmin)
admin.site.register(Nurse, NurseAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Patient, PatientAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)


