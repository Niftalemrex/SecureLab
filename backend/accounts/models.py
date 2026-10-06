from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        PATIENT = "PATIENT", "Patient"
        TECHNICIAN = "TECHNICIAN", "Technician"

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.PATIENT,
    )

    def __str__(self):
        return self.username