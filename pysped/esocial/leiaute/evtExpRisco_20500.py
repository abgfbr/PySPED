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

NAMESPACE_ESOCIAL = 'http://www.esocial.gov.br/schema/evt/evtExpRisco/v02_05_00'


class Obs(XMLNFe):
    def __init__(self):
        super(Obs, self).__init__()
        self.metErg = TagCaracter(nome='metErg', tamanho=[1, 999], raiz='//eSocial/evtExpRisco/InfoExpRisco/obs', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.obsCompl = TagCaracter(nome='obsCompl', tamanho=[1, 999], raiz='//eSocial/evtExpRisco/InfoExpRisco/obs', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<obs>'
        xml += self.metErg.xml
        xml += self.obsCompl.xml
        xml += '</obs>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.metErg.xml = arquivo
            self.obsCompl.xml = arquivo

    xml = property(get_xml, set_xml)


class RespReg(XMLNFe):
    def __init__(self):
        super(RespReg, self).__init__()
        self.cpfResp = TagCaracter(nome='cpfResp', tamanho=[1, 11], raiz='//eSocial/evtExpRisco/InfoExpRisco/respReg', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nisResp = TagCaracter(nome='nisResp', tamanho=[1, 11], raiz='//eSocial/evtExpRisco/InfoExpRisco/respReg', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nmResp = TagCaracter(nome='nmResp', tamanho=[1, 70], raiz='//eSocial/evtExpRisco/InfoExpRisco/respReg', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ideOC = TagCaracter(nome='ideOC', tamanho=[1, 1], raiz='//eSocial/evtExpRisco/InfoExpRisco/respReg', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dscOC = TagCaracter(nome='dscOC', tamanho=[1, 20], raiz='//eSocial/evtExpRisco/InfoExpRisco/respReg', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.nrOC = TagCaracter(nome='nrOC', tamanho=[1, 14], raiz='//eSocial/evtExpRisco/InfoExpRisco/respReg', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ufOC = TagCaracter(nome='ufOC', tamanho=[1, 2], raiz='//eSocial/evtExpRisco/InfoExpRisco/respReg', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<respReg>'
        xml += self.cpfResp.xml
        xml += self.nisResp.xml
        xml += self.nmResp.xml
        xml += self.ideOC.xml
        xml += self.dscOC.xml
        xml += self.nrOC.xml
        xml += self.ufOC.xml
        xml += '</respReg>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cpfResp.xml = arquivo
            self.nisResp.xml = arquivo
            self.nmResp.xml = arquivo
            self.ideOC.xml = arquivo
            self.dscOC.xml = arquivo
            self.nrOC.xml = arquivo
            self.ufOC.xml = arquivo

    xml = property(get_xml, set_xml)


class Epi(XMLNFe):
    def __init__(self):
        super(Epi, self).__init__()
        self.caEPI = TagCaracter(nome='caEPI', tamanho=[1, 20], raiz='//eSocial/evtExpRisco/InfoExpRisco/epcEpi/epi', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.dscEPI = TagCaracter(nome='dscEPI', tamanho=[1, 999], raiz='//eSocial/evtExpRisco/InfoExpRisco/epcEpi/epi', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.eficEpi = TagCaracter(nome='eficEpi', tamanho=[1, 1], raiz='//eSocial/evtExpRisco/InfoExpRisco/epcEpi/epi', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.medProtecao = TagCaracter(nome='medProtecao', tamanho=[1, 1], raiz='//eSocial/evtExpRisco/InfoExpRisco/epcEpi/epi', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.condFuncto = TagCaracter(nome='condFuncto', tamanho=[1, 1], raiz='//eSocial/evtExpRisco/InfoExpRisco/epcEpi/epi', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.usoInint = TagCaracter(nome='usoInint', tamanho=[1, 1], raiz='//eSocial/evtExpRisco/InfoExpRisco/epcEpi/epi', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.przValid = TagCaracter(nome='przValid', tamanho=[1, 1], raiz='//eSocial/evtExpRisco/InfoExpRisco/epcEpi/epi', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.periodicTroca = TagCaracter(nome='periodicTroca', tamanho=[1, 1], raiz='//eSocial/evtExpRisco/InfoExpRisco/epcEpi/epi', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.higienizacao = TagCaracter(nome='higienizacao', tamanho=[1, 1], raiz='//eSocial/evtExpRisco/InfoExpRisco/epcEpi/epi', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<epi>'
        xml += self.caEPI.xml
        xml += self.dscEPI.xml
        xml += self.eficEpi.xml
        xml += self.medProtecao.xml
        xml += self.condFuncto.xml
        xml += self.usoInint.xml
        xml += self.przValid.xml
        xml += self.periodicTroca.xml
        xml += self.higienizacao.xml
        xml += '</epi>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.caEPI.xml = arquivo
            self.dscEPI.xml = arquivo
            self.eficEpi.xml = arquivo
            self.medProtecao.xml = arquivo
            self.condFuncto.xml = arquivo
            self.usoInint.xml = arquivo
            self.przValid.xml = arquivo
            self.periodicTroca.xml = arquivo
            self.higienizacao.xml = arquivo

    xml = property(get_xml, set_xml)


class EpcEpi(XMLNFe):
    def __init__(self):
        super(EpcEpi, self).__init__()
        self.utilizEPC = TagCaracter(nome='utilizEPC', raiz='//eSocial/evtExpRisco/InfoExpRisco/fatRisco/epcEpi', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, ignora_validacao=True)
        self.eficEpc = TagCaracter(nome='eficEpc', tamanho=[1, 9], raiz='//eSocial/evtExpRisco/InfoExpRisco/epcEpi', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.utilizEPI = TagCaracter(nome='utilizEPI', raiz='//eSocial/evtExpRisco/InfoExpRisco/epcEpi', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, ignora_validacao=True)
        self.epi = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<epcEpi>'
        xml += self.utilizEPC.xml
        xml += self.eficEpc.xml
        xml += self.utilizEPI.xml
        for epi in self.epi:
            xml += epi.xml
        xml += '</epcEpi>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.utilizEPC.xml = arquivo
            self.eficEpc.xml = arquivo
            self.utilizEPI.xml = arquivo
            self.epi.xml = self.le_grupo('//eSocial/evtExpRisco/InfoExpRisco/fatRisco/epcEpi/epi', Epi, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class FatRisco(XMLNFe):
    def __init__(self):
        super(FatRisco, self).__init__()
        self.codFatRis = TagCaracter(nome='codFatRis', tamanho=[1, 9], raiz='//eSocial/evtExpRisco/InfoExpRisco/fatRisco', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.tpAval = TagInteiro(nome='tpAval', raiz='//eSocial/evtExpRisco/InfoExpRisco/fatRisco', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.initConc = TagInteiro(nome='initConc', raiz='//eSocial/evtExpRisco/InfoExpRisco/fatRisco', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.limTol = TagInteiro(nome='limTol', raiz='//eSocial/evtExpRisco/InfoExpRisco/fatRisco', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.unMed = TagInteiro(nome='unMed', raiz='//eSocial/evtExpRisco/InfoExpRisco/fatRisco', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.tecMedicao = TagCaracter(nome='tecMedicao', tamanho=[1, 40], raiz='//eSocial/evtExpRisco/InfoExpRisco/fatRisco', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.insalubridade = TagCaracter(nome='insalubridade', tamanho=[1, 1], raiz='//eSocial/evtExpRisco/InfoExpRisco/fatRisco', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.periculosidade = TagCaracter(nome='periculosidade', tamanho=[1, 1], raiz='//eSocial/evtExpRisco/InfoExpRisco/fatRisco', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.aposentEsp = TagCaracter(nome='aposentEsp', tamanho=[1, 1], raiz='//eSocial/evtExpRisco/InfoExpRisco/fatRisco', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.epcEpi = EpcEpi()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<fatRisco>'
        xml += self.codFatRis.xml
        xml += self.tpAval.xml
        xml += self.initConc.xml
        xml += self.limTol.xml
        xml += self.unMed.xml
        xml += self.tecMedicao.xml
        xml += self.insalubridade.xml
        xml += self.periculosidade.xml
        xml += self.aposentEsp.xml
        xml += self.epcEpi.xml
        xml += '</fatRisco>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.codFatRis.xml = arquivo
            self.tpAval.xml = arquivo
            self.initConc.xml = arquivo
            self.limTol.xml = arquivo
            self.unMed.xml = arquivo
            self.tecMedicao.xml = arquivo
            self.insalubridade.xml = arquivo
            self.periculosidade.xml = arquivo
            self.aposentEsp.xml = arquivo
            self.epcEpi.xml = arquivo


    xml = property(get_xml, set_xml)


class AtivPericInsal(XMLNFe):
    def __init__(self):
        super(AtivPericInsal, self).__init__()
        self.codAtiv = TagCaracter(nome='codAtiv', tamanho=[1, 6], raiz='//eSocial/evtExpRisco/InfoExpRisco/infoAtiv/ativPericInsal', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ativPericInsal>'
        xml += self.codAtiv.xml
        xml += '</ativPericInsal>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.codAtiv.xml = arquivo

    xml = property(get_xml, set_xml)


class InfoAtiv(XMLNFe):
    def __init__(self):
        super(InfoAtiv, self).__init__()
        self.dscAtivDes = TagCaracter(nome='dscAtivDes', tamanho=[1, 999], raiz='//eSocial/evtExpRisco/InfoExpRisco/infoAtiv', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ativPericInsal = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoAtiv>'
        xml += self.dscAtivDes.xml
        for ativ_peric in self.ativPericInsal:
            xml += ativ_peric.xml
        xml += '</infoAtiv>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.dscAtivDes.xml = arquivo
            self.ativPericInsal.xml = self.le_grupo('//eSocial/evtExpRisco/InfoExpRisco/infoAtiv/ativPericInsal', AtivPericInsal, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class InfoAmb(XMLNFe):
    def __init__(self):
        super(InfoAmb, self).__init__()
        self.codAmb = TagCaracter(nome='codAmb', tamanho=[1, 30], raiz='//eSocial/evtExpRisco/InfoExpRisco/InfoAmb', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoAmb>'
        xml += self.codAmb.xml
        xml += '</infoAmb>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.codAmb.xml = arquivo

    xml = property(get_xml, set_xml)


class InfoExpRisco(XMLNFe):
    def __init__(self):
        super(InfoExpRisco, self).__init__()
        self.dtIniCondicao = TagData(nome='dtIniCondicao', raiz='//eSocial/evtExpRisco/InfoExpRisco', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.infoAmb = []
        self.infoAtiv = InfoAtiv()
        self.fatRisco = []
        self.respReg = []
        self.obs = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoExpRisco>'
        xml += self.dtIniCondicao.xml
        for info_amb in self.infoAmb:
            xml += info_amb.xml
        xml += self.infoAtiv.xml
        for fat_risco in self.fatRisco:
            xml += fat_risco.xml
        for resp_reg in self.respReg:
            xml += resp_reg.xml
        for obs in self.obs:
            xml += obs.xml
        xml += '</infoExpRisco>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.dtIniCondicao.xml = arquivo
            self.infoAmb.xml = self.le_grupo('//eSocial/evtExpRisco/InfoExpRisco/infoAmb', InfoAmb, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.infoAtiv.xml = arquivo
            self.fatRisco.xml = self.le_grupo('//eSocial/evtExpRisco/fatRisco', FatRisco, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.respReg.xml = self.le_grupo('//eSocial/evtExpRisco/respReg', RespReg, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.obs.xml = self.le_grupo('//eSocial/evtExpRisco/obs', Obs, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class IdeVinculo(XMLNFe):
    def __init__(self):
        super(IdeVinculo, self).__init__()
        self.cpfTrab = TagCaracter(nome='cpfTrab', tamanho=[1, 11], raiz='//eSocial/evtExpRisco/ideVinculo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nisTrab = TagCaracter(nome='nisTrab', tamanho=[1, 11], raiz='//eSocial/evtExpRisco/ideVinculo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.matricula = TagCaracter(nome='matricula', tamanho=[1, 30], raiz='//eSocial/evtExpRisco/ideVinculo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.codCateg = TagCaracter(nome='codCateg', tamanho=[1, 30], raiz='//eSocial/evtExpRisco/ideVinculo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

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
        self.tpInsc = TagCaracter(nome='tpInsc', raiz='//eSocial/evtExpRisco/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor='1')
        self.nrInsc = TagCaracter(nome='nrInsc', raiz='//eSocial/evtExpRisco/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

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
        self.tpAmb = TagInteiro(nome='tpAmb', raiz='//eSocial/evtExpRisco/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=2)
        self.procEmi = TagInteiro(nome='procEmi', raiz='//eSocial/evtExpRisco/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=1)
        self.verProc = TagCaracter(nome='verProc', raiz='//eSocial/evtExpRisco/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

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


class EvtExpRisco(XMLNFe):
    def __init__(self):
        super(EvtExpRisco, self).__init__()
        self.Id = TagCaracter(nome='evtExpRisco', propriedade='Id', raiz='//eSocial/evtExpRisco', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ideEvento = IdeEvento()
        self.ideEmpregador = IdeEmpregador()
        self.ideVinculo = IdeVinculo()
        self.infoExpRisco = InfoExpRisco()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.Id.xml
        xml += self.ideEvento.xml
        xml += self.ideEmpregador.xml
        xml += self.ideVinculo.xml
        xml += self.infoExpRisco.xml
        xml += '</evtExpRisco>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml = arquivo
            self.ideEvento.xml = arquivo
            self.ideEmpregador.xml = arquivo
            self.ideVinculo.xml = arquivo
            self.infoExpRisco.xml = arquivo

    xml = property(get_xml, set_xml)


class S2240(XMLNFe):
    def __init__(self):
        super(S2240, self).__init__()
        self.evtExpRisco = EvtExpRisco()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'evtExpRisco.xsd'
        self.id_evento = ''
        self.tpInsc = ''
        self.nrInsc = ''
        # self.Signature = Signature()
        self.evento = self.evtExpRisco
        self.xml_assinado = ''

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        #xml += ABERTURA
        xml += '<eSocial xmlns="' + NAMESPACE_ESOCIAL + '">'
        xml += self.evtExpRisco.xml

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
            self.evtExpRisco.xml = arquivo
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
        self.evtExpRisco.Id.valor = id_evento
        self.id_evento = id_evento

    xml = property(get_xml, set_xml)
