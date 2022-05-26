# -*- coding: utf-8 -*-

from django.urls import path
from . import views

app_name = 'compras'
urlpatterns = [
    # Orcamentos de compra
    # compras/orcamentocompra/adicionar/
    path(r'orcamentocompra/adicionar/$',
        views.AdicionarOrcamentoCompraView.as_view(), name='addorcamentocompraview'),
    # compras/orcamentocompra/listaorcamentocompra
    path(r'orcamentocompra/listaorcamentocompra/$',
        views.OrcamentoCompraListView.as_view(), name='listaorcamentocompraview'),
    # compras/orcamentocompra/editar/
    path(r'orcamentocompra/editar/(?P<pk>[0-9]+)/$',
        views.EditarOrcamentoCompraView.as_view(), name='editarorcamentocompraview'),
    # compras/orcamentocompra/listaorcamentocompra/vencidos/
    path(r'orcamentocompra/listaorcamentocompra/vencidos/$',
        views.OrcamentoCompraVencidosListView.as_view(), name='listaorcamentocompravencidosview'),
    # compras/orcamentocompra/listaorcamentocompra/hoje/
    path(r'orcamentocompra/listaorcamentocompra/hoje/$',
        views.OrcamentoCompraVencimentoHojeListView.as_view(), name='listaorcamentocomprahojeview'),

    # Pedidos de compra
    # compras/pedidocompra/adicionar/
    path(r'pedidocompra/adicionar/$',
        views.AdicionarPedidoCompraView.as_view(), name='addpedidocompraview'),
    # compras/pedidocompra/listapedidocompra
    path(r'pedidocompra/listapedidocompra/$',
        views.PedidoCompraListView.as_view(), name='listapedidocompraview'),
    # compras/pedidocompra/editar/
    path(r'pedidocompra/editar/(?P<pk>[0-9]+)/$',
        views.EditarPedidoCompraView.as_view(), name='editarpedidocompraview'),
    # compras/pedidocompra/listapedidocompra/atrasados/
    path(r'pedidocompra/listapedidocompra/atrasados/$',
        views.PedidoCompraAtrasadosListView.as_view(), name='listapedidocompraatrasadosview'),
    # compras/pedidocompra/listapedidocompra/hoje/
    path(r'pedidocompra/listapedidocompra/hoje/$',
        views.PedidoCompraEntregaHojeListView.as_view(), name='listapedidocomprahojeview'),

    # Request ajax
    path(r'infocompra/$', views.InfoCompra.as_view(), name='infocompra'),

    # Gerar pdf orcamento
    path(r'gerarpdforcamentocompra/(?P<pk>[0-9]+)/$',
        views.GerarPDFOrcamentoCompra.as_view(), name='gerarpdforcamentocompra'),
    # Gerar pdf pedido
    path(r'gerarpdfpedidocompra/(?P<pk>[0-9]+)/$',
        views.GerarPDFPedidoCompra.as_view(), name='gerarpdfpedidocompra'),
    # Gerar pedido a partir de um orçamento
    path(r'gerarpedidocompra/(?P<pk>[0-9]+)/$',
        views.GerarPedidoCompraView.as_view(), name='gerarpedidocompra'),
    # Copiar orcamento cancelado ou realizado
    path(r'copiarorcamentocompra/(?P<pk>[0-9]+)/$',
        views.GerarCopiaOrcamentoCompraView.as_view(), name='copiarorcamentocompra'),
    # Copiar pedido cancelado ou realizado
    path(r'copiarpedidocompra/(?P<pk>[0-9]+)/$',
        views.GerarCopiaPedidoCompraView.as_view(), name='copiarpedidocompra'),
    # Cancelar Pedido de compra
    path(r'cancelarpedidocompra/(?P<pk>[0-9]+)/$',
        views.CancelarPedidoCompraView.as_view(), name='cancelarpedidocompra'),
    # Cancelar Orcamento de compra
    path(r'cancelarorcamentocompra/(?P<pk>[0-9]+)/$',
        views.CancelarOrcamentoCompraView.as_view(), name='cancelarorcamentocompra'),
    # Receber Pedido de compra
    path(r'receberpedidocompra/(?P<pk>[0-9]+)/$',
        views.ReceberPedidoCompraView.as_view(), name='receberpedidocompra'),
]
