from django.db import models
from .base_model import BaseModel
from .pedido_imersao_model import PedidoImersao
#from .sistema_model import Sistema

class Robo(BaseModel):
    nome = models.CharField(max_length=100)
   
    tempo_execucao_robo = models.IntegerField(
        null= True,
        blank= True,
    )

    tempo_execucao_manual = models.IntegerField(
        null= True,
        blank= True,
    )

    #sistema_id = models.ForeignKey(Sistema, on_delete=models.CASCADE)
    
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
   