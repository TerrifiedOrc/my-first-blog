from django.conf import settings
from django.db import models
from django.utils import timezone
from django.template.defaultfilters import date
from django import forms

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class CV(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    dob = models.DateTimeField(blank=True, null=True)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    employment = []

    created_date = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.last_updated = timezone.now()
        self.save()

    def __str__(self):
        return self.fname + " " + self.lname + "'s CV"

class Employment(models.Model):
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    skills = models.CharField(max_length=200)
    startDate = models.DateTimeField(blank=True, null=True)
    endDate = models.DateTimeField(blank=True, null=True)

class Education(models.Model):
    qualifications = []
    address = models.CharField(max_length=200)
    startDate = models.DateTimeField(blank=True, null=True)
    endDate = models.DateTimeField(blank=True, null=True)