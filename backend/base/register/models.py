from django.db import models
from base.models import *

class EventCard(models.Model):
    title       = models.CharField(max_length=200)
    genre       = models.CharField(max_length=100)
    date        = models.CharField(max_length=10)
    loction     = models.CharField(max_length=100)
    img         = models.ImageField(upload_to='events',default="", blank=True, null=True)
    about       = models.CharField(max_length=100)
    cast_image1 = models.ImageField(upload_to='events/cast', default="", blank=True, null=True)
    cast_image2 = models.ImageField(upload_to='events/cast', default="", blank=True, null=True)
    cast_image3 = models.ImageField(upload_to='events/cast', default="", blank=True, null=True)
    cast_image4 = models.ImageField(upload_to='events/cast', default="", blank=True, null=True)
    cast_image5 = models.ImageField(upload_to='events/cast', default="", blank=True, null=True)
    cast_image6 = models.ImageField(upload_to='events/cast', default="", blank=True, null=True)
    cast_image7 = models.ImageField(upload_to='events/cast', default="", blank=True, null=True)

class EventRegistration(models.Model):
    name = models.CharField(max_length=100, default="Unknown")
    email = LowercaseEmailField(('email address'), unique=True, null=True)
    phone_regex  = RegexValidator( regex = r'^\d{10}$',message = "phone number should exactly be in 10 digits")
    phone        = models.CharField(default="",max_length=255, validators=[phone_regex], blank = True, null=True)
    event_name = models.CharField(max_length=200, blank=True, null=True)