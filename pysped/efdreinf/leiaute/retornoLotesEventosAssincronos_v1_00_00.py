# -*- coding: utf-8 -*-
#
# PySPED - Python libraries to deal with Brazil's SPED Project
#
# Copyright (C) 2010-2012
# Copyright (C) Aristides Caldeira <aristides.caldeira at tauga.com.br>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Library General Public License as
# published by the Free Software Foundation, either version 2.1 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library General Public License for more details.
#
# You should have received a copy of the GNU Library General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# PySPED - Bibliotecas Python para o
#          SPED - Sistema Público de Escrituração Digital
#
# Copyright (C) 2010-2012
# Copyright (C) Aristides Caldeira <aristides.caldeira arroba tauga.com.br>
#
# Este programa é um software livre: você pode redistribuir e/ou modificar
# este programa sob os termos da licença GNU Library General Public License,
# publicada pela Free Software Foundation, em sua versão 2.1 ou, de acordo
# com sua opção, qualquer versão posterior.
#
# Este programa é distribuido na esperança de que venha a ser útil,
# porém SEM QUAISQUER GARANTIAS, nem mesmo a garantia implícita de
# COMERCIABILIDADE ou ADEQUAÇÃO A UMA FINALIDADE ESPECÍFICA. Veja a
# GNU Library General Public License para mais detalhes.
#
# Você deve ter recebido uma cópia da GNU Library General Public License
# juntamente com este programa. Caso esse não seja o caso, acesse:
# <http://www.gnu.org/licenses/>
#

from __future__ import (division, print_function, unicode_literals,
                        absolute_import)

import os

from pysped.efdreinf.leiaute import ESQUEMA_ATUAL_VERSAO_2 as ESQUEMA_ATUAL
from pysped.xml_sped import *

DIRNAME = os.path.dirname(__file__)

NAMESPACE_LOTE_EFDREINF = 'http://www.reinf.esocial.gov.br/schemas/retornoLoteEventosAssincrono/v1_00_00'
NAMESPACE_EVT_RET_EFDREINF = 'http://www.reinf.esocial.gov.br/schemas/evtRet/v2_01_02'
NAMESPACE_EVT_TOTAL_EFDREINF = 'http://www.reinf.esocial.gov.br/schemas/evtTotal/v2_01_02'
NAMESPACE_EVT_RET_CONS_EFDREINF = 'http://www.reinf.esocial.gov.br/schemas/evtRetCons/v2_01_02'
NAMESPACE_EVT_TOTAL_CONTRIB_EFDREINF = 'http://www.reinf.esocial.gov.br/schemas/evtTotalContrib/v2_01_02'


