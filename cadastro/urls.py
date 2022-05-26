# -*- coding: utf-8 -*-

from django.urls import path
from . import views

app_name = 'cadastro'
urlpatterns = [
    # Empresa
    # cadastro/empresa/adicionar/
    path('empresa/adicionar/',
        views.AdicionarEmpresaView.as_view(), name='addempresaview'),
    # cadastro/empresa/listaempresas
    path('empresa/listaempresas/',
        views.EmpresasListView.as_view(), name='listaempresasview'),
    # cadastro/empresa/editar/
    path('empresa/editar/(?P<pk>[0-9]+)/',
        views.EditarEmpresaView.as_view(), name='editarempresaview'),

    # Cliente
    # cadastro/cliente/adicionar/
    path('cliente/adicionar/',
        views.AdicionarClienteView.as_view(), name='addclienteview'),
    # cadastro/cliente/listaclientes
    path('cliente/listaclientes/',
        views.ClientesListView.as_view(), name='listaclientesview'),
    # cadastro/cliente/editar/
    path('cliente/editar/(?P<pk>[0-9]+)/',
        views.EditarClienteView.as_view(), name='editarclienteview'),

    # Fornecedor
    # cadastro/fornecedor/adicionar/
    path('fornecedor/adicionar/',
        views.AdicionarFornecedorView.as_view(), name='addfornecedorview'),
    # cadastro/fornecedor/listafornecedores
    path('fornecedor/listafornecedores/',
        views.FornecedoresListView.as_view(), name='listafornecedoresview'),
    # cadastro/fornecedor/editar/
    path('fornecedor/editar/(?P<pk>[0-9]+)/',
        views.EditarFornecedorView.as_view(), name='editarfornecedorview'),

    # Transportadora
    # cadastro/transportadora/adicionar/
    path(r'transportadora/adicionar/$',
        views.AdicionarTransportadoraView.as_view(), name='addtransportadoraview'),
    # cadastro/transportadora/listatransportadoras
    path(r'transportadora/listatransportadoras/$',
        views.TransportadorasListView.as_view(), name='listatransportadorasview'),
    # cadastro/transportadora/editar/
    path(r'transportadora/editar/(?P<pk>[0-9]+)/$',
        views.EditarTransportadoraView.as_view(), name='editartransportadoraview'),

    # Produto
    # cadastro/produto/adicionar/
    path(r'produto/adicionar/$',
        views.AdicionarProdutoView.as_view(), name='addprodutoview'),
    # cadastro/produto/listaprodutos
    path(r'produto/listaprodutos/$',
        views.ProdutosListView.as_view(), name='listaprodutosview'),
    # cadastro/produto/listaprodutos/baixoestoque
    path(r'produto/listaprodutos/baixoestoque/$',
        views.ProdutosBaixoEstoqueListView.as_view(), name='listaprodutosbaixoestoqueview'),
    # cadastro/produto/editar/
    path(r'produto/editar/(?P<pk>[0-9]+)/$',
        views.EditarProdutoView.as_view(), name='editarprodutoview'),

    # Outros
    # Categorias
    # cadastro/outros/adicionarcategoria/
    path(r'outros/adicionarcategoria/$',
        views.AdicionarCategoriaView.as_view(), name='addcategoriaview'),
    # cadastro/outros/listacategorias/
    path(r'outros/listacategorias/$',
        views.CategoriasListView.as_view(), name='listacategoriasview'),
    # cadastro/outros/editarcategoria/
    path(r'outros/editarcategoria/(?P<pk>[0-9]+)/$',
        views.EditarCategoriaView.as_view(), name='editarcategoriaview'),

    # Unidades
    # cadastro/outros/adicionarunidade/
    path(r'outros/adicionarunidade/$',
        views.AdicionarUnidadeView.as_view(), name='addunidadeview'),
    # cadastro/outros/listaunidades/
    path(r'outros/listaunidades/$',
        views.UnidadesListView.as_view(), name='listaunidadesview'),
    # cadastro/outros/editarcunidade/
    path(r'outros/editarunidade/(?P<pk>[0-9]+)/$',
        views.EditarUnidadeView.as_view(), name='editarunidadeview'),

    # Marcas
    # cadastro/outros/adicionarmarca/
    path(r'outros/adicionarmarca/$',
        views.AdicionarMarcaView.as_view(), name='addmarcaview'),
    # cadastro/outros/listamarcas/
    path(r'outros/listamarcas/$',
        views.MarcasListView.as_view(), name='listamarcasview'),
    # cadastro/outros/editarmarca/
    path(r'outros/editarmarca/(?P<pk>[0-9]+)/$',
        views.EditarMarcaView.as_view(), name='editarmarcaview'),

    # Informacoes de dada empresa (Ajax request)
    path(r'infoempresa/$', views.InfoEmpresa.as_view(), name='infoempresa'),
    path(r'infofornecedor/$', views.InfoFornecedor.as_view(), name='infofornecedor'),
    path(r'infocliente/$', views.InfoCliente.as_view(), name='infocliente'),
    path(r'infotransportadora/$', views.InfoTransportadora.as_view(),
        name='infotransportadora'),
    path(r'infoproduto/$', views.InfoProduto.as_view(), name='infoproduto'),
]
