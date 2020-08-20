from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
import uuid
import datetime
from django.contrib.auth.models import Permission
from django.contrib.auth.models import Group
from django.contrib.auth.models import PermissionsMixin
from .base_model import BaseModel


class UserType(BaseModel):
    is_user_account = models.BooleanField()
    value = models.TextField()


class MyUserManager(BaseUserManager):
    def create_user(self, phone_number, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not phone_number:
            raise ValueError('Users must have an phone_number')

        user = self.model(
            createdate=datetime.datetime.now(),
            modificationdate=datetime.datetime.now(),
            phone_number=phone_number,
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, date_of_birth, password=None):
        """
        Creates and saves a superuser
        """
        user = self.create_user(
            phone_number,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        blank=True
    )
    user_name = models.CharField(max_length=15)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    createdate = models.DateTimeField(default=datetime.datetime.now())
    deletedate = models.DateTimeField(blank=True, null=True)
    modificationdate = models.DateTimeField(default=datetime.datetime.now())
    is_delete = models.BooleanField(default=False)
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=13,
        unique=True,
        verbose_name="Phone Number")
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    user_type = models.ForeignKey(
        UserType, on_delete=models.SET_NULL, null=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['date_of_birth']

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
