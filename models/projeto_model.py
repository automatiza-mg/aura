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
    # oportunidade_id = models.ForeignKey(PedidoImersao, 
    #                                     on_delete=models.CASCADE, 
    #                                     null=True, 
    #                                     blank=True,
    #                                     default='n/a'
    #)
    
    def __str__(self):
        return f'{self.nome}'

    # origen_demanda_choices = [
    #     ('PA', 'Pedidos de apoio'),
    #     ('PG', 'Pedidos do gabinete'),
    #     ('AG', 'Pedidos autogerados'),
    # ]
    # origem_demanda = models.CharField(
    #     max_length=2,
    #     choices=origen_demanda_choices,
    # )
    # nome_demandante = models.CharField(
    #     max_length=100,
    # )
   