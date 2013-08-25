from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    date_of_birth = models.DateField('Date of birth')
    bio = models.TextField()
    email = models.CharField(max_length=100, default='mail@example.com')
    skype = models.CharField(max_length=100, default='john_smith')
    jabber = models.CharField(max_length=100, default='jabber@example.com')
    other_contacts = models.TextField(default='')

class Requests(models.Model):
    req = models.TextField()