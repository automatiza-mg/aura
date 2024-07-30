from django.db import models
from .base_model import BaseModel
from .robo_model import Robo


class PedidoManutencao(BaseModel):
    robo_id = models.ForeignKey(Robo, on_delete=models.CASCADE)
    
    data = models.DateField
    
    link_issue = models.URLField(
        max_length=300,
    )

