# models.py
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class LowercaseEmailField(models.EmailField):
    def get_prep_value(self, value):
        value = super().get_prep_value(value)
        return value.lower() if value else value

class EventCard(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    date = models.CharField(max_length=10)
    location = models.CharField(max_length=100)
    img = models.ImageField(upload_to='events', default="", blank=True, null=True)
    about = models.CharField(max_length=100)

class CastImage(models.Model):
    event = models.ForeignKey(EventCard, related_name='cast_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='events/cast', blank=True)

class EventRegistration(models.Model):
    name = models.CharField(max_length=100, default="Unknown")
    email = LowercaseEmailField(('email address'), unique=True, null=True)
    phone_regex = RegexValidator(regex=r'^\d{10}$', message="phone number should exactly be in 10 digits")
    phone = models.CharField(default="", max_length=255, validators=[phone_regex], blank=True, null=True)
    event_name = models.CharField(max_length=200, blank=True, null=True)
