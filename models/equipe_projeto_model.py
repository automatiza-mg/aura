from django.db import models
from .base_model import BaseModel
from .usuario_model import Usuario
from .projeto_model import Projeto


class EquipeProjeto(BaseModel):
    user_id = models.ForeignKey(Usuario, on_delete=models.CASCADE) 
    projeto_id = models.ForeignKey(Projeto, on_delete=models.CASCADE) 
