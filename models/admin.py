from django.contrib import admin
from .orgao_model import Orgao
from .pedido_imersao_model import PedidoImersao
from .projeto_model import Projeto
from .robo_model import Robo
from .sistema_model import Sistema
from .indicador_model import Indicador
# from .usuario_model import Usuario
from .equipe_projeto_model import EquipeProjeto
from .avaliacao_model import Avaliacao
from .pedido_manutencao_model import PedidoManutencao
from .projeto_estrategico_model import ProjetoEstrategico

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
class SistemaAdmin(admin.ModelAdmin):
    pass

class IndicadorAdmin(admin.ModelAdmin):
   pass

# class UsuarioAdmin(admin.ModelAdmin):
#     list_display = (
#         'nome',
#         'email',
#         'github_user',
#     )
class EquipeProjetoAdmin(admin.ModelAdmin):
    pass

class AvaliacaoAdmin(admin.ModelAdmin):
    pass

class PedidoManutencaoAdmin(admin.ModelAdmin):
    pass

class ProjetoEstrategicoAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
    )
    

admin.site.register(Orgao, OrgaoAdmin)
admin.site.register(PedidoImersao, PedidoImersaoAdmin)
admin.site.register(Projeto, ProjetoAdmin)
admin.site.register(Robo, RoboAdmin)
admin.site.register(Sistema, SistemaAdmin)
admin.site.register(Indicador, IndicadorAdmin)
# admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(EquipeProjeto, EquipeProjetoAdmin)
admin.site.register(Avaliacao, AvaliacaoAdmin)
admin.site.register(PedidoManutencao, PedidoManutencaoAdmin)
admin.site.register(ProjetoEstrategico, ProjetoEstrategicoAdmin)
