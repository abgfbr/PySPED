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

NAMESPACE_ESOCIAL = 'http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_01_00'


class BaseMudCateg(XMLNFe):
    def __init__(self):
        super(BaseMudCateg, self).__init__()
        self.codCateg = TagInteiro(nome='codCateg', raiz='//baseMudCateg', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrBcCPrev = TagDecimal(nome='vrBcCPrev', tamanho=[1, 14, 2], raiz='//baseMudCateg', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<baseMudCateg>'
        xml += self.codCateg.xml
        xml += self.vrBcCPrev.xml
        xml += '</baseMudCateg>'

        return xml


class InfoFGTS(XMLNFe):
    def __init__(self):
        super(InfoFGTS, self).__init__()
        self.vrBcFgtsGuia = TagDecimal(nome='vrBcFgtsGuia', tamanho=[1, 14, 2], raiz='//infoFGTS', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrBcFgts13Guia = TagDecimal(nome='vrBcFgts13Guia', tamanho=[1, 14, 2], raiz='//infoFGTS', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.pagDireto = TagCaracter(nome='pagDireto', tamanho=[1, 2], raiz='//infoFGTS', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoFGTS>'
        xml += self.vrBcFgtsGuia.xml
        xml += self.vrBcFgts13Guia.xml
        xml += self.pagDireto.xml
        xml += '</infoFGTS>'

        return xml


class InfoAgNocivo(XMLNFe):
    def __init__(self):
        super(InfoAgNocivo, self).__init__()
        self.grauExp = TagInteiro(nome='grauExp', raiz='//infoAgNocivo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoAgNocivo>'
        xml += self.grauExp.xml
        xml += '</infoAgNocivo>'

        return xml


class BaseCalculo(XMLNFe):
    def __init__(self):
        super(BaseCalculo, self).__init__()
        self.vrBcCpMensal = TagDecimal(nome='vrBcCpMensal', tamanho=[1, 14, 2], raiz='//baseCalculo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrBcCp13 = TagDecimal(nome='vrBcCp13', tamanho=[1, 14, 2], raiz='//baseCalculo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrBcFgts = TagDecimal(nome='vrBcFgts', tamanho=[1, 14, 2], raiz='//baseCalculo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrBcFgts13 = TagDecimal(nome='vrBcFgts13', tamanho=[1, 14, 2], raiz='//baseCalculo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.infoAgNocivo = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<baseCalculo>'
        xml += self.vrBcCpMensal.xml
        xml += self.vrBcCp13.xml
        xml += self.vrBcFgts.xml
        xml += self.vrBcFgts13.xml
        for agente_nocivo in self.infoAgNocivo:
            xml += agente_nocivo.xml
        xml += '</baseCalculo>'

        return xml


class IdePeriodo(XMLNFe):
    def __init__(self):
        super(IdePeriodo, self).__init__()
        self.perRef = TagCaracter(nome='perRef', tamanho=[1, 7], raiz='//idePeriodo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.baseCalculo = BaseCalculo()
        self.infoFGTS = []
        self.baseMudCateg = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<idePeriodo>'
        xml += self.perRef.xml
        for fgts in self.infoFGTS:
            xml += fgts.xml
        for base_mudanca in self.baseMudCateg:
            xml += base_mudanca.xml
        xml += '</idePeriodo>'

        return xml


class InfoVlr(XMLNFe):
    def __init__(self):
        self.compIni = TagCaracter(nome='compIni', tamanho=[1, 7], raiz='//InfoVlr', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.compFim = TagCaracter(nome='compFim', tamanho=[1, 7], raiz='//InfoVlr', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.repercProc = TagInteiro(nome='repercProc', raiz='//InfoVlr', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrRemun = TagInteiro(nome='vrRemun', raiz='//InfoVlr', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrAPI = TagInteiro(nome='vrAPI', raiz='//InfoVlr', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vr13API = TagInteiro(nome='vr13API', raiz='//InfoVlr', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrInden = TagInteiro(nome='vrInden', raiz='//InfoVlr', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrBaseIndenFGTS = TagInteiro(nome='vrBaseIndenFGTS', raiz='//InfoVlr', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.pagDiretoResc = TagCaracter(nome='pagDiretoResc', tamanho=[1, 2], raiz='//InfoVlr', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.idePeriodo = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoVlr>'
        xml += self.compIni.xml
        xml += self.compFim.xml
        xml += self.repercProc.xml
        xml += self.vrRemun.xml
        xml += self.vrAPI.xml
        xml += self.vr13API.xml
        xml += self.vrInden.xml
        xml += self.vrBaseIndenFGTS.xml
        xml += self.pagDiretoResc.xml
        for periodo in self.idePeriodo:
            xml += periodo.xml

        return xml


class IdeEstab(XMLNFe):
    def __init__(self):
        super(IdeEstab, self).__init__()
        self.tpInsc = TagInteiro(nome='tpInsc', raiz='//ideEstab', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nrInsc = TagCaracter(nome='nrInsc', tamanho=[1, 14], raiz='//ideEstab', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.infoVlr = InfoVlr()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideEstab>'
        xml += self.tpInsc.xml
        xml += self.nrInsc.xml
        xml += '</ideEstab>'

        return xml

class UnicContr(XMLNFe):
    def __init__(self):
        super(UnicContr, self).__init__()
        self.matUnic = TagCaracter(nome='matUnic', tamanho=[1, 30], raiz='//unicContr', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.codCateg = TagInteiro(nome='codCateg', raiz='//unicContr', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.dtInicio = TagData(nome='dtInicio', raiz='//unicContr', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<unicContr>'
        xml += self.matUnic.xml
        xml += self.codCateg.xml
        xml += self.dtInicio.xml

        return xml

class MudCategAtiv(XMLNFe):
    def __init__(self):
        super(MudCategAtiv, self).__init__()
        self.codCateg = TagInteiro(nome='codCateg', raiz='//mudCategAtiv', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.natAtividade = TagInteiro(nome='natAtividade', raiz='//mudCategAtiv', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.dtMudCategAtiv = TagData(nome='dtMudCategAtiv', raiz='//mudCategAtiv', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<mudCategAtiv>'
        xml += self.codCateg.xml
        xml += self.natAtividade.xml
        xml += self.dtMudCategAtiv.xml
        xml += '</mudCategAtiv>'

        return xml


class InfoTerm(XMLNFe):
    def __init__(self):
        super(InfoTerm, self).__init__()
        self.dtTerm = TagData(nome='dtTerm', raiz='//infoTerm', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.mtvDesligTSV = TagCaracter(nome='mtvDesligTSV', tamanho=[1, 2], raiz='//infoTerm', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoTerm>'
        xml += self.dtTerm.xml
        xml += self.mtvDesligTSV.xml
        xml += '</infoTerm>'

        return xml


class InfoDeslig(XMLNFe):
    def __init__(self):
        super(InfoDeslig, self).__init__()
        self.dtDeslig = TagData(nome='dtDeslig', raiz='//infoDeslig', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.mtvDeslig = TagCaracter(nome='mtvDeslig', tamanho=[1, 2], raiz='//infoDeslig', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dtProjFimAPI = TagData(nome='dtDeslig', raiz='//infoDeslig', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoDeslig>'
        xml += self.dtDeslig.xml
        xml += self.mtvDeslig.xml
        xml += self.dtProjFimAPI.xml
        xml += '</infoDeslig>'

        return xml

    xml = property(get_xml)


class SucessaoVinc(XMLNFe):
    def __init__(self):
        super(SucessaoVinc, self).__init__()
        self.tpInsc = TagInteiro(nome='tpInsc', raiz='//sucessaoVinc', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nrInsc = TagCaracter(nome='nrInsc', tamanho=[8, 14], raiz='//sucessaoVinc', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.matricAnt = TagCaracter(nome='matricAnt', tamanho=[1, 30], raiz='//sucessaoVinc', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.dtTransf = TagData(nome='dtTransf', raiz='//sucessaoVinc', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<sucessaoVinc>'
        xml += self.tpInsc.xml
        xml += self.nrInsc.xml
        xml += self.matricAnt.xml
        xml += self.dtTransf.xml
        xml += '</sucessaoVinc>'

        return xml

    xml = property(get_xml)

class Observacoes(XMLNFe):
    def __init__(self):
        super(Observacoes, self).__init__()
        self.observacao = TagCaracter(nome='observacao', tamanho=[1, 255], raiz='//observacoes', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<observacoes>'
        xml += self.observacao.xml
        xml += '</observacoes>'

        return xml

    xml = property(get_xml)

class Duracao(XMLNFe):
    def __init__(self):
        super(Duracao, self).__init__()
        self.tpContr = TagInteiro(nome='tpContr', raiz='//duracao', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dtTerm = TagData(nome='dtTerm', raiz='//duracao', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.clauAssec = TagCaracter(nome='clauAssec', tamanho=[1, 1], raiz='//duracao', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.objDet = TagCaracter(nome='objDet', tamanho=[1, 255], raiz='//duracao', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<duracao>'
        xml += self.tpContr.xml
        xml += self.dtTerm.xml
        xml += self.clauAssec.xml
        xml += self.objDet.xml
        xml += '</duracao>'

        return xml

    xml = property(get_xml)


class InfoVinc(XMLNFe):
    def __init__(self):
        super(InfoVinc, self).__init__()
        self.tpRegTrab = TagInteiro(nome='tpRegTrab', raiz='//infoVinc', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.tpRegPrev = TagInteiro(nome='tpRegPrev', raiz='//infoVinc', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dtAdm = TagData(nome='tpRegPrev', raiz='//infoVinc', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.tmpParc = TagInteiro(nome='tmpParc', raiz='//infoVinc', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.duracao = Duracao()
        self.observacoes = []
        self.sucessaoVinc = []
        self.infoDeslig = InfoDeslig()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoVinc>'
        xml += self.tpRegTrab.xml
        xml += self.tpRegPrev.xml
        xml += self.dtAdm.xml
        xml += self.tmpParc.xml
        xml += self.duracao.xml
        for observacao in self.observacoes:
            xml += observacao.xml
        for sucessao_vinculo in self.sucessaoVinc:
            xml += sucessao_vinculo.xml
        xml += self.infoDeslig.xml
        xml += '</infoVinc>'

        return xml

    xml = property(get_xml)


class Remuneracao(XMLNFe):
    def __init__(self):
        super(Remuneracao, self).__init__()
        self.dtRemun = TagData(nome='dtRemun', raiz='//remuneracao', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrSalFx = TagDecimal(nome='vrSalFx', tamanho=[1, 14, 2], raiz='//remuneracao', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.undSalFixo = TagInteiro(nome='undSalFixo', raiz='//remuneracao', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dscSalVar = TagCaracter(nome='dscSalVar', tamanho=[1, 999], raiz='//remuneracao', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<remuneracao>'
        xml += self.dtRemun.xml
        xml += self.vrSalFx.xml
        xml += self.undSalFixo.xml
        xml += self.dscSalVar.xml
        xml += '</remuneracao>'

        return xml

    xml = property(get_xml)

class InfoCompl(XMLNFe):
    def __init__(self):
        super(InfoCompl, self).__init__()
        self.codCBO = TagCaracter(nome='codCBO', tamanho=[1, 6], raiz='//infCompl', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.natAtividade = TagInteiro(nome='natAtividade', raiz='//infCompl', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.remuneracao = []
        self.infoVinc = []
        self.infoTerm = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infCompl>'
        xml += self.codCBO.xml
        xml += self.natAtividade.xml
        for remuneracao in self.remuneracao:
            xml += remuneracao.xml
        for info_vinc in self.infoVinc:
            xml += info_vinc.xml
        for info_termino in self.infoTerm:
            xml += info_termino.xml
        xml += '</infCompl>'

        return xml

    xml = property(get_xml)

class InfoContr(XMLNFe):
    def __init__(self):
        super(InfoContr, self).__init__()
        self.tpContr = TagInteiro(nome='tpContr', raiz='//infoContr', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.indContr = TagCaracter(nome='indContr', tamanho=[1, 1], raiz='//infoContr', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dtAdmOrig = TagData(nome='dtAdmOrig', raiz='//infoContr', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.indReint = TagCaracter(nome='indReint', tamanho=[1, 1], raiz='//infoContr', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.indCateg = TagCaracter(nome='indCateg', tamanho=[1, 1], raiz='//infoContr', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.indNatAtiv = TagCaracter(nome='indNatAtiv', tamanho=[1, 1], raiz='//infoContr', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.indMotDeslig = TagCaracter(nome='indMotDeslig', tamanho=[1, 1], raiz='//infoContr', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.indUnic = TagCaracter(nome='indUnic', tamanho=[1, 1], raiz='//infoContr', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.matricula = TagCaracter(nome='matricula', tamanho=[1, 30], raiz='//infoContr', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.codCateg = TagInteiro(nome='codCateg',  raiz='//infoContr', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.dtInicio = TagData(nome='dtInicio', raiz='//infoContr', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.infoCompl = InfoCompl()
        self.mudCategAtiv = []
        self.unicContr = []
        self.ideEstab = IdeEstab()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoContr>'
        xml += self.tpContr.xml
        xml += self.indContr.xml
        xml += self.dtAdmOrig.xml
        xml += self.indReint.xml
        xml += self.indCateg.xml
        xml += self.indNatAtiv.xml
        xml += self.indMotDeslig.xml
        xml += self.indUnic.xml
        xml += self.matricula.xml
        xml += self.codCateg.xml
        xml += self.dtInicio.xml
        xml += self.infoCompl.xml
        for mudanca_categ_ativ in self.mudCategAtiv:
            xml += mudanca_categ_ativ.xml
        for unicidade_contratual in self.unicContr:
            xml += unicidade_contratual.xml
        xml += self.ideEstab.xml
        xml += '</infoContr>'

        return xml

    xml = property(get_xml)


class Dependente(XMLNFe):
    def __init__(self):
        super(Dependente, self).__init__()
        self.cpfDep = TagCaracter(nome='cpfDep', tamanho=[1, 11], raiz='//dependente', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.tpDep = TagCaracter(nome='tpDep', tamanho=[1, 2], raiz='//dependente', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.descDep = TagCaracter(nome='descDep', tamanho=[1, 11], raiz='//dependente', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<dependente>'
        xml += self.cpfDep.xml
        xml += self.tpDep.xml
        xml += self.descDep.xml
        xml += '</dependente>'

        return xml

    xml = property(get_xml)


class IdeTrab(XMLNFe):
    def __init__(self):
        super(IdeTrab, self).__init__()
        self.cpfTrab = TagCaracter(nome='cpfTrab', tamanho=[1, 11], raiz='//eSocial/evtProcTrab/ideTrab/cpfTrab', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nmTrab = TagCaracter(nome='nmTrab', tamanho=[1, 100], raiz='//eSocial/evtProcTrab/ideTrab/nmTrab', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dtNascto = TagData(nome='dtNascto', raiz='//eSocial/evtProcTrab/ideTrab/infoCCP', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.dependente = []
        self.infoContr = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideTrab>'
        xml += self.cpfTrab.xml
        xml += self.nmTrab.xml
        xml += self.dtNascto.xml
        for dependente in self.dependente:
            xml += dependente.xml
        for info_contrato in self.infoContr:
            xml += info_contrato.xml
        xml += '</ideTrab>'

        return xml

    xml = property(get_xml)


class InfoCCP(XMLNFe):
    def __init__(self):
        super(InfoCCP, self).__init__()
        self.dtCCP = TagData(nome='dtCCP', raiz='//eSocial/evtProcTrab/infoProcesso/infoCCP', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.tpCCP = TagInteiro(nome='tpCCP', raiz='//eSocial/evtProcTrab/infoProcesso/infoCCP', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.cnpjCCP = TagCaracter(nome='cnpjCCP', tamanho=[1, 14], raiz='//eSocial/evtProcTrab/infoProcesso/infoCCP', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoCCP>'
        xml += self.dtCCP.xml
        xml += self.tpCCP.xml
        xml += self.cnpjCCP.xml
        xml += '</infoCCP>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.dtCCP.xml = arquivo
            self.tpCCP.xml = arquivo
            self.cnpjCCP.xml = arquivo

    xml = property(get_xml)


class InfoProcJud(XMLNFe):
    def __init__(self):
        super(InfoProcJud, self).__init__()
        self.dtSent = TagData(nome='dtSent', raiz='//eSocial/evtProcTrab/infoProcesso/infoProcJud', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ufVara = TagCaracter(nome='ufVara', tamanho=[1, 2], raiz='//eSocial/evtProcTrab/infoProcesso/infoProcJud', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.codMunic = TagInteiro(nome='codMunic', raiz='//eSocial/evtProcTrab/infoProcesso/infoProcJud', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.idVara = TagInteiro(nome='idVara', raiz='//eSocial/evtProcTrab/infoProcesso/infoProcJud', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoProcJud>'
        xml += self.dtSent.xml
        xml += self.ufVara.xml
        xml += self.codMunic.xml
        xml += self.idVara.xml
        xml += '</infoProcJud>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.dtSent.xml = arquivo
            self.ufVara.xml = arquivo
            self.codMunic.xml = arquivo
            self.idVara.xml = arquivo

    xml = property(get_xml, set_xml)


class DadosCompl(XMLNFe):
    def __init__(self):
        super(DadosCompl, self).__init__()
        self.infoProcJud = InfoProcJud()
        self.infoCCP = InfoCCP()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<dadosCompl>'
        xml += self.infoProcJud.xml
        xml += self.infoCCP.xml
        xml += '</dadosCompl>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.infoProcJud.xml = arquivo
            self.infoCCP.xml = arquivo

    xml = property(get_xml, set_xml)


class InfoProcesso(XMLNFe):
    def __init__(self):
        super(InfoProcesso, self).__init__()
        self.origim = TagInteiro(nome='origim', raiz='//eSocial/evtProcTrab/infoProcesso', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nrProcTrab = TagCaracter(nome='nrProcTrab', tamanho=[1, 20], raiz='//eSocial/evtProcTrab/infoProcesso', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.obsProcTrab = TagCaracter(nome='obsProcTrab', tamanho=[1, 999], raiz='//eSocial/evtProcTrab/infoProcesso', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.dadosCompl = DadosCompl()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoProcesso>'
        xml += self.origim.xml
        xml += self.nrProcTrab.xml
        xml += self.obsProcTrab.xml
        xml += self.dadosCompl.xml
        xml += '</infoProcesso>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.origim.xml = arquivo
            self.nrProcTrab.xml = arquivo
            self.obsProcTrab.xml = arquivo
            self.dadosCompl.xml = arquivo

    xml = property(get_xml, set_xml)


class IdeEmpregador(XMLNFe):
    def __init__(self):
        super(IdeEmpregador, self).__init__()
        self.tpInsc = TagCaracter(nome='tpInsc', raiz='//eSocial/evtProcTrab/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor='1')
        self.nrInsc = TagCaracter(nome='nrInsc', raiz='//eSocial/evtProcTrab/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

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
        self.indRetif = TagInteiro( nome='indRetif', raiz='//eSocial/evtProcTrab/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=1)
        self.nrRecibo = TagCaracter(nome='nrRecibo', raiz='//eSocial/evtProcTrab/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.tpAmb    = TagInteiro( nome='tpAmb'   , raiz='//eSocial/evtProcTrab/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=2)
        self.procEmi  = TagInteiro( nome='procEmi' , raiz='//eSocial/evtProcTrab/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=1)
        self.verProc  = TagCaracter(nome='verProc' , raiz='//eSocial/evtProcTrab/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

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


class EvtProcTrab(XMLNFe):
    def __init__(self):
        super(EvtProcTrab, self).__init__()
        self.Id = TagCaracter(nome='evtProcTrab', propriedade='Id', raiz='//eSocial/evtProcTrab', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ideEvento = IdeEvento()
        self.ideEmpregador = IdeEmpregador()
        self.infoProcesso = InfoProcesso()
        self.ideTrab = IdeTrab()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.Id.xml
        xml += self.ideEvento.xml
        xml += self.ideEmpregador.xml
        xml += self.infoProcesso.xml
        xml += self.ideTrab.xml
        xml += '</evtProcTrab>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml = arquivo
            self.ideEvento.xml = arquivo
            self.ideEmpregador.xml = arquivo
            self.infoProcesso.xml = arquivo
            self.ideTrab.xml = arquivo

    xml = property(get_xml, set_xml)


class S2500(XMLNFe):
    def __init__(self):
        super(S2500, self).__init__()
        self.evtProcTrab = EvtProcTrab()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'evtProcTrab.xsd'
        self.id_evento = ''
        self.tpInsc = ''
        self.nrInsc = ''
        # self.Signature = Signature()
        self.evento = self.evtProcTrab
        self.xml_assinado = ''

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        #xml += ABERTURA
        xml += '<eSocial xmlns="' + NAMESPACE_ESOCIAL + '">'
        xml += self.evtProcTrab.xml

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
            self.evtProcTrab.xml = arquivo
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
        self.evtProcTrab.Id.valor = id_evento
        self.id_evento = id_evento

    xml = property(get_xml, set_xml)
