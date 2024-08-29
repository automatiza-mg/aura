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
    
    def __str__(self):
        return f'{self.nome}'
    
   