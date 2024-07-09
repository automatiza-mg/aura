from django.db import models
from .base_model import BaseModel


class PedidoImersao(BaseModel):
    origen_demanda_choices = [
        ('PA', 'Pedidos de apoio'),
        ('PG', 'Pedidos do gabinete'),
        ('AG', 'Pedidos autogerados'),
    ]
    origem_demanda = models.CharField(
        max_length=2,
        choices=origen_demanda_choices,
    )
    nome_demandante = models.CharField(
        max_length=100,
    )
