from django.db import models

class EventCard(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    date = models.CharField(max_length=10)
    loction = models.CharField(max_length=100)
    img = models.ImageField(upload_to='events',default="", blank=True, null=True)
    about = models.CharField(max_length=10000)
    cast_image1 = models.ImageField(upload_to='events/cast', default="", blank=True, null=True)
    cast_image2 = models.ImageField(upload_to='events/cast', default="", blank=True, null=True)
    cast_image3 = models.ImageField(upload_to='events/cast', default="", blank=True, null=True)
    cast_image4 = models.ImageField(upload_to='events/cast', default="", blank=True, null=True)
    cast_image5 = models.ImageField(upload_to='events/cast', default="", blank=True, null=True)
    cast_image6 = models.ImageField(upload_to='events/cast', default="", blank=True, null=True)
    cast_image7 = models.ImageField(upload_to='events/cast', default="", blank=True, null=True)
