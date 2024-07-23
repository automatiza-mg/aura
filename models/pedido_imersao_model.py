from django.db import models
from .base_model import BaseModel
from .orgao_model import Orgao
from .projeto_estrategico_model import ProjetoEstrategico
from .usuario_model import Usuario

class PedidoImersao(BaseModel):
    origen_demanda_choices = [
        ('PA', 'Pedidos de apoio'),
        ('PG', 'Pedidos do gabinete'),
        ('AG', 'Pedidos autogerados'),
    ]
    origem_demanda = models.CharField(
        max_length=2,
        choices=origen_demanda_choices,
    )
    nome_demandante = models.CharField(
        max_length=100,
    )
    email_demandante = models.EmailField(
        max_length=254,
    )
    telefone_demandante = models.CharField(
        max_length=13,
    )
    orgao_id = models.ForeignKey(Orgao, on_delete=models.CASCADE)

    orgao_outros = models.CharField(
        max_length=100,
    )
    nome_processo = models.CharField(
        max_length=100,
    )
    descricao_processo = models.CharField(
        max_length=300,
    )
    processo_comum_choices = [
        ('S', 'Sim'),
        ('N', 'Não'),
    ]
    processo_comum_orgaos = models.CharField(
        max_length=1,
        choices=processo_comum_choices,
    )
    conhecimento_automate_choices = [
        ('A', 'Alto'),
        ('M', 'Médio'),
        ('B', 'Baixo'),
    ]
    conhecimento_automate = models.CharField(
        max_length=1,
        choices=conhecimento_automate_choices
    )
    conhecimento_excel_choices = [
        ('A', 'Alto'),
        ('M', 'Médio'),
        ('B', 'Baixo'),
    ]
    conhecimento_excel = models.CharField(
        max_length=1,
        choices=conhecimento_excel_choices
    )
    conhecimento_programacao_choices = [
        ('A', 'Alto'),
        ('M', 'Médio'),
        ('B', 'Baixo'),
    ]
    conhecimento_programacao = models.CharField(
        max_length=1,
        choices=conhecimento_programacao_choices
    )
    projeto_estrategico_choices = [
        ('S', 'Sim'),
        ('N', 'Não'),
    ]
    projeto_estrategico = models.CharField(
        max_length=1,
        choices=projeto_estrategico_choices,
    )
    Projeto_estrategico_id = models.ForeignKey(
        ProjetoEstrategico, 
        on_delete=models.CASCADE,
        null = True,
        blank= True
    )
    existe_automacao_choices = [
        ('S', 'Sim'),
        ('N', 'Não'),
    ]
    existe_automacao = models.CharField(
        max_length=1,
        choices=existe_automacao_choices,
    )
    detalhamento_automacao = models.CharField(
        max_length=300,
        null = True,
        blank = True,
    )
    existe_bd_choices = [
        ('S', 'Sim'),
        ('N', 'Não'),
    ]
    existe_bd = models.CharField(
        max_length=1,
        choices=existe_bd_choices,
    )
    detalhamento_bd = models.CharField(
        max_length=300,
        null = True,
        blank = True,
    )
    periodicidade_choices = [
        ('DIA', 'Diário'),
        ('SMN', 'Semanal'),
        ('QUI', 'Quinzenal'),
        ('MEN', 'Mensal'),
        ('BIM', 'Bimestral'),
        ('TRI', 'Trimestral'),
        ('SMT', 'Semestral'),
        ('ANU', 'Anual'),
    ]
    periocdicidade = models.CharField(
        max_length=3,
        choices=periodicidade_choices,
    )
    recorrencia = models.IntegerField

    tempo_execucao_manual = models.IntegerField(
        null= True,
        blank= True,
    )
    impacto_arrecadacao_choices = [
        ('S', 'Sim'),
        ('N', 'Não'),
    ]
    impacto_arrecadacao = models.CharField(
        max_length=1,
        choices=impacto_arrecadacao_choices,
    )
    valor_arrecadacao = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        null = True,
        blank = True,
    )
    usuario_id_principal = models.ForeignKey(Usuario, on_delete=models.CASCADE,)
    
    usuario_id_apoio = models.ForeignKey(Usuario, on_delete=models.CASCADE,)

    # fase_choices = [
    #     ('PREC', 'Pedido recebido'),
    #     ('PEAN', 'Pedido em análise'),
    #     ('PANA', 'Pedido analisado'),
    # ]
    # fase = models.CharField(
    #     max_length=4,
    #     choices=fase_choices,
    # )
    # status_choices = [
    #     ('PREC', 'Pedido recebido'),
    #     ('PEAN', 'Pedido em análise'),
    #     ('PANA', 'Pedido analisado'),
    # ]
    # status = models.CharField(
    #     max_length=4,
    #     choices=status_choices,
    # )
    link_issue = models.URLField(
        max_length=300,
        null = True,
        blank = True,
    )
    nivel_prioridade_choices =[
        ('A', 'Alto'),
        ('M', 'Médio'),
        ('B', 'Baixo'),
    ]
    nivel_prioridade = models.CharField(
        max_length=1,
        choices=nivel_prioridade_choices
    )
    nota_prioridade = models.IntegerField(
        max_length=2
    )
    formato_atendimento_choices = [
        ('IA', 'Imersão automatiza'),
        ('TV', 'Time volante'),
        ('CM', 'Curso e mentoria'),
        ('CU', 'Curso EAD'),
        ('PE', 'Projeto extensão'),
    ]
    formato_atendimento = models.CharField(
        max_length=2,
        choices=formato_atendimento_choices
        null = True,
        blank = True,
    )

