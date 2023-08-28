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

NAMESPACE_ESOCIAL = 'http://www.esocial.gov.br/schema/evt/evtContProc/v_S_01_01_00'


class InfoCRIRRF(XMLNFe):
    def __init__(self):
        super(InfoCRIRRF, self).__init__()
        self.tpCR = TagInteiro(nome='tpCR', raiz='//infoCRIRRF', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrCR = TagDecimal(nome='vrCR', tamanho=[1, 14, 2], raiz='//infoCRIRRF', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoCRIRRF>'
        xml += self.tpCR.xml
        xml += self.vrCR.xml
        xml += '</infoCRIRRF>'

        return xml


class InfoCRContrib(XMLNFe):
    def __init__(self):
        super(InfoCRContrib, self).__init__()
        self.tpCR = TagInteiro(nome='tpCR', raiz='//infoCRContrib', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrCR = TagDecimal(nome='vrCR', tamanho=[1, 14, 2], raiz='//infoCRContrib', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoCRContrib>'
        xml += self.tpCR.xml
        xml += self.vrCR.xml
        xml += '</infoCRContrib>'

        return xml


class CalcTrib(XMLNFe):
    def __init__(self):
        super(CalcTrib, self).__init__()
        self.perRef = TagCaracter(nome='perRef', raiz='//calcTrib', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrBcCpMensal = TagDecimal(nome='vrBcCpMensal', tamanho=[1, 14, 2], raiz='//calcTrib', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrBcCp13 = TagDecimal(nome='vrBcCp13', tamanho=[1, 14, 2], raiz='//calcTrib', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrRendIRRF = TagDecimal(nome='vrRendIRRF', tamanho=[1, 14, 2], raiz='//calcTrib', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrRendIRRF13 = TagDecimal(nome='vrRendIRRF13', tamanho=[1, 14, 2], raiz='//calcTrib', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.infoCRContrib = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<calcTrib>'
        xml += self.perRef.xml
        xml += self.vrBcCpMensal.xml
        xml += self.vrBcCp13.xml
        xml += self.vrRendIRRF.xml
        xml += self.vrRendIRRF13.xml
        for info_cr_contrib in self.infoCRContrib:
            xml += info_cr_contrib.xml
        xml += '</calcTrib>'

        return xml


class IdeTrab(XMLNFe):
    def __init__(self):
        super(IdeTrab, self).__init__()
        self.cpfTrab = TagCaracter(nome='cpfTrab', raiz='//ideTrab', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.calcTrib = []
        self.infoCRIRRF = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideTrab>'
        xml += self.cpfTrab.xml
        for calc_trib in self.calcTrib:
            xml += calc_trib.xml
        for info_cr_irrf in self.infoCRIRRF:
            xml += info_cr_irrf.xml
        xml += '</ideTrab>'

        return xml


class IdeProc(XMLNFe):
    def __init__(self):
        super(IdeProc, self).__init__()
        self.nrProcTrab = TagCaracter(nome='nrProcTrab', raiz='//ideProc', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.perApurPgto = TagCaracter(nome='perApurPgto', raiz='//ideProc', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.obs = TagCaracter(nome='obs', raiz='//ideProc', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideProc>'
        xml += self.nrProcTrab.xml
        xml += self.perApurPgto.xml
        xml += self.obs.xml
        xml += '</ideProc>'

        return xml



class IdeEmpregador(XMLNFe):
    def __init__(self):
        super(IdeEmpregador, self).__init__()
        self.tpInsc = TagCaracter(nome='tpInsc', raiz='//eSocial/evtContProc/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor='1')
        self.nrInsc = TagCaracter(nome='nrInsc', raiz='//eSocial/evtContProc/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

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
        self.indRetif = TagInteiro( nome='indRetif', raiz='//eSocial/evtContProc/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=1)
        self.nrRecibo = TagCaracter(nome='nrRecibo', raiz='//eSocial/evtContProc/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.tpAmb    = TagInteiro( nome='tpAmb'   , raiz='//eSocial/evtContProc/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=2)
        self.procEmi  = TagInteiro( nome='procEmi' , raiz='//eSocial/evtContProc/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=1)
        self.verProc  = TagCaracter(nome='verProc' , raiz='//eSocial/evtContProc/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideEvento>'
        xml += self.indRetif.xml
        xml += self.nrRecibo.xml
        xml += self.tpAmb.xml
        xml += self.procEmi.xml
        xml += self.verProc.xml
        xml += '</ideEvento>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.indRetif.xml = arquivo
            self.nrRecibo.xml = arquivo
            self.tpAmb.xml = arquivo
            self.procEmi.xml = arquivo
            self.verProc.xml = arquivo

    xml = property(get_xml, set_xml)


class evtContProc(XMLNFe):
    def __init__(self):
        super(evtContProc, self).__init__()
        self.Id = TagCaracter(nome='evtContProc', propriedade='Id', raiz='//eSocial/evtContProc', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ideEvento = IdeEvento()
        self.ideEmpregador = IdeEmpregador()
        self.ideProc = IdeProc()
        self.ideTrab = IdeTrab()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.Id.xml
        xml += self.ideEvento.xml
        xml += self.ideEmpregador.xml
        xml += self.ideProc.xml
        xml += self.ideTrab.xml
        xml += '</evtContProc>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml = arquivo
            self.ideEvento.xml = arquivo
            self.ideEmpregador.xml = arquivo
            self.infoProcesso.xml = arquivo

    xml = property(get_xml, set_xml)


class S2501(XMLNFe):
    def __init__(self):
        super(S2501, self).__init__()
        self.evtContProc = evtContProc()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'evtContProc.xsd'
        self.id_evento = ''
        self.tpInsc = ''
        self.nrInsc = ''
        # self.Signature = Signature()
        self.evento = self.evtContProc
        self.xml_assinado = ''

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        #xml += ABERTURA
        xml += '<eSocial xmlns="' + NAMESPACE_ESOCIAL + '">'
        xml += self.evtContProc.xml

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
            self.evtContProc.xml = arquivo
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
        self.evtContProc.Id.valor = id_evento
        self.id_evento = id_evento

    xml = property(get_xml, set_xml)
