# Generated by Django 4.0.4 on 2022-04-19 04:03

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovimentoCaixa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_movimento', models.DateField(blank=True, null=True)),
                ('saldo_inicial', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=13)),
                ('saldo_final', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=13)),
                ('entradas', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=13, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('saidas', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=13, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
            ],
            options={
                'verbose_name': 'Movimento de Caixa',
                'permissions': (('acesso_fluxodecaixa', 'Pode acessar o Fluxo de Caixa'),),
            },
        ),
        migrations.CreateModel(
            name='PlanoContasGrupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=6)),
                ('tipo_grupo', models.CharField(choices=[('0', 'Entrada'), ('1', 'Saída')], max_length=1)),
                ('descricao', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Grupo do Plano de Contas',
            },
        ),
        migrations.CreateModel(
            name='Lancamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_vencimento', models.DateField(blank=True, null=True)),
                ('data_pagamento', models.DateField(blank=True, null=True)),
                ('descricao', models.CharField(max_length=255)),
                ('valor_total', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=13, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('abatimento', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=13, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('juros', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=13, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('valor_liquido', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=13, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('movimentar_caixa', models.BooleanField(default=True)),
                ('conta_corrente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='conta_corrente_conta', to='cadastro.banco')),
                ('movimento_caixa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='movimento_caixa_lancamento', to='financeiro.movimentocaixa')),
            ],
            options={
                'verbose_name': 'Lançamento',
            },
        ),
        migrations.CreateModel(
            name='Saida',
            fields=[
                ('lancamento_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='financeiro.lancamento')),
                ('status', models.CharField(choices=[('0', 'Paga'), ('1', 'A pagar'), ('2', 'Atrasada')], default='1', max_length=1)),
                ('fornecedor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='conta_fornecedor', to='cadastro.fornecedor')),
                ('grupo_plano', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='grupo_plano_pagamento', to='financeiro.planocontasgrupo')),
            ],
            bases=('financeiro.lancamento',),
        ),
        migrations.CreateModel(
            name='PlanoContasSubgrupo',
            fields=[
                ('planocontasgrupo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='financeiro.planocontasgrupo')),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subgrupos', to='financeiro.planocontasgrupo')),
            ],
            bases=('financeiro.planocontasgrupo',),
        ),
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('lancamento_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='financeiro.lancamento')),
                ('status', models.CharField(choices=[('0', 'Recebida'), ('1', 'A receber'), ('2', 'Atrasada')], default='1', max_length=1)),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='conta_cliente', to='cadastro.cliente')),
                ('grupo_plano', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='grupo_plano_recebimento', to='financeiro.planocontasgrupo')),
            ],
            bases=('financeiro.lancamento',),
        ),
    ]
