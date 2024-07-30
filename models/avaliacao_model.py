from django.db import models
from .base_model import BaseModel
from .projeto_model import Projeto


class Avaliacao(BaseModel): 
    projeto_id = models.ForeignKey(Projeto, on_delete=models.CASCADE) 
