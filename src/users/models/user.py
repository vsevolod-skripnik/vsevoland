from django.contrib.auth.models import AbstractUser, UserManager

from default.models import DefaultModel


class User(DefaultModel, AbstractUser):
    objects = UserManager()
