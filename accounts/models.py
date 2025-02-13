from django.db import models

from django.contrib.auth.models import AbstractUser, UserManager

class User(AbstractUser):
    """
    Users within the Django authentication system are represented by this
    model.

    Username and password are required. Other fields are optional.
    """
