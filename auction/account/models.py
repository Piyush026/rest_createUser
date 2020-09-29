from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.

class Account(AbstractBaseUser):
    fname = models.CharField(max_length=250)
    lname = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    password2 = models.CharField(max_length=250)
    mobile = models.CharField(max_length=15)
    telephone = models.CharField(max_length=15)
    email = models.EmailField(unique=True, max_length=254, )
    confirm_email = models.EmailField(max_length=254, )
    company = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    address1 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postalZip = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'
