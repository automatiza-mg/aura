from django.db import models
from .base_model import BaseModel
from .orgao_model import Orgao
from .projeto_estrategico_model import ProjetoEstrategico
from .usuario_model import Usuario
from .projeto_model import Projeto
from django.core.validators import MinValueValidator

class PedidoImersao(BaseModel):

    yes_no_list = [
        ('S', 'SIM'),
        ('N', 'NÃO'),
    ]

    amb_list = [
        ('A', 'ALTO'),
        ('M', 'MÉDIO'),
        ('B', 'BAIXO'),
    ]

    origen_demanda_choices = [
        ('PA', 'PEDIDO DE APOIO'),
        ('PG', 'PEDIDOS DO GABINETE'),
        ('AG', 'PEDIDOS AUTOGERADOS'),
        ('CS', 'CURSO'),
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
        null = True,
        blank = True,
        max_length=13,
    )
    orgao_id = models.ForeignKey(Orgao,
                                 on_delete=models.CASCADE,
                                 )

    orgao_outros = models.CharField(
        null = True,
        blank = True,
        max_length=100,
    )
    nome_processo = models.CharField(
        max_length=100,
    )
    descricao_processo = models.TextField()
    processo_comum_choices = yes_no_list
    processo_comum_orgaos = models.CharField(
        max_length=1,
        choices=processo_comum_choices,
    )
    conhecimento_automate_choices =  amb_list
    conhecimento_automate = models.CharField(
        max_length=1,
        choices=conhecimento_automate_choices,
    )
    conhecimento_excel_choices =  amb_list
    conhecimento_excel = models.CharField(
        max_length=1,
        choices=conhecimento_excel_choices,
    )
    conhecimento_programacao_choices =  amb_list
    conhecimento_programacao = models.CharField(
        max_length=1,
        choices=conhecimento_programacao_choices,
    )
    projeto_estrategico_choices = yes_no_list
    projeto_estrategico = models.CharField(
        max_length=1,
        choices=projeto_estrategico_choices,
    )
    projeto_estrategico_id = models.ForeignKey(
        ProjetoEstrategico,
        on_delete=models.CASCADE,
        null = True,
        blank= True,
    )
    existe_automacao_choices = yes_no_list
    existe_automacao = models.CharField(
        max_length=1,
        choices=existe_automacao_choices,
    )
    detalhamento_automacao = models.TextField(
        null = True,
        blank = True,
    )
    existe_banco_de_dados_choices = yes_no_list
    existe_banco_de_dados = models.CharField(
        max_length=1,
        choices=existe_banco_de_dados_choices,
    )
    detalhamento_banco_de_dados = models.TextField(
        null = True,
        blank = True,
    )
    periodicidade_choices = [
        ('UNI', 'ÚNICO'),
        ('DIA', 'DIÁRIO'),
        ('SMN', 'SEMANAL'),
        ('QUI', 'QUINZENAL'),
        ('MEN', 'MENSAL'),
        ('BIM', 'BIMESTRAL'),
        ('TRI', 'TRIMESTRAL'),
        ('SMT', 'SEMESTRAL'),
        ('ANU', 'ANUAL'),
    ]
    periodicidade = models.CharField(
        max_length=3,
        choices=periodicidade_choices,
    )
    recorrencia = models.IntegerField(
        null= True,
        blank= True,
    )

    tempo_execucao_manual_min = models.FloatField(
        null= True,
        blank= True,
        validators = [MinValueValidator(0.0)],
    )
    impacto_arrecadacao_choices = yes_no_list
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
    usuario_id_principal = models.ForeignKey(Usuario,
                                             related_name='usuario_id_principal',
                                             on_delete=models.CASCADE,
                                             )

    usuario_id_apoio = models.ForeignKey(Usuario,
                                         related_name='usuario_id_apoio',
                                         on_delete=models.CASCADE,
                                         )

    fase_choices = [
        ('PREC', 'PEDIDO RECEBIDO'),
        ('PEAN', 'PEDIDO EM ANÁLISE'),
        ('PANA', 'PEDIDO ANALISADO'),
    ]
    fase = models.CharField(
        max_length=4,
        choices=fase_choices,
    )
    status_choices = [
        ('NAN', 'PEDIDO NÃO ANALISADO'),
        ('PRI', 'PRIMEIRO CONTATO'),
        ('APR', 'PEDIDO APROVADO'),
        ('ENC', 'PEDIDO ENCAMINHADO'),
        ('NAT', 'PEDIDO NÃO ATENDIDO'),
    ]
    status = models.CharField(
        max_length=4,
        choices=status_choices,
    )
    link_issue = models.URLField(
        max_length=300,
        null = True,
        blank = True,
    )
    nivel_prioridade_choices = amb_list
    nivel_prioridade = models.CharField(
        max_length=1,
        choices=nivel_prioridade_choices,
        null = True,
        blank = True,
    )
    nota_prioridade = models.IntegerField(
        null = True,
        blank = True,
    )

    formato_atendimento_choices = [
        ('IA', 'IMERSÃO AUTOMATIZA'),
        ('TV', 'TIME VOLANTE'),
        ('CM', 'CURSO MENTORIA'),
        ('CU', 'CURSO EAD'),
        ('PE', 'PROJETO EXTENSÃO'),
        ('ND', 'NÃO DEFINIDO'),
    ]
    formato_atendimento = models.CharField(
        max_length=2,
        choices=formato_atendimento_choices,
        null = True,
        blank = True,
    )
    projeto_id = models.ForeignKey(Projeto,
                                 on_delete=models.CASCADE,
                                 null=True,
                                 blank=True,
    )

    def __str__(self):
        return f'{self.nome_processo}'
