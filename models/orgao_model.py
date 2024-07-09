from django.db import models
from .base_model import BaseModel


class Orgao(BaseModel):
    data_fim = models.DateTimeField(
        null=True,
        blank=True,
    )
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=10)
