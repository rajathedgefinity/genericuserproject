from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings

# Create your models here.
class UserProfileManager(BaseUserManager):
    """Manager for User Profile Model"""

    def create_user(self, email, name, mobile_no, password=None, is_supervisor=False, is_gaurd=False):
        """Create new user profile"""
        if not email:
            raise ValueError("User must have email address")

        email = self.normalize_email(email)
        user = self.model(email=email,name=name,mobile_no=mobile_no,is_supervisor=is_supervisor,is_gaurd=is_gaurd)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, mobile_no, password):
        """Create and Save New SuperUser with given Details"""
        user = self.create_user(email, name, mobile_no, password)

        user.is_superuser = True
        user.is_staff = True
        user.is_supervisor = True
        user.is_gaurd = True

        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the System"""
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    mobile_no = models.CharField(max_length=12)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_supervisor = models.BooleanField(default=False)
    is_gaurd = models.BooleanField(default=False)
    is_demo_account = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','mobile_no']

    def get_full_name(self):
        """Retrieve Full Name of User"""
        return self.first_name+' '+self.last_name

    def get_short_name(self):
        """Retrieve Short Name of User"""
        return self.name

    def get_contact_details(self):
        """Retrieve Contact Details of the User"""
        return 'Email ID: {} Mobile No: {}'.format(self.email, self.mobile_no)

    def __str__(self):
        """Return Representation of User"""
        return self.email
