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

NAMESPACE_ESOCIAL = 'http://www.esocial.gov.br/schema/evt/evtCAT/v02_05_00'


class CatOrigem(XMLNFe):
    def __init__(self):
        super(CatOrigem, self).__init__()
        self.nrRecCatOrig = TagCaracter(nome='nrRecCatOrig', tamanho=[1, 40], raiz='//nrRecCatOrig', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<catOrigem>'
        xml += self.nrRecCatOrig.xml
        xml += '</catOrigem>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nrRecCatOrig.xml = arquivo

    xml = property(get_xml, set_xml)


class Atestado(XMLNFe):
    def __init__(self):
        super(Atestado, self).__init__()
        self.codCNES = TagCaracter(nome='codCNES', tamanho=[1, 7], raiz='//codCNES', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.dtAtendimento = TagData(nome='dtAtendimento', raiz='//dtAtendimento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.hrAtendimento = TagCaracter(nome='hrAtendimento', tamanho=[1, 4], raiz='//hrAtendimento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.indInternacao = TagCaracter(nome='indInternacao', tamanho=[1, 1], raiz='//indInternacao', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.durTrat = TagInteiro(nome='durTrat', raiz='//durTrat', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=1)
        self.indAfast = TagCaracter(nome='indAfast', tamanho=[1, 1], raiz='//indAfast', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dscLesao = TagInteiro(nome='dscLesao', raiz='//dscLesao', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=1)
        self.dscCompLesao = TagCaracter(nome='dscCompLesao', tamanho=[1, 200], raiz='//dscCompLesao', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.diagProvavel = TagCaracter(nome='diagProvavel', tamanho=[1, 100], raiz='//diagProvavel', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.codCID = TagCaracter(nome='codCID', tamanho=[1, 4], raiz='//codCID', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.observacao = TagCaracter(nome='observacao', tamanho=[1, 255], raiz='//observacao', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.nmEmit = TagCaracter(nome='nmEmit', tamanho=[1, 70], raiz='//nmEmit', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ideOC = TagInteiro(nome='ideOC', raiz='//ideOC', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=1)
        self.nrOC = TagCaracter(nome='nrOC', tamanho=[1, 14], raiz='//nrOC', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ufOC = TagCaracter(nome='ufOC', tamanho=[1, 2], raiz='//ufOC', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<atestado>'
        xml += self.codCNES.xml
        xml += self.dtAtendimento.xml
        xml += self.hrAtendimento.xml
        xml += self.indInternacao.xml
        xml += self.durTrat.xml
        xml += self.indAfast.xml
        xml += self.dscLesao.xml
        xml += self.dscCompLesao.xml
        xml += self.diagProvavel.xml
        xml += self.codCID.xml
        xml += self.observacao.xml
        xml += '<emitente>'
        xml += self.nmEmit.xml
        xml += self.ideOC.xml
        xml += self.nrOC.xml
        xml += self.ufOC.xml
        xml += '</emitente>'
        xml += '</atestado>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.codCNES.xml = arquivo
            self.dtAtendimento.xml = arquivo
            self.hrAtendimento.xml = arquivo
            self.indInternacao.xml = arquivo
            self.durTrat.xml = arquivo
            self.indAfast.xml = arquivo
            self.dscLesao.xml = arquivo
            self.dscCompLesao.xml = arquivo
            self.diagProvavel.xml = arquivo
            self.codCID.xml = arquivo
            self.observacao.xml = arquivo
            self.nmEmit.xml = arquivo
            self.ideOC.xml = arquivo
            self.nrOC.xml = arquivo
            self.ufOC.xml = arquivo

    xml = property(get_xml, set_xml)


class AgenteCausador(XMLNFe):
    def __init__(self):
        super(AgenteCausador, self).__init__()
        self.codAgntCausador = TagInteiro(nome='codAgntCausador', raiz='//codAgntCausador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=1)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<agenteCausador>'
        xml += self.codAgntCausador.xml
        xml += '</agenteCausador>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.codAgntCausador.xml = arquivo

    xml = property(get_xml, set_xml)


class ParteAtingida(XMLNFe):
    def __init__(self):
        super(ParteAtingida, self).__init__()
        self.codParteAting = TagInteiro(nome='codParteAting', raiz='//codParteAting', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=1)
        self.lateralidade = TagInteiro(nome='lateralidade', raiz='//lateralidade', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=1)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<parteAtingida>'
        xml += self.codParteAting.xml
        xml += self.lateralidade.xml
        xml += '</parteAtingida>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.codParteAting.xml = arquivo
            self.lateralidade.xml = arquivo

    xml = property(get_xml, set_xml)


class IdeLocalAcid(XMLNFe):
    def __init__(self):
        super(IdeLocalAcid, self).__init__()
        self.tpInsc = TagInteiro(nome='tpInsc', raiz='//tpInsc', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=1)
        self.nrInsc = TagCaracter(nome='nrInsc', tamanho=[1, 15], raiz='//nrInsc', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideLocalAcid>'
        xml += self.tpInsc.xml
        xml += self.nrInsc.xml
        xml += '</ideLocalAcid>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpInsc.xml = arquivo
            self.nrInsc.xml = arquivo

    xml = property(get_xml, set_xml)


class LocalAcidente(XMLNFe):
    def __init__(self):
        super(LocalAcidente, self).__init__()
        self.tpLocal = TagInteiro(nome='tpLocal', raiz='//eSocial/evtCAT/cat/localAcidente', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=1)
        self.dscLocal = TagCaracter(nome='dscLocal', tamanho=[1, 255], raiz='//eSocial/evtCAT/cat/localAcidente', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.codAmb = TagCaracter(nome='codAmb', tamanho=[1, 30], raiz='//eSocial/evtCAT/cat/localAcidente', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.tpLograd = TagCaracter(nome='tpLograd', tamanho=[1, 4], raiz='//eSocial/evtCAT/cat/localAcidente', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dscLograd = TagCaracter(nome='dscLograd', tamanho=[1, 100], raiz='//eSocial/evtCAT/cat/localAcidente', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nrLograd = TagCaracter(nome='nrLograd', tamanho=[1, 10], raiz='//eSocial/evtCAT/cat/localAcidente', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.complemento = TagCaracter(nome='complemento', tamanho=[1, 30], raiz='//eSocial/evtCAT/cat/localAcidente', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.bairro = TagCaracter(nome='bairro', tamanho=[1, 90], raiz='//eSocial/evtCAT/cat/localAcidente', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.cep = TagCaracter(nome='cep', tamanho=[1, 9], raiz='//eSocial/evtCAT/cat/localAcidente', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.codMunic = TagCaracter(nome='codMunic', tamanho=[1, 8], raiz='//eSocial/evtCAT/cat/localAcidente', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=1, obrigatorio=False)
        self.uf = TagCaracter(nome='uf', tamanho=[1, 2], raiz='//eSocial/evtCAT/cat/localAcidente', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.pais = TagCaracter(nome='pais', tamanho=[1, 3], raiz='//eSocial/evtCAT/cat/localAcidente', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.codPostal = TagCaracter(nome='codPostal', tamanho=[1, 12], raiz='//eSocial/evtCAT/cat/localAcidente', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.ideLocalAcid = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<localAcidente>'
        xml += self.tpLocal.xml
        xml += self.dscLocal.xml
        xml += self.codAmb.xml
        xml += self.tpLograd.xml
        xml += self.dscLograd.xml
        xml += self.nrLograd.xml
        xml += self.complemento.xml
        xml += self.bairro.xml
        xml += self.cep.xml
        xml += self.codMunic.xml
        xml += self.uf.xml
        xml += self.pais.xml
        xml += self.codPostal.xml
        for identificacao_local in self.ideLocalAcid:
            xml += identificacao_local.xml
        xml += '</localAcidente>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpLocal.xml = arquivo
            self.dscLocal.xml = arquivo
            self.codAmb.xml = arquivo
            self.tpLograd.xml = arquivo
            self.dscLograd.xml = arquivo
            self.nrLograd.xml = arquivo
            self.complemento.xml = arquivo
            self.bairro.xml = arquivo
            self.cep.xml = arquivo
            self.codMunic.xml = arquivo
            self.uf.xml = arquivo
            self.pais.xml = arquivo
            self.codPostal.xml = arquivo
            self.ideLocalAcid.xml = self.le_grupo('//eSocial/evtCAT/cat/localAcidente/ideLocalAcid', IdeLocalAcid, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class Cat(XMLNFe):
    def __init__(self):
        super(Cat, self).__init__()
        self.dtAcid = TagData(nome='dtAcid', raiz='//eSocial/evtCAT/cat', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.tpAcid = TagCaracter(nome='tpAcid', tamanho=[1, 6], raiz='//eSocial/evtCAT/cat', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.hrAcid = TagCaracter(nome='hrAcid', tamanho=[1, 4], raiz='//eSocial/evtCAT/cat', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.hrsTrabAntesAcid = TagCaracter(nome='hrsTrabAntesAcid', tamanho=[1, 4], raiz='//eSocial/evtCAT/cat', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.tpCat = TagCaracter(nome='tpCat', tamanho=[1, 4], raiz='//eSocial/evtCAT/cat', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.indCatObito = TagCaracter(nome='indCatObito', tamanho=[1, 1], raiz='//eSocial/evtCAT/cat', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dtObito = TagData(nome='dtObito', raiz='//eSocial/evtCAT/cat', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.indComunPolicia = TagCaracter(nome='indComunPolicia', tamanho=[1, 1], raiz='//eSocial/evtCAT/cat', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.codSitGeradora = TagInteiro(nome='codSitGeradora', raiz='//eSocial/evtExpRisco/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=1)
        self.iniciatCAT = TagInteiro(nome='iniciatCAT', raiz='//eSocial/evtExpRisco/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=1)
        self.obsCAT = TagCaracter(nome='obsCAT', tamanho=[1, 999], raiz='//eSocial/evtCAT/cat', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.localAcidente = LocalAcidente()
        self.parteAtingida = []
        self.agenteCausador = []
        self.atestado = []
        self.catOrigem = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<cat>'
        xml += self.dtAcid.xml
        xml += self.tpAcid.xml
        xml += self.hrAcid.xml
        xml += self.hrsTrabAntesAcid.xml
        xml += self.tpCat.xml
        xml += self.indCatObito.xml
        xml += self.dtObito.xml
        xml += self.indComunPolicia.xml
        xml += self.codSitGeradora.xml
        xml += self.iniciatCAT.xml
        xml += self.obsCAT.xml
        xml += self.localAcidente.xml
        for parte_atingida in self.parteAtingida:
            xml += parte_atingida.xml
        for agente_causador in self.agenteCausador:
            xml += agente_causador.xml
        for atestado in self.atestado:
            xml += atestado.xml
        for cat_origem in self.catOrigem:
            xml += cat_origem.xml
        xml += '</cat>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.dtAcid.xml = arquivo
            self.tpAcid.xml = arquivo
            self.hrAcid.xml = arquivo
            self.hrsTrabAntesAcid.xml = arquivo
            self.tpCat.xml = arquivo
            self.indCatObito.xml = arquivo
            self.dtObito.xml = arquivo
            self.indComunPolicia.xml = arquivo
            self.codSitGeradora.xml = arquivo
            self.iniciatCAT.xml = arquivo
            self.obsCAT.xml = arquivo
            self.localAcidente.xml = arquivo
            self.parteAtingida.xml = self.le_grupo('//eSocial/evtCAT/cat/parteAtingida', ParteAtingida, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.agenteCausador.xml = self.le_grupo('//eSocial/evtCAT/cat/agenteCausador', AgenteCausador, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.atestado.xml = self.le_grupo('//eSocial/evtCAT/cat/atestado', Atestado, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.catOrigem.xml = self.le_grupo('//eSocial/evtCAT/cat/catOrigem', CatOrigem, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class IdeVinculo(XMLNFe):
    def __init__(self):
        super(IdeVinculo, self).__init__()
        self.cpfTrab = TagCaracter(nome='cpfTrab', tamanho=[1, 11], raiz='//eSocial/evtCAT/ideVinculo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nisTrab = TagCaracter(nome='nisTrab', tamanho=[1, 11], raiz='//eSocial/evtCAT/ideVinculo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.matricula = TagCaracter(nome='matricula', tamanho=[1, 30], raiz='//eSocial/evtCAT/ideVinculo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.codCateg = TagCaracter(nome='matricula', tamanho=[1, 30], raiz='//eSocial/evtCAT/ideVinculo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

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
        self.tpInsc = TagCaracter(nome='tpInsc', raiz='//eSocial/evtCAT/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor='1')
        self.nrInsc = TagCaracter(nome='nrInsc', raiz='//eSocial/evtCAT/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

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
        self.tpAmb = TagInteiro(nome='tpAmb', raiz='//eSocial/evtCAT/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=2)
        self.procEmi = TagInteiro(nome='procEmi', raiz='//eSocial/evtCAT/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=1)
        self.verProc = TagCaracter(nome='verProc', raiz='//eSocial/evtCAT/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

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


class EvtCAT(XMLNFe):
    def __init__(self):
        super(EvtCAT, self).__init__()
        self.Id = TagCaracter(nome='evtCAT', propriedade='Id', raiz='//eSocial/evtCAT', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ideEvento = IdeEvento()
        self.ideEmpregador = IdeEmpregador()
        self.ideVinculo = IdeVinculo()
        self.cat = Cat()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.Id.xml
        xml += self.ideEvento.xml
        xml += self.ideEmpregador.xml
        xml += self.ideVinculo.xml
        xml += self.cat.xml
        xml += '</evtCAT>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml = arquivo
            self.ideEvento.xml = arquivo
            self.ideEmpregador.xml = arquivo
            self.ideVinculo.xml = arquivo
            self.cat.xml = arquivo

    xml = property(get_xml, set_xml)


class S2210(XMLNFe):
    def __init__(self):
        super(S2210, self).__init__()
        self.evtCAT = EvtCAT()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'evtCAT.xsd'
        self.id_evento = ''
        self.tpInsc = ''
        self.nrInsc = ''
        # self.Signature = Signature()
        self.evento = self.evtCAT
        self.xml_assinado = ''

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        #xml += ABERTURA
        xml += '<eSocial xmlns="' + NAMESPACE_ESOCIAL + '">'
        xml += self.evtCAT.xml

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
            self.evtCAT.xml = arquivo
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
        self.evtCAT.Id.valor = id_evento
        self.id_evento = id_evento

    xml = property(get_xml, set_xml)
