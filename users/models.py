from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom user that we can update later
class CustomUser(AbstractUser):
    # The birthdate of the user
    birthdate = models.DateField(null=True, blank=True)
