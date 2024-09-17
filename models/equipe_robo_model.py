from django.db import models
from .base_model import BaseModel
from .equipe_projeto_model import EquipeProjeto
from .robo_model import Robo


class EquipeRobo(BaseModel):
    equipe_projeto_id = models.ForeignKey(EquipeProjeto, on_delete=models.CASCADE) 
    robo_id = models.ForeignKey(Robo, on_delete=models.CASCADE) 

    def __str__(self):
        return f'{self.robo_id} - {self.equipe_projeto_id}'