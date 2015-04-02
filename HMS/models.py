from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
import hashlib, datetime, random
from datetime import date
from django import forms
#test for git
class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
  
    email = models.EmailField(
        verbose_name='e-mail',
        max_length=255,
        unique=True,
        )

    activation_key = models.CharField(max_length=40, blank=True)
    key_expires = models.DateTimeField(default=datetime.date.today())
    first_name = models.CharField(max_length = 20, default = "")
    last_name = models.CharField(max_length = 20, default = "")
    birth_date = models.DateField(default = date.today)
    phone_number = models.IntegerField(default = 0)
    gender = models.CharField(max_length = 7, default = "")
    marital_Status = models.CharField(max_length = 10, default = "")

    #Address
    house_number = models.IntegerField(default = 0)
    street = models.CharField(max_length = 30, default = "")
    city = models.CharField(max_length = 20, default = "")
    state = models.CharField(max_length = 20, default = "")
    zip_Code = models.IntegerField(default = 0)

    #Emergency Contact
    name = models.CharField(max_length = 50, default = "")
    relation = models.CharField(max_length = 20, default = "")
    primary_Phone = models.IntegerField(default = 0)
    secondary_Phone = models.IntegerField(default = 0)
    is_active = models.BooleanField(default=True)
    is_content_manager = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    #user_Type = models.CharField(max_length = 10, default = "")

    objects = MyUserManager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    def save(self, *args, **kwargs):
        # if user being demoted from content manager, make sure they are not
        # managing any courses
        super().save(*args, **kwargs)

    #def get_Type():
        #return self.user_Type

class Nurse(MyUser):
    department = models.CharField(max_length = 30, default = "")
    #insurance
    #availability
    #calendar

    #def setUserType():
     #   super.user_Type = "Nurse"
      #  return


class Doctor(MyUser):
    degree = models.CharField(max_length = 40, default = "")
    specialty = models.CharField(max_length = 40, default = "")
    experience = models.CharField(max_length = 60, default = "")
    #availability
    #calendar
    #insurance
    #current patients

    #def setUserType():
     #   super.user_Type = "Doctor"
      #  return
    
class Patient(MyUser):
    medical_History = models.CharField(max_length = 40, default = "")
    insurance_Provider = models.CharField(max_length = 40, default = "")
    insurance_Policy_Number = models.IntegerField(default = 0)
    #primaryCareProvider
    #Diagnosis
    #Calendar

    #def setUserType():
     #   super.user_Type = "Patient"
      #  return
    
