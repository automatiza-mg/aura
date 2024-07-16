from django.contrib import admin
from .orgao_model import Orgao
from .pedido_imersao_model import PedidoImersao
from .projeto_model import Projeto

class OrgaoAdmin(admin.ModelAdmin):
    # fields at the models' index page
    list_display = (
        'sigla',
        'nome',
    )
    # fields at the models' edit page
    fields = [
        'sigla',
        'nome',
        'data_fim'
    ]



class PedidoImersaoAdmin(admin.ModelAdmin):
    list_display = (
        'origem_demanda',
        'nome_demandante',
    )

class ProjetoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Orgao, OrgaoAdmin)
admin.site.register(PedidoImersao, PedidoImersaoAdmin)
admin.site.register(Projeto,ProjetoAdmin)
