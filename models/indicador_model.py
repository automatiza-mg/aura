from django.db import models
from .base_model import BaseModel
from .pedido_imersao_model import PedidoImersao


class Indicador(BaseModel):
    arrecadacao = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        null = True,
        blank = True,
        )
    
    horas_manuais_economizadas = models.IntegerField(
        null= True,
        blank= True,
    )
    servidores_reposicionados = models.IntegerField(
        null= True,
        blank= True,
    )
    horas_totais_economizadas = models.IntegerField(
        null= True,
        blank= True,
    )
    ganho_eficiencia = models.IntegerField(
        null= True,
        blank= True,
    )

    oportunidade_id = models.ForeignKey(PedidoImersao, on_delete=models.CASCADE)
    
