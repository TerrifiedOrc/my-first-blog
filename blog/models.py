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
    dob = models.CharField(default="21/03/1999", max_length=200)
    email = models.CharField(max_length=200)
    address = models.TextField(default="", max_length=200)
    phone = models.CharField(default="", max_length=200)

class Employment(models.Model):
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    skills = models.CharField(max_length=200)
    startDate = models.TextField(blank=True, null=True)
    endDate = models.TextField(blank=True, null=True)
    foreignKey = models.ForeignKey(CV, default="", on_delete=models.CASCADE)

class Education(models.Model):
    address = models.CharField(max_length=200)
    startDate = models.TextField(blank=True, null=True)
    endDate = models.TextField(blank=True, null=True)
    foreignKey = models.ForeignKey(CV, default="", on_delete=models.CASCADE)