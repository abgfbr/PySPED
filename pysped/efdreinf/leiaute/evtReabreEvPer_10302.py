# -*- coding: utf-8 -*-
#
# PySPED - Python libraries to deal with Brazil's SPED Project
#
# Copyright (C) 2010-2012
# Copyright (C) Wagner Pereira <wagner.pereira at tauga.com.br>
# Copyright (C) Luiz Felipe do Divino <luiz.divino@abgf.gov.br>
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

from builtins import str
from pysped.efdreinf.leiaute import ESQUEMA_ATUAL_VERSAO_1 as ESQUEMA_ATUAL
from pysped.xml_sped import *

DIRNAME = os.path.dirname(__file__)

NAMESPACE_EFDREINF = 'http://www.reinf.esocial.gov.br/schemas/evtReabreEvPer/v1_04_00'


class IdeContri(XMLNFe):
    def __init__(self):
        super(IdeContri, self).__init__()
        self.tpInsc = TagCaracter(nome='tpInsc', valor='1',
                                  raiz='//Reinf/evtReabreEvPer/ideContri',
                                  namespace=NAMESPACE_EFDREINF,
                                  namespace_obrigatorio=False)
        self.nrInsc = TagCaracter(nome='nrInsc', tamanho=[8, 14],
                                  raiz='//Reinf/evtReabreEvPer/ideContri',
                                  namespace=NAMESPACE_EFDREINF,
                                  namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideContri>'
        xml += self.tpInsc.xml
        xml += self.nrInsc.xml
        xml += '</ideContri>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpInsc.xml = arquivo
            self.nrInsc.xml = arquivo
        return True

    xml = property(get_xml, set_xml)


class IdeEvento(XMLNFe):
    def __init__(self):
        super(IdeEvento, self).__init__()
        self.perApur = TagCaracter(nome='perApur', tamanho=[1, 10],
                                   raiz='//Reinf/evtReabreEvPer/ideEvento',
                                   namespace=NAMESPACE_EFDREINF,
                                   namespace_obrigatorio=False)
        self.tpAmb = TagInteiro(nome='tpAmb', tamanho=[1, 1, 1],
                                raiz='//Reinf/evtReabreEvPer/ideEvento',
                                namespace=NAMESPACE_EFDREINF,
                                namespace_obrigatorio=False, valor=2)
        self.procEmi = TagInteiro(nome='procEmi', tamanho=[1, 1, 1],
                                  raiz='//Reinf/evtReabreEvPer/ideEvento',
                                  namespace=NAMESPACE_EFDREINF,
                                  namespace_obrigatorio=False)
        self.verProc = TagCaracter(nome='verProc', tamanho=[1, 20],
                                   raiz='//Reinf/evtReabreEvPer/ideEvento',
                                   namespace=NAMESPACE_EFDREINF,
                                   namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideEvento>'
        xml += self.perApur.xml
        xml += self.tpAmb.xml
        xml += self.procEmi.xml
        xml += self.verProc.xml
        xml += '</ideEvento>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.perApur.xml = arquivo
            self.tpAmb.xml = arquivo
            self.procEmi.xml = arquivo
            self.verProc.xml = arquivo
        return True

    xml = property(get_xml, set_xml)


class EvtReabreEvPer(XMLNFe):
    def __init__(self):
        super(EvtReabreEvPer, self).__init__()
        self.Id = TagCaracter(nome='evtReabreEvPer', propriedade='id',
                              raiz='//Reinf/evtReabreEvPer',
                              namespace=NAMESPACE_EFDREINF,
                              namespace_obrigatorio=False)
        self.ideEvento = IdeEvento()
        self.ideContri = IdeContri()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.Id.xml
        xml += self.ideEvento.xml
        xml += self.ideContri.xml
        xml += '</evtReabreEvPer>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml = arquivo
            self.ideEvento.xml = arquivo
            self.ideContri.xml = arquivo
        return True

    xml = property(get_xml, set_xml)


class R2098(XMLNFe):
    def __init__(self):
        super(R2098, self).__init__()
        self.evtReabreEvPer = EvtReabreEvPer()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/',
                                            ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'evtReabreEvPer-v1_04_00.xsd'
        self.id_evento = ''
        self.Signature = Signature()
        self.evento = self.evtReabreEvPer

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        # xml += ABERTURA
        xml += '<Reinf xmlns="' + NAMESPACE_EFDREINF + '">'
        xml += self.evtReabreEvPer.xml

        #
        # Define a URI a ser assinada
        #
        self.Signature.URI = '#' + self.evtReabreEvPer.Id.valor
        xml += self.Signature.xml
        xml += '</Reinf>'

        # Define o método de assinatura
        self.Signature.metodo = 'sha256'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.evtReabreEvPer.xml = arquivo
            self.Signature.xml = self._le_noh(
                '//Reinf/evtReabreEvPer/sig:Signature')

    def gera_id_evento(self, data_hora, sequencia=False):

        # A identificação única do evento (Id) é composta por 36 caracteres, conforme o que segue: IDTNNNNNNNNNNNNNNAAAAMMDDHHMMSSQQQQQ
        # ID - Texto Fixo "ID";
        # T - Tipo de Inscrição do Empregador (1 - CNPJ; 2 - CPF);
        # NNNNNNNNNNNNNN - Número do CNPJ ou CPF do empregador - Completar com
        # zeros à direita. No caso de pessoas jurídicas, o CNPJ informado deve conter 8 ou 14
        # posições de acordo com o enquadramento do contribuinte para preenchimento do campo
        # {ideEmpregador/nrInsc} do evento S-1000, completando-se com zeros à direita, se
        # necessário.
        # AAAAMMDD - Ano, mês e dia da geração do evento;
        # HHMMSS - Hora, minuto e segundo da geração do evento;
        # QQQQQ - Número sequencial da chave. Incrementar somente quando ocorrer geração de
        # eventos na mesma data/hora, completando com zeros à esquerda.
        # OBS.: No caso de pessoas jurídicas, o CNPJ informado deverá conter 8 ou 14 posições de
        # acordo com o enquadramento do contribuinte para preenchimento do campo {ideEmpregador/nrInsc} do evento S-1000, completando-se com zeros à direita, se necessário.        

        if not sequencia:
            sequencia = 1

        id_evento = 'ID'
        id_evento += self.evtReabreEvPer.ideContri.tpInsc.valor
        id_evento += str(self.evtReabreEvPer.ideContri.nrInsc.valor)[
                     0:8] + '000000'
        # id_evento += str(self.evtInfoContri.ideContri.nrInsc.valor).zfill(14)
        id_evento += data_hora
        id_evento += str(sequencia).zfill(5)

        # Define o Id
        #
        self.evtReabreEvPer.Id.valor = id_evento
        self.id_evento = id_evento

    xml = property(get_xml, set_xml)
