from django.db import models
from .base_model import BaseModel


class Sistema(BaseModel):
    nome = models.CharField(max_length=100)

   