# Generated by Django 4.0.4 on 2022-04-19 04:03

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('estoque', '0001_initial'),
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CondicaoPagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255)),
                ('forma', models.CharField(choices=[('01', 'Dinheiro'), ('02', 'Cheque'), ('03', 'Cartão de Crédito'), ('04', 'Cartão de Débito'), ('05', 'Crédito Loja'), ('10', 'Vale Alimentação'), ('11', 'Vale Refeição'), ('12', 'Vale Presente'), ('13', 'Vale Combustível'), ('99', 'Outros')], default='99', max_length=2)),
                ('n_parcelas', models.IntegerField()),
                ('dias_recorrencia', models.IntegerField(default=0)),
                ('parcela_inicial', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Condição de Pagamento',
            },
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ind_final', models.BooleanField(default=False)),
                ('mod_frete', models.CharField(choices=[('0', 'Por conta do emitente'), ('1', 'Por conta do destinatário/remetente'), ('2', 'Por conta de terceiros'), ('9', 'Sem frete')], default='9', max_length=1)),
                ('movimentar_estoque', models.BooleanField(default=True)),
                ('data_emissao', models.DateField(blank=True, null=True)),
                ('vendedor', models.CharField(blank=True, max_length=255, null=True)),
                ('valor_total', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=13, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('tipo_desconto', models.CharField(choices=[('0', 'Valor'), ('1', 'Percentual')], default='0', max_length=1)),
                ('desconto', models.DecimalField(decimal_places=4, default=Decimal('0.00'), max_digits=15, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('despesas', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=13, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('frete', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=13, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('seguro', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=13, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('impostos', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=13, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('observacoes', models.CharField(blank=True, max_length=1055, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='venda_cliente', to='cadastro.cliente')),
                ('cond_pagamento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='venda_pagamento', to='vendas.condicaopagamento')),
                ('local_orig', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='venda_local_estoque', to='estoque.localestoque')),
                ('transportadora', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='venda_transportadora', to='cadastro.transportadora')),
                ('veiculo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='venda_veiculo', to='cadastro.veiculo')),
            ],
        ),
        migrations.CreateModel(
            name='OrcamentoVenda',
            fields=[
                ('venda_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='vendas.venda')),
                ('data_vencimento', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('0', 'Aberto'), ('1', 'Baixado'), ('2', 'Cancelado')], default='0', max_length=1)),
            ],
            options={
                'verbose_name': 'Orçamento de Venda',
            },
            bases=('vendas.venda',),
        ),
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indice_parcela', models.IntegerField()),
                ('vencimento', models.DateField()),
                ('valor_parcela', models.DecimalField(decimal_places=2, max_digits=13, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('venda_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parcela_pagamento', to='vendas.venda')),
            ],
        ),
        migrations.CreateModel(
            name='ItensVenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.DecimalField(blank=True, decimal_places=2, max_digits=13, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('valor_unit', models.DecimalField(blank=True, decimal_places=2, max_digits=13, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('tipo_desconto', models.CharField(blank=True, choices=[('0', 'Valor'), ('1', 'Percentual')], max_length=1, null=True)),
                ('desconto', models.DecimalField(blank=True, decimal_places=2, max_digits=13, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('subtotal', models.DecimalField(blank=True, decimal_places=2, max_digits=13, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('inf_ad_prod', models.CharField(blank=True, max_length=500, null=True)),
                ('valor_rateio_frete', models.DecimalField(blank=True, decimal_places=2, max_digits=13, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('valor_rateio_despesas', models.DecimalField(blank=True, decimal_places=2, max_digits=13, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('valor_rateio_seguro', models.DecimalField(blank=True, decimal_places=2, max_digits=13, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('vbc_icms', models.DecimalField(blank=True, decimal_places=2, max_digits=13, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('vbc_icms_st', models.DecimalField(blank=True, decimal_places=2, max_digits=13, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('vbc_ipi', models.DecimalField(blank=True, decimal_places=2, max_digits=13, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('vicms', models.DecimalField(blank=True, decimal_places=2, max_digits=13, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('vicms_st', models.DecimalField(blank=True, decimal_places=2, max_digits=13, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('vipi', models.DecimalField(blank=True, decimal_places=2, max_digits=13, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('vfcp', models.DecimalField(blank=True, decimal_places=2, max_digits=13, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('vicmsufdest', models.DecimalField(blank=True, decimal_places=2, max_digits=13, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('vicmsufremet', models.DecimalField(blank=True, decimal_places=2, max_digits=13, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('vicms_deson', models.DecimalField(blank=True, decimal_places=2, max_digits=13, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('p_icms', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('p_icmsst', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('p_ipi', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('vq_bcpis', models.DecimalField(blank=True, decimal_places=2, max_digits=13, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('vq_bccofins', models.DecimalField(blank=True, decimal_places=2, max_digits=13, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('vpis', models.DecimalField(blank=True, decimal_places=2, max_digits=13, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('vcofins', models.DecimalField(blank=True, decimal_places=2, max_digits=13, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('icms_incluido_preco', models.BooleanField(default=False)),
                ('icmsst_incluido_preco', models.BooleanField(default=False)),
                ('ipi_incluido_preco', models.BooleanField(default=False)),
                ('incluir_bc_icms', models.BooleanField(default=False)),
                ('incluir_bc_icmsst', models.BooleanField(default=False)),
                ('auto_calcular_impostos', models.BooleanField(default=True)),
                ('produto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='venda_produto', to='cadastro.produto')),
                ('venda_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens_venda', to='vendas.venda')),
            ],
        ),
        migrations.CreateModel(
            name='PedidoVenda',
            fields=[
                ('venda_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='vendas.venda')),
                ('data_entrega', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('0', 'Aberto'), ('1', 'Faturado'), ('2', 'Cancelado'), ('3', 'Importado por XML')], default='0', max_length=1)),
                ('orcamento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orcamento_pedido', to='vendas.orcamentovenda')),
            ],
            options={
                'verbose_name': 'Pedido de Venda',
                'permissions': (('faturar_pedidovenda', 'Pode faturar Pedidos de Venda'),),
            },
            bases=('vendas.venda',),
        ),
    ]
