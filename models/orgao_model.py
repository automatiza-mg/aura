from django.db import models
from .base_model import BaseModel


class Orgao(BaseModel):
    data_fim = models.DateField(
        null=True,
        blank=True,
    )
    nome = models.CharField(max_length=100, unique=True)
    sigla = models.CharField(max_length=50, unique=True)
    

    def __str__(self):
        return f'{self.sigla}'