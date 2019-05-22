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

NAMESPACE_ESOCIAL = 'http://www.esocial.gov.br/schema/evt/evtMonit/v02_05_00'


class RespMonit(XMLNFe):
    def __init__(self):
        super(RespMonit, self).__init__()
        self.cpfResp = TagCaracter(nome='cpfResp', tamanho=[1, 11], raiz='//eSocial/evtMonit/exMedOcup/respMonit', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.nmResp = TagCaracter(nome='nmResp', tamanho=[1, 70], raiz='//eSocial/evtMonit/exMedOcup/respMonit', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nrCRM = TagCaracter(nome='nrCRM', tamanho=[1, 11], raiz='//eSocial/evtMonit/exMedOcup/respMonit', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ufCRM = TagCaracter(nome='ufCRM', tamanho=[1, 11], raiz='//eSocial/evtMonit/exMedOcup/respMonit', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<respMonit>'
        xml += self.cpfResp.xml
        xml += self.nmResp.xml
        xml += self.nrCRM.xml
        xml += self.ufCRM.xml
        xml += '</respMonit>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cpfResp.xml = arquivo
            self.nmResp.xml = arquivo
            self.nrCRM.xml = arquivo
            self.ufCRM.xml = arquivo

    xml = property(get_xml, set_xml)


class Medico(XMLNFe):
    def __init__(self):
        super(Medico, self).__init__()
        self.cpfMed = TagCaracter(nome='cpfMed', tamanho=[1, 11],   raiz='//eSocial/evtMonit/exMedOcup/aso/medico', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.nisMed = TagCaracter(nome='nisMed', tamanho=[1, 11],   raiz='//eSocial/evtMonit/exMedOcup/aso/medico', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.nmMed = TagCaracter(nome='nmMed', tamanho=[1, 70],   raiz='//eSocial/evtMonit/exMedOcup/aso/medico', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nrCRM = TagCaracter(nome='nrCRM', tamanho=[1, 8],   raiz='//eSocial/evtMonit/exMedOcup/aso/medico', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ufCRM = TagCaracter(nome='ufCRM', tamanho=[1, 2],   raiz='//eSocial/evtMonit/exMedOcup/aso/medico', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<medico>'
        xml += self.cpfMed.xml
        xml += self.nisMed.xml
        xml += self.nmMed.xml
        xml += self.nrCRM.xml
        xml += self.ufCRM.xml
        xml += '</medico>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cpfMed.xml = arquivo
            self.nisMed.xml = arquivo
            self.nmMed.xml = arquivo
            self.nrCRM.xml = arquivo
            self.ufCRM.xml = arquivo

    xml = property(get_xml, set_xml)


class Exame(XMLNFe):
    def __init__(self):
        super(Exame, self).__init__()
        self.dtExm = TagData(nome='dtExm', raiz='//dtExm', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.procRealizado = TagInteiro(nome='procRealizado', tamanho=[1, 4], raiz='//procRealizado', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.obsProc = TagCaracter(nome='obsProc', tamanho=[1, 999],   raiz='//obsProc', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.ordExame = TagInteiro(nome='ordExame', tamanho=[1, 1], raiz='//ordExame', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.indResult = TagInteiro(nome='indResult', tamanho=[1, 1], raiz='//indResult', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<exame>'
        xml += self.dtExm.xml
        xml += self.procRealizado.xml
        xml += self.obsProc.xml
        xml += self.ordExame.xml
        xml += self.indResult.xml
        xml += '</exame>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.dtExm.xml = arquivo
            self.procRealizado.xml = arquivo
            self.obsProc.xml = arquivo
            self.ordExame.xml = arquivo
            self.indResult.xml = arquivo

    xml = property(get_xml, set_xml)


class Aso(XMLNFe):
    def __init__(self):
        super(Aso, self).__init__()
        self.dtAso = TagData(nome='dtAso', raiz='//eSocial/evtMonit/exMedOcup/aso', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.resAso = TagInteiro(nome='resAso', raiz='//eSocial/evtMonit/exMedOcup/aso', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.exame = []
        self.medico = Medico()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<aso>'
        xml += self.dtAso.xml
        xml += self.resAso.xml
        for e in self.exame:
            xml += e.xml
        xml += self.medico.xml
        xml += '</aso>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.exame.xml = self.le_grupo('//eSocial/evtMonit/exMedOcup/aso/exame', Exame, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.medico.xml = arquivo

    xml = property(get_xml, set_xml)


class ExMedOcup(XMLNFe):
    def __init__(self):
        super(ExMedOcup, self).__init__()
        self.tpExameOcup = TagCaracter(nome='tpExameOcup', tamanho=[1, 1], raiz='//eSocial/evtMonit/exMedOcup', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, ignora_validacao=True)
        self.aso = Aso()
        self.respMonit = RespMonit()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<exMedOcup>'
        xml += self.tpExameOcup.xml
        xml += self.aso.xml
        xml += self.respMonit.xml
        xml += '</exMedOcup>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.aso.xml = arquivo
            self.respMonit.xml = arquivo

    xml = property(get_xml, set_xml)


class IdeVinculo(XMLNFe):
    def __init__(self):
        super(IdeVinculo, self).__init__()
        self.cpfTrab = TagCaracter(nome='cpfTrab', tamanho=[1, 11], raiz='//eSocial/evtMonit/ideVinculo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nisTrab = TagCaracter(nome='nisTrab', tamanho=[1, 11], raiz='//eSocial/evtMonit/ideVinculo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.matricula = TagCaracter(nome='matricula', tamanho=[1, 30], raiz='//eSocial/evtMonit/ideVinculo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.codCateg = TagCaracter(nome='codCateg', tamanho=[1, 30], raiz='//eSocial/evtMonit/ideVinculo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

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
        self.tpInsc = TagCaracter(nome='tpInsc', raiz='//eSocial/evtMonit/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor='1')
        self.nrInsc = TagCaracter(nome='nrInsc', raiz='//eSocial/evtMonit/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

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
        self.indRetif = TagInteiro(nome='indRetif', tamanho=[1, 1], raiz='//eSocial/evtExpRisco/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=1)
        self.tpAmb = TagInteiro(nome='tpAmb', raiz='//eSocial/evtMonit/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=2)
        self.procEmi = TagInteiro(nome='procEmi', raiz='//eSocial/evtMonit/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=1)
        self.verProc = TagCaracter(nome='verProc', raiz='//eSocial/evtMonit/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideEvento>'
        xml += self.indRetif.xml
        xml += self.tpAmb.xml
        xml += self.procEmi.xml
        xml += self.verProc.xml
        xml += '</ideEvento>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.indRetif.xml = arquivo
            self.tpAmb.xml = arquivo
            self.procEmi.xml = arquivo
            self.verProc.xml = arquivo

    xml = property(get_xml, set_xml)


class EvtMonit(XMLNFe):
    def __init__(self):
        super(EvtMonit, self).__init__()
        self.Id = TagCaracter(nome='evtMonit', propriedade='Id', raiz='//eSocial/evtMonit', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ideEvento = IdeEvento()
        self.ideEmpregador = IdeEmpregador()
        self.ideVinculo = IdeVinculo()
        self.exMedOcup = ExMedOcup()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.Id.xml
        xml += self.ideEvento.xml
        xml += self.ideEmpregador.xml
        xml += self.ideVinculo.xml
        xml += self.exMedOcup.xml
        xml += '</evtMonit>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml = arquivo
            self.ideEvento.xml = arquivo
            self.ideEmpregador.xml = arquivo
            self.ideVinculo.xml = arquivo
            self.exMedOcup.xml = arquivo

    xml = property(get_xml, set_xml)


class S2220(XMLNFe):
    def __init__(self):
        super(S2220, self).__init__()
        self.evtMonit = EvtMonit()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'evtMonit.xsd'
        self.id_evento = ''
        self.tpInsc = ''
        self.nrInsc = ''
        # self.Signature = Signature()
        self.evento = self.evtMonit
        self.xml_assinado = ''

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        #xml += ABERTURA
        xml += '<eSocial xmlns="' + NAMESPACE_ESOCIAL + '">'
        xml += self.evtMonit.xml

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
            self.evtMonit.xml = arquivo
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
        self.evtMonit.Id.valor = id_evento
        self.id_evento = id_evento

    xml = property(get_xml, set_xml)
