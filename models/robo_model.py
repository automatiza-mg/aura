from django.db import models
from .base_model import BaseModel
from .pedido_imersao_model import PedidoImersao
from .sistema_model import Sistema
from django.core.validators import MinValueValidator

class Robo(BaseModel):
    nome = models.CharField(max_length=100)

    tempo_execucao_robo_min = models.FloatField(
        null= True,
        blank= True,
        validators=[MinValueValidator(0.0)],
    )

    tempo_execucao_manual_min = models.FloatField(
        null= True,
        blank= True,
        validators=[MinValueValidator(0.0)],
    )

    fase_choices = [
        ('NAOI', 'Não iniciado'),
        ('EXEC', 'Em execução'),
        ('CONC', 'Concluído'),
    ]
    fase = models.CharField(
        max_length=4,
        choices=fase_choices,
    )
    oportunidade_id = models.ForeignKey(PedidoImersao, on_delete=models.CASCADE)

    sistema_id = models.ForeignKey(Sistema, 
                                on_delete=models.CASCADE,
                                null=True,
                                blank=True,
    )

    def __str__(self):
        return f'{self.nome}'
