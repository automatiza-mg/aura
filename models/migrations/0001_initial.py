# Generated by Django 5.0.7 on 2024-09-13 22:01

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orgao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateField(auto_now_add=True)),
                ('data_atualizacao', models.DateField(auto_now=True)),
                ('data_fim', models.DateField(blank=True, null=True)),
                ('nome', models.CharField(max_length=100, unique=True)),
                ('sigla', models.CharField(max_length=10, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateField(auto_now_add=True)),
                ('data_atualizacao', models.DateField(auto_now=True)),
                ('data_fim', models.DateField(blank=True, null=True)),
                ('nome', models.CharField(max_length=100)),
                ('fase', models.CharField(choices=[('FORM', 'Formatação'), ('PLAN', 'Planejamento'), ('EXEC', 'Execução'), ('CONC', 'Concluído')], max_length=4)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sistema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateField(auto_now_add=True)),
                ('data_atualizacao', models.DateField(auto_now=True)),
                ('nome', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('github_user', models.URLField(max_length=300)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'auth_user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='PedidoImersao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateField(auto_now_add=True)),
                ('data_atualizacao', models.DateField(auto_now=True)),
                ('origem_demanda', models.CharField(choices=[('PA', 'PEDIDO DE APOIO'), ('PG', 'PEDIDOS DO GABINETE'), ('AG', 'PEDIDOS AUTOGERADOS'), ('CS', 'CURSO')], max_length=2)),
                ('nome_demandante', models.CharField(max_length=100)),
                ('email_demandante', models.EmailField(max_length=254)),
                ('telefone_demandante', models.CharField(max_length=13)),
                ('orgao_outros', models.CharField(blank=True, max_length=100, null=True)),
                ('nome_processo', models.CharField(max_length=100)),
                ('descricao_processo', models.TextField()),
                ('processo_comum_orgaos', models.CharField(choices=[('S', 'SIM'), ('N', 'NÃO')], max_length=1)),
                ('conhecimento_automate', models.CharField(choices=[('A', 'ALTO'), ('M', 'MÉDIO'), ('B', 'BAIXO')], max_length=1)),
                ('conhecimento_excel', models.CharField(choices=[('A', 'ALTO'), ('M', 'MÉDIO'), ('B', 'BAIXO')], max_length=1)),
                ('conhecimento_programacao', models.CharField(choices=[('A', 'ALTO'), ('M', 'MÉDIO'), ('B', 'BAIXO')], max_length=1)),
                ('projeto_estrategico', models.CharField(choices=[('S', 'SIM'), ('N', 'NÃO')], max_length=1)),
                ('existe_automacao', models.CharField(choices=[('S', 'SIM'), ('N', 'NÃO')], max_length=1)),
                ('detalhamento_automacao', models.TextField(blank=True, null=True)),
                ('existe_banco_de_dados', models.CharField(choices=[('S', 'SIM'), ('N', 'NÃO')], max_length=1)),
                ('detalhamento_banco_de_dados', models.TextField(blank=True, null=True)),
                ('periodicidade', models.CharField(choices=[('DIA', 'DIÁRIO'), ('SMN', 'SEMANAL'), ('QUI', 'QUINZENAL'), ('MEN', 'MENSAL'), ('BIM', 'BIMESTRAL'), ('TRI', 'TRIMESTRAL'), ('SMT', 'SEMESTRAL'), ('ANU', 'ANUAL')], max_length=3)),
                ('recorrencia', models.IntegerField(blank=True, null=True)),
                ('tempo_execucao_manual_min', models.IntegerField(blank=True, null=True)),
                ('impacto_arrecadacao', models.CharField(choices=[('S', 'SIM'), ('N', 'NÃO')], max_length=1)),
                ('valor_arrecadacao', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('fase', models.CharField(choices=[('PREC', 'PEDIDO RECEBIDO'), ('PEAN', 'PEDIDO EM ANÁLISE'), ('PANA', 'PEDIDO ANALISADO')], max_length=4)),
                ('status', models.CharField(choices=[('NAN', 'PEDIDO NÃO ANALISADO'), ('APR', 'PEDIDO APROVADO'), ('ENC', 'PEDIDO ENCAMINHADO'), ('NAT', 'PEDIDO NÃO ATENDIDO')], max_length=4)),
                ('link_issue', models.URLField(blank=True, max_length=300, null=True)),
                ('nivel_prioridade', models.CharField(choices=[('A', 'ALTO'), ('M', 'MÉDIO'), ('B', 'BAIXO')], max_length=1)),
                ('nota_prioridade', models.IntegerField()),
                ('formato_atendimento', models.CharField(blank=True, choices=[('IA', 'IMERSÃO AUTOMATIZA'), ('TV', 'TIME VOLANTE'), ('CM', 'CURSO MENTORIA'), ('CU', 'CURSO EAD'), ('PE', 'PROJETO EXTENSÃO'), ('ND', 'NÃO DEFINIDO')], max_length=2, null=True)),
                ('orgao_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.orgao')),
                ('usuario_id_apoio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_id_apoio', to=settings.AUTH_USER_MODEL)),
                ('usuario_id_principal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_id_principal', to=settings.AUTH_USER_MODEL)),
                ('projeto_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.projeto')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Indicador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateField(auto_now_add=True)),
                ('data_atualizacao', models.DateField(auto_now=True)),
                ('arrecadacao', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('horas_manuais_economizadas', models.IntegerField(blank=True, null=True)),
                ('servidores_reposicionados', models.IntegerField(blank=True, null=True)),
                ('horas_totais_economizadas', models.IntegerField(blank=True, null=True)),
                ('ganho_eficiencia', models.IntegerField(blank=True, null=True)),
                ('oportunidade_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.pedidoimersao')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EquipeProjeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateField(auto_now_add=True)),
                ('data_atualizacao', models.DateField(auto_now=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('projeto_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.projeto')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateField(auto_now_add=True)),
                ('data_atualizacao', models.DateField(auto_now=True)),
                ('projeto_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.projeto')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProjetoEstrategico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateField(auto_now_add=True)),
                ('data_atualizacao', models.DateField(auto_now=True)),
                ('nome', models.CharField(max_length=100)),
                ('data_fim', models.DateField(blank=True, null=True)),
                ('orgao_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.orgao')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='pedidoimersao',
            name='projeto_estrategico_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.projetoestrategico'),
        ),
        migrations.CreateModel(
            name='Robo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateField(auto_now_add=True)),
                ('data_atualizacao', models.DateField(auto_now=True)),
                ('nome', models.CharField(max_length=100)),
                ('tempo_execucao_robo', models.IntegerField(blank=True, null=True)),
                ('tempo_execucao_manual', models.IntegerField(blank=True, null=True)),
                ('fase', models.CharField(choices=[('NAOI', 'Não iniciado'), ('EXEC', 'Em execução'), ('CONC', 'Concluído')], max_length=4)),
                ('oportunidade_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.pedidoimersao')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PedidoManutencao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateField(auto_now_add=True)),
                ('data_atualizacao', models.DateField(auto_now=True)),
                ('data_fim', models.DateField(blank=True, null=True)),
                ('link_issue', models.URLField(max_length=300)),
                ('robo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.robo')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
