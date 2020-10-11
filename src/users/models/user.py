from django.contrib.auth.models import AbstractUser

from app.models import DefaultModel


class User(DefaultModel, AbstractUser):
    pass
