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
        ('CS', 'Curso'),
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
        default='n/a',
    )
    telefone_demandante = models.CharField(
        max_length=13,
        default='n/a',
    )
    orgao_id = models.ForeignKey(Orgao,
                                 on_delete=models.CASCADE,
                                 default=0,
                                 )

    orgao_outros = models.CharField(
        max_length=100,
        default='n/a',
    )
    nome_processo = models.CharField(
        max_length=100,
        default='n/a',
    )
    descricao_processo = models.CharField(
        max_length=300,
        default='n/a',
    )
    processo_comum_choices = [
        ('S', 'Sim'),
        ('N', 'Não'),
    ]
    processo_comum_orgaos = models.CharField(
        max_length=1,
        choices=processo_comum_choices,
        default='n/a',
    )
    conhecimento_automate_choices = [
        ('A', 'Alto'),
        ('M', 'Médio'),
        ('B', 'Baixo'),
    ]
    conhecimento_automate = models.CharField(
        max_length=1,
        choices=conhecimento_automate_choices,
        default='n/a'
    )
    conhecimento_excel_choices = [
        ('A', 'Alto'),
        ('M', 'Médio'),
        ('B', 'Baixo'),
    ]
    conhecimento_excel = models.CharField(
        max_length=1,
        choices=conhecimento_excel_choices,
        default='n/a',
    )
    conhecimento_programacao_choices = [
        ('A', 'Alto'),
        ('M', 'Médio'),
        ('B', 'Baixo'),
    ]
    conhecimento_programacao = models.CharField(
        max_length=1,
        choices=conhecimento_programacao_choices,
        default='n/a',
    )
    projeto_estrategico_choices = [
        ('S', 'Sim'),
        ('N', 'Não'),
    ]
    projeto_estrategico = models.CharField(
        max_length=1,
        choices=projeto_estrategico_choices,
        default='n/a',
    )
    Projeto_estrategico_id = models.ForeignKey(
        ProjetoEstrategico,
        on_delete=models.CASCADE,
        null = True,
        blank= True,
        default=0,
    )
    existe_automacao_choices = [
        ('S', 'Sim'),
        ('N', 'Não'),
    ]
    existe_automacao = models.CharField(
        max_length=1,
        choices=existe_automacao_choices,
        default='n/a',
    )
    detalhamento_automacao = models.CharField(
        max_length=300,
        null = True,
        blank = True,
    )
    existe_banco_de_dados_choices = [
        ('S', 'Sim'),
        ('N', 'Não'),
    ]
    existe_banco_de_dados = models.CharField(
        max_length=1,
        choices=existe_banco_de_dados_choices,
        default='n/a',
    )
    detalhamento_banco_de_dados = models.CharField(
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
    periodicidade = models.CharField(
        max_length=3,
        choices=periodicidade_choices,
        default='n/a',
    )
    recorrencia = models.IntegerField(
        null= True,
        blank= True,
    )

    tempo_execucao_manual_min = models.IntegerField(
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
        default='n/a',
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
                                             default=0,
                                             )

    usuario_id_apoio = models.ForeignKey(Usuario,
                                         related_name='usuario_id_apoio',
                                         on_delete=models.CASCADE,
                                         default=0,
                                         )

    fase_choices = [
        ('PREC', 'Pedido recebido'),
        ('PEAN', 'Pedido em análise'),
        ('PANA', 'Pedido analisado'),
    ]
    fase = models.CharField(
        max_length=4,
        choices=fase_choices,
        default='n/a',
    )
    status_choices = [
        ('NAN', 'Pedido não analisado'),
        ('APR', 'Pedido aprovado'),
        ('ENC', 'Pedido encaminhado'),
        ('NAT', 'Pedido não atendido'),
    ]
    status = models.CharField(
        max_length=4,
        choices=status_choices,
        default='n/a',
    )
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
        choices=nivel_prioridade_choices,
        default='n/a',
    )
    nota_prioridade = models.IntegerField(
        default=0,
    )

    formato_atendimento_choices = [
        ('IA', 'Imersão automatiza'),
        ('TV', 'Time volante'),
        ('CM', 'Curso e mentoria'),
        ('CU', 'Curso EAD'),
        ('PE', 'Projeto extensão'),
        ('ND', 'Não definido'),
    ]
    formato_atendimento = models.CharField(
        max_length=2,
        choices=formato_atendimento_choices,
        null = True,
        blank = True,
    )
    def __str__(self):
        return f'{self.nome_processo}'