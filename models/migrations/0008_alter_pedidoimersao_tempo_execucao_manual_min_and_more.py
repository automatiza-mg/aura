# Generated by Django 5.0.7 on 2024-09-17 19:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0007_rename_tempo_execucao_manual_robo_tempo_execucao_manual_min_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidoimersao',
            name='tempo_execucao_manual_min',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='robo',
            name='tempo_execucao_manual_min',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
    ]
