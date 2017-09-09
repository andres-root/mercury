from django.db import models
from django.contrib.auth.models import User


class Passenger(models.Model):
    user = models.OneToOneField(User)
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class Package(models.Model):
    origin = models.CharField(max_length=255, null=True, blank=True)
    destination = models.CharField(max_length=255, null=True, blank=True)
    cost = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class Ticket(models.Model):
    code = models.CharField(max_length=255, null=True, blank=True)
    cabin = models.CharField(max_length=255, null=True, blank=True)
    cost = models.CharField(max_length=255, null=True, blank=True)
    passenger = models.CharField(max_length=255, null=True, blank=True)
    package = models.CharField(max_length=255, null=True, blank=True)
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
