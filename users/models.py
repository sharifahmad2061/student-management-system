from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)
from django.contrib.auth import get_user_model
# Create your models here.


class CustomUserManager(BaseUserManager):
    """
    custom user manager
    """

    def create_user(self, email, password=None, is_student=True):
        if not email:
            raise ValueError('users must have an email')
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.is_student = is_student
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    """
    uses email as the primary key field
    """
    email = models.EmailField(
        verbose_name='email address',
        unique=True,
        max_length=256
    )
    is_student = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        "does the user have perm to view app"
        return True


class StudentProfile(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        primary_key=True,
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    preferred_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profile-images')
    discord_name = models.CharField(max_length=100)
    github_username = models.CharField(max_length=100)
    codepen_username = models.CharField(max_length=100)
    fcc_profile_url = models.CharField(max_length=256)

    LEVELS = (
        (1, 'Level One'),
        (2, 'Level Two'),
        (3, 'Level Three')
    )

    current_level = models.IntegerField(choices=LEVELS)
    phone = models.CharField(max_length=50)
    timezone = models.CharField(max_length=50)
