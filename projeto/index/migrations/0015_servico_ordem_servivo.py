# Generated by Django 5.0.1 on 2024-03-21 17:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0014_remove_servico_ordem_servico'),
    ]

    operations = [
        migrations.AddField(
            model_name='servico',
            name='ordem_servivo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='index.ordemservico'),
            preserve_default=False,
        ),
    ]