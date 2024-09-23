from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    github_user = models.URLField(
        max_length=300,
    )

    class Meta:
        db_table = 'auth_user'
