# Generated by Django 5.1.1 on 2024-09-22 23:30

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exames', '0003_pedidosexames'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PedidosExames',
            new_name='PedidosExame',
        ),
        migrations.RenameModel(
            old_name='SolicitacaoExames',
            new_name='SolicitacaoExame',
        ),
        migrations.RenameModel(
            old_name='TiposExames',
            new_name='TiposExame',
        ),
    ]