class DadosProcessamentoLote(XMLNFe):
    def __init__(self):
        super(DadosProcessamentoLote, self).__init__()
        self.versaoAplicativoProcessamentoLote = TagCaracter(nome='versaoAplicativoProcessamentoLote', tamanho=[1, 255], raiz='//Reinf/retornoLoteEventosAssincrono/dadosProcessamentoLote', namespace=NAMESPACE_LOTE_EFDREINF, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<dadosProcessamentoLote>'
        xml += self.versaoAplicativoProcessamentoLote.xml
        xml += '</dadosProcessamentoLote>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versaoAplicativoProcessamentoLote.xml = arquivo

    xml = property(get_xml, set_xml)


class DadosRegistroOcorrenciaLote(XMLNFe):
    def __init__(self):
        super(DadosRegistroOcorrenciaLote, self).__init__()
        self.dhRecepcao = TagCaracter(nome='dhRecepcao', tamanho=[1, 255], raiz='//Reinf/retornoLoteEventosAssincrono/dadosRecepcaoLote', namespace=NAMESPACE_LOTE_EFDREINF, namespace_obrigatorio=False)
        self.versaoAplicativoRecepcao = TagCaracter(nome='versaoAplicativoRecepcao', tamanho=[1, 255], raiz='//Reinf/retornoLoteEventosAssincrono/dadosRecepcaoLote', namespace=NAMESPACE_LOTE_EFDREINF, namespace_obrigatorio=False)
        self.protocoloEnvio = TagCaracter(nome='protocoloEnvio', tamanho=[1, 255], raiz='//Reinf/retornoLoteEventosAssincrono/dadosRecepcaoLote', namespace=NAMESPACE_LOTE_EFDREINF, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<dadosRecepcaoLote>'
        xml += self.dhRecepcao.xml
        xml += self.versaoAplicativoRecepcao.xml
        xml += self.protocoloEnvio.xml
        xml += '</dadosRecepcaoLote>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.dhRecepcao.xml = arquivo
            self.versaoAplicativoRecepcao.xml = arquivo
            self.protocoloEnvio.xml = arquivo

    xml = property(get_xml, set_xml)


class Status(XMLNFe):
    def __init__(self):
        super(Status, self).__init__()
        self.cdResposta = TagInteiro(nome='cdResposta', tamanho=[1, 1, 1], raiz='//Reinf/retornoLoteEventosAssincrono/status', namespace=NAMESPACE_LOTE_EFDREINF, namespace_obrigatorio=False)
        self.descResposta = TagCaracter(nome='descResposta', tamanho=[1, 255], raiz='//Reinf/retornoLoteEventosAssincrono/status', namespace=NAMESPACE_LOTE_EFDREINF, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<status>'
        xml += self.cdResposta.xml
        xml += self.descResposta.xml
        xml += '</status>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cdResposta.xml = arquivo
            self.descResposta.xml = arquivo

    xml = property(get_xml, set_xml)


class IdeContribuinte(XMLNFe):
    def __init__(self):
        super(IdeContribuinte, self).__init__()
        self.tpInsc = TagCaracter(nome='tpInsc', valor='1',
                                  raiz='//Reinf/retornoLoteEventosAssincrono/ideContribuinte',
                                  namespace=NAMESPACE_LOTE_EFDREINF,
                                  namespace_obrigatorio=False)
        self.nrInsc = TagCaracter(nome='nrInsc', tamanho=[8, 14],
                                  raiz='//Reinf/retornoLoteEventosAssincrono/ideContribuinte',
                                  namespace=NAMESPACE_LOTE_EFDREINF,
                                  namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideContribuinte>'
        xml += self.tpInsc.xml
        xml += self.nrInsc.xml
        xml += '</ideContribuinte>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpInsc.xml = arquivo
            self.nrInsc.xml = arquivo

    xml = property(get_xml, set_xml)


class Ocorrencias(XMLNFe):
    def __init__(self):
        super(Ocorrencias, self).__init__()
        self.tpOcorr = TagCaracter(nome='tpOcorr', tamanho=[1, 255], raiz='//regOcorrs', namespace=NAMESPACE_EVT_RET_EFDREINF, namespace_obrigatorio=False)
        self.localErroAviso = TagCaracter(nome='localErroAviso', tamanho=[1, 255], raiz='//regOcorrs', namespace=NAMESPACE_EVT_RET_EFDREINF, namespace_obrigatorio=False)
        self.codResp = TagCaracter(nome='codResp', tamanho=[1, 255], raiz='//regOcorrs', namespace=NAMESPACE_EVT_RET_EFDREINF, namespace_obrigatorio=False)
        self.dscResp = TagCaracter(nome='dscResp', tamanho=[1, 999], raiz='//regOcorrs', namespace=NAMESPACE_EVT_RET_EFDREINF, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<regOcorrs>'
        xml += self.tpOcorr.xml
        xml += self.localErroAviso.xml
        xml += self.codResp.xml
        xml += self.dscResp.xml
        xml += '</regOcorrs>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpOcorr.namespace = self.get_namespace()
            self.tpOcorr.xml = arquivo
            self.localErroAviso.namespace = self.get_namespace()
            self.localErroAviso.xml = arquivo
            self.codResp.namespace = self.get_namespace()
            self.codResp.xml = arquivo
            self.dscResp.namespace = self.get_namespace()
            self.dscResp.xml = arquivo

    def get_namespace(self):
        elem_list = []
        for elem in self._xml.iter():
            elem_list.append(elem.tag)

        namespace = ''

        if "evtTotal" in elem_list[4]:
            namespace = NAMESPACE_EVT_TOTAL_EFDREINF
        elif "evtRetCons" in elem_list[4]:
            namespace = NAMESPACE_EVT_RET_CONS_EFDREINF
        elif "evtTotalContrib" in elem_list[4]:
            namespace = NAMESPACE_EVT_TOTAL_CONTRIB_EFDREINF
        else:
            namespace = NAMESPACE_EVT_RET_EFDREINF

        return namespace

    xml = property(get_xml, set_xml)


class RetornoLoteEventoStatus(XMLNFe):
    def __init__(self):
        super(RetornoLoteEventoStatus, self).__init__()
        self.cdRetorno = TagCaracter(nome='cdRetorno', tamanho=[1, 255], raiz='//Reinf/evtRet/ideRecRetorno/ideStatus', namespace=NAMESPACE_EVT_RET_EFDREINF, namespace_obrigatorio=False)
        self.descRetorno = TagCaracter(nome='descRetorno', tamanho=[1, 255], raiz='//Reinf/evtRet/ideRecRetorno/ideStatus', namespace=NAMESPACE_EVT_RET_EFDREINF, namespace_obrigatorio=False)
        self.nrProtLote = TagCaracter(nome='nrProtLote', tamanho=[1, 255], raiz='//Reinf/evtRet/infoRecEv', namespace=NAMESPACE_EVT_RET_EFDREINF, namespace_obrigatorio=False)
        self.hash = TagCaracter(nome='hash', tamanho=[1, 255], raiz='//Reinf/evtRet/infoRecEv', namespace=NAMESPACE_EVT_RET_EFDREINF, namespace_obrigatorio=False)
        self.nrRecArqBase = TagCaracter(nome='nrRecArqBase', tamanho=[1, 255], raiz='//Reinf/evtRet/infoRecEv', namespace=NAMESPACE_EVT_RET_EFDREINF, namespace_obrigatorio=False)
        self.regOcorrs = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideRecRetorno>'
        xml += '<ideStatus>'
        xml += self.cdRetorno.xml
        xml += self.descRetorno.xml
        for ocorr in self.regOcorrs:
            xml += ocorr.xml
        xml += '<infoRecEv>'
        xml += self.nrProtLote.xml
        xml += self.hash.xml
        xml += self.nrRecArqBase.xml
        xml += '</infoRecEv>'
        xml += '</ideStatus>'
        xml += '</ideRecRetorno>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cdRetorno.namespace = self.get_namespace()
            self.cdRetorno.raiz = self.get_raiz_correta(self.cdRetorno.raiz)
            self.cdRetorno.xml = arquivo
            self.descRetorno.raiz = self.get_raiz_correta(self.descRetorno.raiz)
            self.descRetorno.namespace = self.get_namespace()
            self.descRetorno.xml = arquivo
            self.nrProtLote.raiz = self.get_raiz_correta('//Reinf/evtRet/infoRecEv')
            self.nrProtLote.namespace = self.get_namespace()
            self.nrProtLote.xml = arquivo
            self.hash.raiz = self.get_raiz_correta('//Reinf/evtRet/infoRecEv')
            self.hash.namespace = self.get_namespace()
            self.hash.xml = arquivo
            self.nrRecArqBase.raiz = self.get_raiz_correta('//Reinf/evtRet/infoRecEv')
            self.nrRecArqBase.namespace = self.get_namespace()
            self.nrRecArqBase.xml = arquivo
            self.regOcorrs = self.le_grupo(self.get_raiz_correta('//Reinf/evtRet/ideRecRetorno/ideStatus/regOcorrs'), Ocorrencias, namespace=self.get_namespace(), sigla_ns='res')

    def get_namespace(self):
        elem_list = []
        for elem in self._xml.iter():
            elem_list.append(elem.tag)

        namespace = ''

        if "evtTotalContrib" in elem_list[4]:
            namespace = NAMESPACE_EVT_TOTAL_CONTRIB_EFDREINF
        elif "evtRetCons" in elem_list[4]:
            namespace = NAMESPACE_EVT_RET_CONS_EFDREINF
        elif "evtTotal" in elem_list[4]:
            namespace = NAMESPACE_EVT_TOTAL_EFDREINF
        else:
            namespace = NAMESPACE_EVT_RET_EFDREINF

        return namespace

    def get_raiz_correta(self, raiz):
        namespace = self.get_namespace()
        if namespace == NAMESPACE_EVT_TOTAL_EFDREINF:
            raiz = raiz.replace('evtRet', 'evtTotal')
        elif namespace == NAMESPACE_EVT_TOTAL_CONTRIB_EFDREINF:
            raiz = raiz.replace('evtRet', 'evtTotalContrib')
        elif namespace == NAMESPACE_EVT_RET_CONS_EFDREINF:
            raiz = raiz.replace('evtRet', 'evtRetCons')

        return raiz

    xml = property(get_xml, set_xml)


class RetornoTotalizadorEvento(XMLNFe):
    def __init__(self):
        super(RetornoTotalizadorEvento, self).__init__()
        self.Id = TagCaracter(nome='evento', propriedade='Id', raiz='/', namespace=NAMESPACE_LOTE_EFDREINF, namespace_obrigatorio=False)
        self.ideStatus = RetornoLoteEventoStatus()
        self.nrRecArqBase = TagCaracter(nome='nrRecArqBase', raiz='//Reinf/evtRet/infoTotal', namespace=NAMESPACE_EVT_RET_EFDREINF, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.Id.xml
        xml += self.ideStatus.xml
        xml += self.nrRecArqBase.xml
        xml += '</evento>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml = arquivo
            self.nrRecArqBase.namespace = self.get_namespace()
            self.nrRecArqBase.raiz = self.get_raiz_correta(self.nrRecArqBase.raiz)
            self.nrRecArqBase.xml = arquivo
            self.ideStatus.xml = arquivo

    def get_namespace(self):
        elem_list = []
        for elem in self._xml.iter():
            elem_list.append(elem.tag)

        namespace = ''

        if "evtTotalContrib" in elem_list[4]:
            namespace = NAMESPACE_EVT_TOTAL_CONTRIB_EFDREINF
        elif "evtRetCons" in elem_list[4]:
            namespace = NAMESPACE_EVT_RET_CONS_EFDREINF
        elif "evtTotal" in elem_list[4]:
            namespace = NAMESPACE_EVT_TOTAL_EFDREINF
        else:
            namespace = NAMESPACE_EVT_RET_EFDREINF

        return namespace

    def get_raiz_correta(self, raiz):
        namespace = self.get_namespace()
        if namespace == NAMESPACE_EVT_TOTAL_EFDREINF:
            raiz = raiz.replace('evtRet', 'evtTotal')
        elif namespace == NAMESPACE_EVT_TOTAL_CONTRIB_EFDREINF:
            raiz = raiz.replace('evtRet/infoTotal', 'evtTotalContrib/infoTotalContrib')
        elif namespace == NAMESPACE_EVT_RET_CONS_EFDREINF:
            raiz = raiz.replace('evtRet/infoTotal', 'evtRetCons/infoCR_CNR')

        return raiz

    xml = property(get_xml, set_xml)


class RetornoLoteEventos(XMLNFe):
    def __init__(self):
        super(RetornoLoteEventos, self).__init__()
        self.ideContribuinte = IdeContribuinte()
        self.status = Status()
        self.dadosRegistroOcorrenciaLote = DadosRegistroOcorrenciaLote()
        self.dadosProcessamentoLote = DadosProcessamentoLote()
        self.cdRetorno = ''
        self.descRetorno = ''
        self.ocorrencias = []
        self.retornoEventos = []
        self.eventos = []
        self.status_code = ''
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'retornoLoteEventosAssincrono-v1_00_00.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<Reinf xmlns="' + NAMESPACE_LOTE_EFDREINF + '">'
        xml += '<retornoLoteEventosAssincrono>'
        xml += self.ideContribuinte.xml
        xml += self.status.xml
        xml += self.dadosRegistroOcorrenciaLote.xml
        xml += self.dadosProcessamentoLote.xml
        xml += '<retornoEventos>'
        if len(self.retornoEventos) >= 1:
            for r in self.retornoEventos:
                xml += r.xml
        xml += '</retornoEventos>'
        xml += '</retornoLoteEventosAssincrono>'
        xml += '</Reinf>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.ideContribuinte.xml = arquivo
            self.status.xml = arquivo
            self.dadosRegistroOcorrenciaLote.xml = arquivo
            self.dadosProcessamentoLote.xml = arquivo
            self.retornoEventos = self.le_grupo('//Reinf/retornoLoteEventosAssincrono/retornoEventos/evento', RetornoTotalizadorEvento, namespace=NAMESPACE_LOTE_EFDREINF)

    xml = property(get_xml, set_xml)
