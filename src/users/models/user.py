from django.contrib.auth.models import AbstractUser

from default.models import DefaultModel


class User(DefaultModel, AbstractUser):
    pass
