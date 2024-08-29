from django.db import models
from .base_model import BaseModel
from .orgao_model import Orgao


class ProjetoEstrategico(BaseModel):
    nome = models.CharField(max_length=100)
    orgao_id = models.ForeignKey(Orgao, on_delete=models.CASCADE)
    data_fim = models.DateTimeField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.nome}'