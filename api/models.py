from django.db import models
from django.contrib.auth.models import User


class Package(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    origin = models.CharField(max_length=255, null=True, blank=True)
    destination = models.CharField(max_length=255, null=True, blank=True)
    cost = models.CharField(max_length=255, null=True, blank=True)
    departure_date = models.DateTimeField()
    return_date = models.DateTimeField()
    discount = models.CharField(max_length=255, null=True, blank=True)
    segment = models.CharField(max_length=255, null=True, blank=True)
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


# class Passenger(models.Model):
#     user = models.OneToOneField(User)
#     active = models.BooleanField(default=True)
#     date_created = models.DateTimeField(auto_now_add=True)
#     date_updated = models.DateTimeField(auto_now=True)


# class Ticket(models.Model):
#     code = models.CharField(max_length=255, null=True, blank=True)
#     origin = models.CharField(max_length=255, null=True, blank=True)
#     destination = models.CharField(max_length=255, null=True, blank=True)
#     cabin = models.CharField(max_length=255, null=True, blank=True)
#     cost = models.CharField(max_length=255, null=True, blank=True)
#     passenger = models.CharField(max_length=255, null=True, blank=True)
#     package = models.CharField(max_length=255, null=True, blank=True)
#     active = models.BooleanField(default=True)
#     departure_date = models.DateTimeField()
#     return_date = models.DateTimeField()
#     date_created = models.DateTimeField(auto_now_add=True)
#     date_updated = models.DateTimeField(auto_now=True)


# class Segment(models.Model):
#     name = models.CharField(max_length=255, null=True, blank=True)
#     description = models.TextField(blank=True, null=True)
#     packages = models.CharField(max_length=255, null=True, blank=True)
#     active = models.BooleanField(default=True)
#     date_created = models.DateTimeField(auto_now_add=True)
#     date_updated = models.DateTimeField(auto_now=True)


# class Preferences(models.Model):
#     passenger = models.CharField(max_length=255, null=True, blank=True)
#     name = models.CharField(max_length=255, null=True, blank=True)
#     tags = models.TextField(blank=True, null=True)
#     segment = models.TextField(blank=True, null=True)
#     passenger = models.CharField(max_length=255, null=True, blank=True)
#     active = models.BooleanField(default=True)
#     date_created = models.DateTimeField(auto_now_add=True)
#     date_updated = models.DateTimeField(auto_now=True)
