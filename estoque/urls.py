# -*- coding: utf-8 -*-

from django.urls import path
from . import views

app_name = 'estoque'
urlpatterns = [
    # Consulta de estoque
    # estoque/consultaestoque/
    path(r'consultaestoque/$', views.ConsultaEstoqueView.as_view(),
        name='consultaestoqueview'),

    # Local de estoque
    # estoque/local/adicionar/
    path(r'local/saida/adicionar/$',
        views.AdicionarLocalEstoqueView.as_view(), name='addlocalview'),
    # estoque/local/listalocal
    path(r'local/listalocal/$', views.LocalEstoqueListView.as_view(),
        name='listalocalview'),
    # estoque/local/editar/
    path(r'local/editar/(?P<pk>[0-9]+)/$',
        views.EditarLocalEstoqueView.as_view(), name='editarlocalview'),

    # Movimento de estoque
    # Lista todos movimentos
    path(r'movimentos/$', views.MovimentoEstoqueListView.as_view(),
        name='listamovimentoestoqueview'),

    # EntradaEstoque
    # estoque/movimento/adicionarentrada/
    path(r'movimento/adicionarentrada/$',
        views.AdicionarEntradaEstoqueView.as_view(), name='addentradaestoqueview'),
    # estoque/movimento/listaentradas/
    path(r'movimento/listaentradas/$', views.EntradaEstoqueListView.as_view(),
        name='listaentradasestoqueview'),
    # estoque/movimento/editarentrada/
    path(r'movimento/editarentrada/(?P<pk>[0-9]+)/$', views.DetalharEntradaEstoqueView.as_view(
    ), name='detalharentradaestoqueview'),

    # SaidaEstoque
    # estoque/movimento/adicionarsaida/
    path(r'movimento/adicionarsaida/$',
        views.AdicionarSaidaEstoqueView.as_view(), name='addsaidaestoqueview'),
    # estoque/movimento/listasaidas/
    path(r'movimento/listasaidas/$', views.SaidaEstoqueListView.as_view(),
        name='listasaidasestoqueview'),
    # estoque/movimento/editarsaida/
    path(r'movimento/editarsaida/(?P<pk>[0-9]+)/$',
        views.DetalharSaidaEstoqueView.as_view(), name='detalharsaidaestoqueview'),

    # TransferenciaEstoque
    # estoque/movimento/adicionartransferencia/
    path(r'movimento/adicionartransferencia/$',
        views.AdicionarTransferenciaEstoqueView.as_view(), name='addtransferenciaestoqueview'),
    # estoque/movimento/listatransferencias/
    path(r'movimento/listatransferencias/$', views.TransferenciaEstoqueListView.as_view(),
        name='listatransferenciasestoqueview'),
    # estoque/movimento/editartransferencia/
    path(r'movimento/editartransferencia/(?P<pk>[0-9]+)/$', views.DetalharTransferenciaEstoqueView.as_view(
    ), name='detalhartransferenciaestoqueview'),
]
