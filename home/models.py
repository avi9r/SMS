from django.db import models
from django.db import connections
from twilio.rest import Client
from django.utils import timezone


# Create your models here.

class Person(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    ph_number = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pin = models.CharField(max_length=6)
    
    class Meta:
        db_table="user"

class Admin(models.Model):
    username = models.CharField( max_length=50)
    password = models.CharField( max_length=50)
    account_sid = models.CharField( max_length=100)
    auth_token = models.CharField(max_length=100)
    twillo_number = models.CharField( max_length=50)
    class Meta:
        db_table="admin"


class Message(models.Model):
    msg_from = models.CharField( max_length=50)
    msg_to = models.CharField( max_length=50)
    msg = models.CharField( max_length=50)
    account_type = models.CharField( max_length=50)
    status =models.BooleanField(default=0)
    created_at = models.TimeField(default = timezone.now)
    updated_at = models.TimeField(default = timezone.now)
    
    class Meta:
        db_table="msg_single"

class Message2(models.Model):
    msg_from = models.CharField( max_length=50)
    msg_to = models.CharField( max_length=100)
    msg = models.CharField( max_length=50)
    account_type = models.CharField( max_length=50)
    status =models.BooleanField(default=0)
    created_at = models.TimeField(default = timezone.now)
    updated_at = models.TimeField(default = timezone.now)
    
    class Meta:
        db_table="msg_bulk"

    

    