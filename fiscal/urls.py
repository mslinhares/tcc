# -*- coding: utf-8 -*-

from django.urls import path
from . import views

app_name = 'fiscal'
urlpatterns = [
    # Nota fiscal saida
    # fiscal/notafiscal/saida/adicionar/
    path(r'notafiscal/saida/adicionar/$',
        views.AdicionarNotaFiscalSaidaView.as_view(), name='addnotafiscalsaidaview'),
    # fiscal/notafiscal/saida/listanotafiscal
    path(r'notafiscal/saida/listanotafiscal/$',
        views.NotaFiscalSaidaListView.as_view(), name='listanotafiscalsaidaview'),
    # fiscal/notafiscal/saida/editar/
    path(r'notafiscal/saida/editar/(?P<pk>[0-9]+)/$', views.EditarNotaFiscalSaidaView.as_view(
    ), name='editarnotafiscalsaidaview'),
    # fiscal/notafiscal/saida/importar/
    path(r'notafiscal/saida/importar/$',
        views.ImportarNotaSaidaView.as_view(), name='importarnotafiscalsaida'),
    # fiscal/notafiscal/saida/gerar/
    path(r'notafiscal/saida/gerar/(?P<pk>[0-9]+)/$',
        views.GerarNotaFiscalSaidaView.as_view(), name='gerarnotafiscalsaida'),

    # Nota fiscal entrada
    # fiscal/notafiscal/entrada/listanotafiscal
    path(r'notafiscal/entrada/listanotafiscal/$',
        views.NotaFiscalEntradaListView.as_view(), name='listanotafiscalentradaview'),
    # fiscal/notafiscal/entrada/editar/
    path(r'notafiscal/entrada/editar/(?P<pk>[0-9]+)/$', views.EditarNotaFiscalEntradaView.as_view(
    ), name='editarnotafiscalentradaview'),
    # fiscal/notafiscal/entrada/importar/
    path(r'notafiscal/entrada/importar/$',
        views.ImportarNotaEntradaView.as_view(), name='importarnotafiscalentrada'),

    # Configuracao NF-e
    path(r'notafiscal/configuracaonotafiscal/$',
        views.ConfiguracaoNotaFiscalView.as_view(), name='configuracaonotafiscal'),

    # Natureza operacao
    # fiscal/naturezaoperacao/adicionar/
    path(r'naturezaoperacao/adicionar/$',
        views.AdicionarNaturezaOperacaoView.as_view(), name='addnaturezaoperacaoview'),
    # fiscal/naturezaoperacao/listanaturezaoperacao
    path(r'naturezaoperacao/listanaturezaoperacao/$',
        views.NaturezaOperacaoListView.as_view(), name='listanaturezaoperacaoview'),
    # fiscal/naturezaoperacao/editar/
    path(r'naturezaoperacao/editar/(?P<pk>[0-9]+)/$', views.EditarNaturezaOperacaoView.as_view(
    ), name='editarnaturezaoperacaoview'),

    # Grupo fiscal
    # fiscal/grupofiscal/adicionar/
    path(r'grupofiscal/adicionar/$',
        views.AdicionarGrupoFiscalView.as_view(), name='addgrupofiscalview'),
    # fiscal/grupofiscal/listagrupofiscalview
    path(r'grupofiscal/listagrupofiscal/$',
        views.GrupoFiscalListView.as_view(), name='listagrupofiscalview'),
    # fiscal/grupofiscal/editar/
    path(r'grupofiscal/editar/(?P<pk>[0-9]+)/$',
        views.EditarGrupoFiscalView.as_view(), name='editargrupofiscalview'),

    # Acoes Nota Fiscal
    # Validar XML nota
    path(r'notafiscal/validar/(?P<pk>[0-9]+)/$',
        views.ValidarNotaView.as_view(), name='validarnotafiscal'),
    # fiscal/notafiscal/emitir/
    path(r'notafiscal/emitir/(?P<pk>[0-9]+)/$',
        views.EmitirNotaView.as_view(), name='emitirnotafiscal'),
    # Clonar nota
    path(r'notafiscal/copiar/(?P<pk>[0-9]+)/$',
        views.GerarCopiaNotaView.as_view(), name='copiarnotafiscal'),
    # Cancelar nota
    path(r'notafiscal/cancelar/(?P<pk>[0-9]+)/$',
        views.CancelarNotaView.as_view(), name='cancelarnotafiscal'),
    # Gerar DANFE
    path(r'notafiscal/gerardanfe/(?P<pk>[0-9]+)/$',
        views.GerarDanfeView.as_view(), name='gerardanfe'),
    # Gerar DANFCE
    path(r'notafiscal/gerardanfce/(?P<pk>[0-9]+)/$',
        views.GerarDanfceView.as_view(), name='gerardanfce'),

    # Comunicacao SEFAZ
    # Consultar cadastro
    path(r'notafiscal/consultarcadastro/$',
        views.ConsultarCadastroView.as_view(), name='consultarcadastro'),
    # Inutilizar notas
    path(r'notafiscal/inutilizarnotas/$',
        views.InutilizarNotasView.as_view(), name='inutilizarnotas'),
    # Consultar nota
    path(r'notafiscal/consultarnota/$',
        views.ConsultarNotaView.as_view(), name='consultarnota'),
    path(r'^notafiscal/consultarnota/(?P<pk>[0-9]+)/$',
        views.ConsultarNotaView.as_view(), name='consultarnota'),
    # Baixar nota
    path(r'notafiscal/baixarnota/$',
        views.BaixarNotaView.as_view(), name='baixarnota'),
    path(r'^notafiscal/baixarnota/(?P<pk>[0-9]+)/$',
        views.BaixarNotaView.as_view(), name='baixarnota'),
    # Manifestacao destinatario
    path(r'notafiscal/manifestacaodestinatario/$',
        views.ManifestacaoDestinatarioView.as_view(), name='manifestacaodestinatario'),
]
