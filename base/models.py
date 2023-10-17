from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from .managers import CustomUserManager
from django.core.validators import RegexValidator

class LowercaseEmailField(models.EmailField):
    """
    Override EmailField to convert emails to lowercase before saving.
    """
    def to_python(self, value):
        """
        Convert email to lowercase.
        """
        value = super(LowercaseEmailField, self).to_python(value)
        # Value can be None so check that it's a string before lowercasing.
        if isinstance(value, str):
            return value.lower()
        return value


def upload_to(instance, filename):
    return 'base/images/{filename}'.format(filename=filename)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    USER_CHOICES=[
        ('employee','Employee'),
        ('sub_employee','Sub-employee'),
        ('baseUser','User'),
    ]
    email = LowercaseEmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    admin = models.BooleanField(default=False)
    username = models.CharField(max_length=12)
    user_image = models.ImageField(upload_to=upload_to, default="")
    phone_regex = RegexValidator( regex = r'^\d{10}$',message = "phone number should exactly be in 10 digits")
    phone = models.CharField(default="",max_length=255, validators=[phone_regex], blank = True, null=True)  # you can set it unique = True
    house = models.CharField(default="",max_length=255,blank = True, null=True)
    area = models.CharField(default="",max_length=255,blank = True, null=True)
    landmark = models.CharField(default="",max_length=255,blank = True, null=True)
    pincode = models.CharField(default="",max_length=6,blank = True, null=True)
    town = models.CharField(default="",max_length=255,blank = True, null=True)
    state = models.CharField(default="",max_length=255,blank = True, null=True)
    country = models.CharField(default="",max_length=255,blank = True, null=True)
  
    user_choices = models.TextField(choices=USER_CHOICES,blank = True, null=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    

class UserProducts(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    type = models.CharField(default='',max_length=20)
    manufacturer = models.CharField(default='',max_length=20)
    model = models.CharField(default='',max_length=20)
    condition = models.CharField(default='',max_length=20)

    def __str__(self):
        return self.name

