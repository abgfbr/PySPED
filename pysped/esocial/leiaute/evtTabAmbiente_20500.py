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

NAMESPACE_ESOCIAL = 'http://www.esocial.gov.br/schema/evt/evtTabAmbiente/v02_05_00'


class DadosAmbiente(XMLNFe):
    def __init__(self, tipo):
        super(DadosAmbiente, self).__init__(tipo)
        raiz_tipo = '//eSocial/evtTabAmbiente/infoAmbiente/{}/nmAmb'.format(tipo)
        self.nmAmb = TagCaracter(nome='nmAmb', tamanho=[1, 100], raiz=raiz_tipo, namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dscAmb = TagCaracter(nome='dscAmb', tamanho=[1, 8000], raiz=raiz_tipo, namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.localAmb = TagCaracter(nome='localAmb', tamanho=[1, 1], raiz=raiz_tipo, namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.tpInsc = TagCaracter(nome='tpInsc', tamanho=[1, 1], raiz=raiz_tipo, namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.nrInsc = TagCaracter(nome='nrInsc', tamanho=[1, 15], raiz=raiz_tipo, namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.codLotacao = TagCaracter(nome='codLotacao', tamanho=[1, 30], raiz=raiz_tipo, namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<dadosAmbiente>'
        xml += self.nmAmb.xml
        xml += self.dscAmb.xml
        xml += self.localAmb.xml
        xml += self.tpInsc.xml
        xml += self.nrInsc.xml
        xml += self.codLotacao.xml
        xml += '</dadosAmbiente>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nmAmb.xml = arquivo
            self.dscAmb.xml = arquivo
            self.localAmb.xml = arquivo
            self.tpInsc.xml = arquivo
            self.nrInsc.xml = arquivo
            self.codLotacao.xml = arquivo

    xml = property(get_xml, set_xml)


class IdeAmbiente(XMLNFe):
    def __init__(self, tipo):
        super(IdeAmbiente, self).__init__(tipo)
        raiz_tipo = '//eSocial/evtTabAmbiente/infoAmbiente/{}/ideAmbiente'.format(tipo)
        self.codAmb = TagCaracter(nome='codAmb', raiz=raiz_tipo, namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.iniValid = TagCaracter(nome='iniValid', raiz=raiz_tipo, namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.fimValid = TagCaracter(nome='fimValid', raiz=raiz_tipo, namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideAmbiente>'
        xml += self.codAmb.xml
        xml += self.iniValid.xml
        xml += self.fimValid.xml
        xml += '</ideAmbiente>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.codAmb.xml = arquivo
            self.iniValid.xml = arquivo
            self.fimValid.xml = arquivo

    xml = property(get_xml, set_xml)


class Exclusao(XMLNFe):
    def __init__(self):
        super(Exclusao, self).__init__()
        self.ideAmbiente = IdeAmbiente(tipo='exclusao')

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<exclusao>'
        xml += self.ideAmbiente.xml
        xml += self.dadosAmbiente.xml
        xml += '</exclusao>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.ideAmbiente.xml = arquivo
            self.dadosAmbiente.xml = arquivo

    xml = property(get_xml, set_xml)


class NovaValidade(XMLNFe):
    def __init__(self):
        super(NovaValidade, self).__init__()
        self.iniValid = TagCaracter(nome='iniValid', raiz='//iniValid', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.fimValid = TagCaracter(nome='fimValid', raiz='//fimValid', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<novaValidade>'
        xml += self.iniValid.xml
        xml += self.fimValid.xml
        xml += '</novaValidade>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.iniValid.xml = arquivo
            self.fimValid.xml = arquivo

    xml = property(get_xml, set_xml)


class Alteracao(XMLNFe):
    def __init__(self):
        super(Alteracao, self).__init__()
        self.ideAmbiente = IdeAmbiente(tipo='alteracao')
        self.dadosAmbiente = DadosAmbiente(tipo='alteracao')
        self.novaValidade = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<alteracao>'
        xml += self.ideAmbiente.xml
        xml += self.dadosAmbiente.xml
        for nova_validade in self.novaValidade:
            xml += nova_validade.xml
        xml += '</alteracao>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.ideAmbiente.xml = arquivo
            self.dadosAmbiente.xml = arquivo
            self.novaValidade.xml = self.le_grupo('//eSocial/evtTabAmbiente/infoAmbiente/alteracao/novaValidade', NovaValidade, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class Inclusao(XMLNFe):
    def __init__(self):
        super(Inclusao, self).__init__()
        self.ideAmbiente = IdeAmbiente(tipo='inclusao')
        self.dadosAmbiente = DadosAmbiente(tipo='inclusao')

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<inclusao>'
        xml += self.ideAmbiente.xml
        xml += self.dadosAmbiente.xml
        xml += '</inclusao>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.ideAmbiente.xml = arquivo
            self.dadosAmbiente.xml = arquivo

    xml = property(get_xml, set_xml)


class InfoAmbiente(XMLNFe):
    def __init__(self):
        super(InfoAmbiente, self).__init__()
        self.inclusao = []
        self.alteracao = []
        self.exclusao = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoAmbiente>'
        for i in self.inclusao:
            xml += i.xml
        for a in self.alteracao:
            xml += a.xml
        for e in self.exclusao:
            xml += e.xml
        xml += '</infoAmbiente>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.inclusao = self.le_grupo('//eSocial/evtTabAmbiente/infoAmbiente/inclusao', Inclusao, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.alteracao = self.le_grupo('//eSocial/evtTabAmbiente/infoAmbiente/alteracao', Alteracao, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.exclusao = self.le_grupo('//eSocial/evtTabAmbiente/infoAmbiente/exclusao', Exclusao, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class IdeEmpregador(XMLNFe):
    def __init__(self):
        super(IdeEmpregador, self).__init__()
        self.tpInsc = TagCaracter(nome='tpInsc', raiz='//eSocial/evtTabAmbiente/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor='1')
        self.nrInsc = TagCaracter(nome='nrInsc', raiz='//eSocial/evtTabAmbiente/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

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
        self.tpAmb = TagInteiro(nome='tpAmb', raiz='//eSocial/evtTabAmbiente/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=2)
        self.procEmi = TagInteiro(nome='procEmi', raiz='//eSocial/evtTabAmbiente/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=1)
        self.verProc = TagCaracter(nome='verProc', raiz='//eSocial/evtTabAmbiente/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

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


class EvtTabAmbiente(XMLNFe):
    def __init__(self):
        super(EvtTabAmbiente, self).__init__()
        self.Id = TagCaracter(nome='evtTabAmbiente', propriedade='Id', raiz='//eSocial/evtTabAmbiente', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ideEvento = IdeEvento()
        self.ideEmpregador = IdeEmpregador()
        self.infoAmbiente = InfoAmbiente()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.Id.xml
        xml += self.ideEvento.xml
        xml += self.ideEmpregador.xml
        xml += self.infoAmbiente.xml
        xml += '</evtTabAmbiente>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml = arquivo
            self.ideEvento.xml = arquivo
            self.ideEmpregador.xml = arquivo
            self.infoAmbiente.xml = arquivo

    xml = property(get_xml, set_xml)


class S1060(XMLNFe):
    def __init__(self):
        super(S1060, self).__init__()
        self.evtTabAmbiente = EvtTabAmbiente()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'evtTabAmbiente.xsd'
        self.id_evento = ''
        self.tpInsc = ''
        self.nrInsc = ''
        # self.Signature = Signature()
        self.evento = self.evtTabAmbiente
        self.xml_assinado = ''

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        #xml += ABERTURA
        xml += '<eSocial xmlns="' + NAMESPACE_ESOCIAL + '">'
        xml += self.evtTabAmbiente.xml

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
            self.evtTabAmbiente.xml = arquivo
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
        self.evtTabAmbiente.Id.valor = id_evento
        self.id_evento = id_evento

    xml = property(get_xml, set_xml)
