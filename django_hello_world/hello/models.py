from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    date_of_birth = models.DateField('Date of birth')
    bio = models.TextField()
    email = models.EmailField(max_length=100, default='mail@example.com')
    skype = models.CharField(max_length=100, default='john_smith')
    jabber = models.EmailField(max_length=100, default='jabber@example.com')
    other_contacts = models.TextField(default='')
    photo = models.ImageField(upload_to='photos')


class Requests(models.Model):
    req = models.TextField()
    url = models.URLField(blank=True)
    datetime = models.DateTimeField(auto_now_add=True)
    method = models.CharField(max_length=10, blank=True)
    user = models.CharField(max_length=50, blank=True)
    priority = models.IntegerField(default=1)

    class Meta():
        ordering = ['id']


class State(models.Model):
    model = models.CharField(max_length=200)
    record_id = models.IntegerField()
    state = models.CharField(max_length=20)