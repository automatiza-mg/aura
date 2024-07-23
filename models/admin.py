from django.contrib import admin
from .orgao_model import Orgao
from .pedido_imersao_model import PedidoImersao
from .projeto_model import Projeto
from .robo_model import Robo
#from .sistema_model import Sistema
from .indicador_model import Indicador
from .usuario import Usuario
from .equipe_projeto import EquipeProjeto

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

class RoboAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'fase',
    )
# class SistemaAdmin(admin.ModelAdmin):
#     pass

class IndicadorAdmin(admin.ModelAdmin):
   pass

class UsuarioAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'email',
        'github_user',
    )
class EquipeProjetoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Orgao, OrgaoAdmin)
admin.site.register(PedidoImersao, PedidoImersaoAdmin)
admin.site.register(Projeto, ProjetoAdmin)
admin.site.register(Robo, RoboAdmin)
#admin.site.register(Sistema, SistemaAdmin)
admin.site.register(Indicador, IndicadorAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(EquipeProjeto, EquipeProjetoAdmin)