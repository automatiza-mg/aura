# Generated by Django 5.0.7 on 2024-09-16 17:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0005_alter_pedidoimersao_nivel_prioridade_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='robo',
            name='sistema_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.sistema'),
        ),
    ]
