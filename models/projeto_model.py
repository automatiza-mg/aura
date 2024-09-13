from django.db import models
from .base_model import BaseModel
#from .pedido_imersao_model import PedidoImersao


class Projeto(BaseModel):
    data_fim = models.DateField(
        null=True,
        blank=True,
    )
    nome = models.CharField(max_length=100)
    fase_choices = [
        ('FORM', 'Formatação'),
        ('PLAN', 'Planejamento'),
        ('EXEC', 'Execução'),
        ('CONC', 'Concluído'),

    ]
    fase = models.CharField(
        max_length=4,
        choices=fase_choices,
    )

    def __str__(self):
        return f'{self.nome}'
