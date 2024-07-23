from django.db import models
from .base_model import BaseModel


class Usuario(BaseModel):
    nome = models.CharField(
        max_length=100,
    )
    email = models.EmailField(
        max_length=254,
    )
    github_user = models.URLField(
        max_length=300,
    )

