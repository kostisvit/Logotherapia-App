from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager
from django_extensions.db.models import TimeStampedModel
from django.utils.translation import gettext_lazy as _

class User(AbstractBaseUser, PermissionsMixin,TimeStampedModel):
    class Gender(models.TextChoices):
        MALE = 'M', _('Male')
        FEMALE = 'F', _('Female')
        OTHER = 'O', _('Other')
    #organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField(unique=True)
    #email_alias = models.EmailField(unique=True, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_company_owner = models.BooleanField(default=False)
    date_of_birth = models.DateField(null=True)
    phone_number = models.CharField(max_length=10, unique=False,null=True, blank=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    gender = models.CharField(
        max_length=1,
        choices=Gender.choices,
        default=Gender.OTHER,
    )
    first_login = models.BooleanField(default=True)
    
    objects = CustomUserManager()
  
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('Χρήστες')
        verbose_name_plural = _('Χρήστες')
    
    def __str__(self):
        return self.email