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

from builtins import str
import os
from pysped.xml_sped import *
from pysped.esocial.leiaute import ESQUEMA_ATUAL_VERSAO_2 as ESQUEMA_ATUAL

DIRNAME = os.path.dirname(__file__)

NAMESPACE_ESOCIAL = 'http://www.esocial.gov.br/schema/evt/evtTreiCap/v02_05_00'


class IdeProfResp(XMLNFe):
    def __init__(self):
        super(IdeProfResp, self).__init__()
        self.cpfProf = TagCaracter(nome='cpfProf', tamanho=[1, 11], raiz='//ideProfResp', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.nmProf = TagCaracter(nome='nmProf', tamanho=[1, 70], raiz='//ideProfResp', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.tpProf = TagInteiro(nome='tpProf', raiz='//ideProfResp', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.formProf = TagCaracter(nome='formProf', tamanho=[1, 255], raiz='//ideProfResp', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.codCBO = TagCaracter(nome='codCBO', tamanho=[1, 6], raiz='//ideProfResp', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nacProf = TagInteiro(nome='nacProf', raiz='//ideProfResp', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideProfResp>'
        xml += self.cpfProf.xml
        xml += self.nmProf.xml
        xml += self.tpProf.xml
        xml += self.formProf.xml
        xml += self.codCBO.xml
        xml += self.nacProf.xml
        xml += '</ideProfResp>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cpfProf.xml = arquivo
            self.nmProf.xml = arquivo
            self.tpProf.xml = arquivo
            self.formProf.xml = arquivo
            self.codCBO.xml = arquivo
            self.nacProf.xml = arquivo

    xml = property(get_xml, set_xml)


class InfoComplem(XMLNFe):
    def __init__(self):
        super(InfoComplem, self).__init__()
        self.dtTreiCap = TagData(nome='dtTreiCap', raiz='//infoComplem', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.durTreiCap = TagInteiro(nome='durTreiCap', raiz='//infoComplem', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=2)
        self.modTreiCap = TagInteiro(nome='modTreiCap', raiz='//infoComplem', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.tpTreiCap = TagInteiro(nome='tpTreiCap', raiz='//infoComplem', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ideProfResp = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoComplem>'
        xml += self.dtTreiCap.xml
        xml += self.durTreiCap.xml
        xml += self.modTreiCap.xml
        xml += self.tpTreiCap.xml
        for ide_prof_resp in self.ideProfResp:
            xml += ide_prof_resp.xml
        xml += '</infoComplem>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.dtTreiCap.xml = arquivo
            self.durTreiCap.xml = arquivo
            self.modTreiCap.xml = arquivo
            self.tpTreiCap.xml = arquivo
            self.ideProfResp.xml = self.le_grupo('//eSocial/evtTreiCap/TreiCap/infoComplem/ideProfResp', IdeProfResp, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class TreiCap(XMLNFe):
    def __init__(self):
        super(TreiCap, self).__init__()
        self.codTreiCap = TagCaracter(nome='codTreiCap', tamanho=[1, 4], raiz='//eSocial/evtTreiCap/TreiCap', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.obsTreiCap = TagCaracter(nome='obsTreiCap', tamanho=[1, 999], raiz='//eSocial/evtTreiCap/TreiCap', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.infoComplem = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<treiCap>'
        xml += self.codTreiCap.xml
        for obs in self.obsTreiCap:
            xml += obs.xml
        xml += '</treiCap>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.codTreiCap.xml = arquivo
            self.obsTreiCap.xml = arquivo
            self.infoComplem.xml = self.le_grupo('//eSocial/evtTreiCap/TreiCap/infoComplem', InfoComplem, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class IdeVinculo(XMLNFe):
    def __init__(self):
        super(IdeVinculo, self).__init__()
        self.cpfTrab = TagCaracter(nome='cpfTrab', tamanho=[1, 11], raiz='//eSocial/evtTreiCap/ideVinculo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nisTrab = TagCaracter(nome='nisTrab', tamanho=[1, 11], raiz='//eSocial/evtTreiCap/ideVinculo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.matricula = TagCaracter(nome='matricula', tamanho=[1, 30], raiz='//eSocial/evtTreiCap/ideVinculo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.codCateg = TagCaracter(nome='matricula', tamanho=[1, 30], raiz='//eSocial/evtTreiCap/ideVinculo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideVinculo>'
        xml += self.cpfTrab.xml
        xml += self.nisTrab.xml
        xml += self.matricula.xml
        xml += self.codCateg.xml
        xml += '</ideVinculo>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cpfTrab.xml = arquivo
            self.nisTrab.xml = arquivo
            self.matricula.xml = arquivo
            self.codCateg.xml = arquivo

    xml = property(get_xml, set_xml)


class IdeEmpregador(XMLNFe):
    def __init__(self):
        super(IdeEmpregador, self).__init__()
        self.tpInsc = TagCaracter(nome='tpInsc', raiz='//eSocial/evtTreiCap/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor='1')
        self.nrInsc = TagCaracter(nome='nrInsc', raiz='//eSocial/evtTreiCap/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideEmpregador>'
        xml += self.tpInsc.xml
        xml += self.nrInsc.xml
        xml += '</ideEmpregador>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpInsc.xml = arquivo
            self.nrInsc.xml = arquivo

    xml = property(get_xml, set_xml)


class IdeEvento(XMLNFe):
    def __init__(self):
        super(IdeEvento, self).__init__()
        self.tpAmb = TagInteiro(nome='tpAmb', raiz='//eSocial/evtTreiCap/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=2)
        self.procEmi = TagInteiro(nome='procEmi', raiz='//eSocial/evtTreiCap/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=1)
        self.verProc = TagCaracter(nome='verProc', raiz='//eSocial/evtTreiCap/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideEvento>'
        xml += self.tpAmb.xml
        xml += self.procEmi.xml
        xml += self.verProc.xml
        xml += '</ideEvento>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpAmb.xml = arquivo
            self.procEmi.xml = arquivo
            self.verProc.xml = arquivo

    xml = property(get_xml, set_xml)


class EvtTreiCap(XMLNFe):
    def __init__(self):
        super(EvtTreiCap, self).__init__()
        self.Id = TagCaracter(nome='evtTreiCap', propriedade='Id', raiz='//eSocial/evtTreiCap', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ideEvento = IdeEvento()
        self.ideEmpregador = IdeEmpregador()
        self.ideVinculo = IdeVinculo()
        self.treiCap = TreiCap()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.Id.xml
        xml += self.ideEvento.xml
        xml += self.ideEmpregador.xml
        xml += self.ideVinculo.xml
        xml += self.treiCap.xml
        xml += '</evtTreiCap>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml = arquivo
            self.ideEvento.xml = arquivo
            self.ideEmpregador.xml = arquivo
            self.ideVinculo.xml = arquivo
            self.treiCap.xml = arquivo

    xml = property(get_xml, set_xml)


class S2245(XMLNFe):
    def __init__(self):
        super(S2245, self).__init__()
        self.evtTreiCap = EvtTreiCap()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'evtTreiCap.xsd'
        self.id_evento = ''
        self.tpInsc = ''
        self.nrInsc = ''
        # self.Signature = Signature()
        self.evento = self.evtTabHorTur
        self.xml_assinado = ''

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        #xml += ABERTURA
        xml += '<eSocial xmlns="' + NAMESPACE_ESOCIAL + '">'
        xml += self.evtTreiCap.xml

        #
        # Define a URI a ser assinada
        #
        # self.Signature.URI = '#' + self.evtInfoEmpregador.Id.valor
        # xml += self.Signature.xml
        xml += '</eSocial>'

        # Define o método de assinatura
        # self.Signature.metodo = 'sha256'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.evtTreiCap.xml = arquivo
            # self.Signature.xml = self._le_noh('//eSocial/sig:Signature')

    def gera_id_evento(self, data_hora, sequencia=False):
        #A identificação única do evento (Id) é composta por 36 caracteres, conforme o que segue: IDTNNNNNNNNNNNNNNAAAAMMDDHHMMSSQQQQQ
        #ID - Texto Fixo "ID";
        #T - Tipo de Inscrição do Empregador (1 - CNPJ; 2 - CPF);
        #NNNNNNNNNNNNNN - Número do CNPJ ou CPF do empregador - Completar com
        #zeros à direita. No caso de pessoas jurídicas, o CNPJ informado deve conter 8 ou 14
        #posições de acordo com o enquadramento do contribuinte para preenchimento do campo
        #{ideEmpregador/nrInsc} do evento S-1000, completando-se com zeros à direita, se
        #necessário.
        #AAAAMMDD - Ano, mês e dia da geração do evento;
        #HHMMSS - Hora, minuto e segundo da geração do evento;
        #QQQQQ - Número sequencial da chave. Incrementar somente quando ocorrer geração de
        #eventos na mesma data/hora, completando com zeros à esquerda.
        #OBS.: No caso de pessoas jurídicas, o CNPJ informado deverá conter 8 ou 14 posições de
        #acordo com o enquadramento do contribuinte para preenchimento do campo {ideEmpregador/nrInsc} do evento S-1000, completando-se com zeros à direita, se necessário.

        if not sequencia:
            sequencia=1

        id_evento = 'ID'
        id_evento += self.tpInsc
        id_evento += self.nrInsc[0:8] + '000000'
        id_evento += data_hora
        id_evento += str(sequencia).zfill(5)

        # Define o Id
        #
        self.evtTabHorTur.Id.valor = id_evento
        self.id_evento = id_evento

    xml = property(get_xml, set_xml)
