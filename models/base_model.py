from django.db import models


class BaseModel(models.Model):
    data_criacao = models.DateField(auto_now_add=True)
    data_atualizacao = models.DateField(auto_now=True)

    class Meta:
        abstract = True
