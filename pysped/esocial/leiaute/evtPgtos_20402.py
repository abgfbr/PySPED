# -*- coding: utf-8 -*-
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
from pysped.xml_sped.base import XMLNFe, TagData, TagCaracter, TagDecimal, TagInteiro

from pysped.esocial.leiaute import ESQUEMA_ATUAL_VERSAO_2 as ESQUEMA_ATUAL

DIRNAME = os.path.dirname(__file__)

NAMESPACE_ESOCIAL = 'http://www.esocial.gov.br/schema/evt/evtPgtos/v_S_01_03_00'


class InfoPgto(XMLNFe):
    def __init__(self):
        super(InfoPgto, self).__init__()
        self.dtPgto    = TagData(    nome='dtPgto',                   raiz='//infoPgto', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.tpPgto    = TagCaracter(nome='tpPgto',   tamanho=[1, 2], raiz='//infoPgto', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.perRef    = TagCaracter(nome='perRef', tamanho=[4,7], raiz='//infoPgto', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ideDmDev  = TagCaracter(nome='ideDmDev', tamanho=[1,30], raiz='//infoPgto', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vrLiq     = TagDecimal(nome='vrLiq', tamanho=[1, 14, 2], raiz='//infoPgto', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoPgto>'
        xml += self.dtPgto.xml
        xml += self.tpPgto.xml
        xml += self.perRef.xml
        xml += self.ideDmDev.xml
        xml += self.vrLiq.xml
        xml += '</infoPgto>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.dtPgto.xml = arquivo
            self.tpPgto.xml = arquivo
            self.perRef.xml = arquivo
            self.ideDmDev.xml = arquivo
            self.vrLiq.xml = arquivo

    xml = property(get_xml, set_xml)


class PerAnt(XMLNFe):
    def __init__(self):
        super(PerAnt, self).__init__()
        self.perRefAjuste = TagCaracter(nome='perRefAjuste', tamanho=[1,7], raiz='//eSocial/evtPgtos/ideBenef/infoIRComplem/perAnt', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nrRec1210Orig = TagCaracter(nome='nrRec1210Orig', tamanho=[1, 23], raiz='//eSocial/evtPgtos/ideBenef/infoIRComplem/perAnt', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<perAnt>'
        xml += self.perRefAjuste.xml
        xml += self.nrRec1210Orig.xml
        xml += '</perAnt>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.perRefAjuste.xml = arquivo
            self.nrRec1210Orig.xml = arquivo

    xml = property(get_xml, set_xml)


class InfoDep(XMLNFe):
    def __init__(self):
        super(InfoDep, self).__init__()
        self.cpfDep  = TagCaracter(nome='cpfDep', tamanho=[1, 11], raiz='//eSocial/evtPgtos/ideBenef/infoIRComplem/infoDep/cpfDep', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dtNascto  = TagData(nome='dtNascto', raiz='//eSocial/evtPgtos/ideBenef/infoIRComplem/infoDep/dtNascto', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.nome  = TagCaracter(nome='nome', tamanho=[2, 70], raiz='//eSocial/evtPgtos/ideBenef/infoIRComplem/infoDep/nome', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.depIRRF  = TagCaracter(nome='depIRRF', tamanho=[1, 1], raiz='//eSocial/evtPgtos/ideBenef/infoIRComplem/infoDep/dpIRRF', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.tpDep  = TagCaracter(nome='tpDep', tamanho=[1, 2], raiz='//eSocial/evtPgtos/ideBenef/infoIRComplem/infoDep/tpDep', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.descrDep  = TagCaracter(nome='descrDep', tamanho=[1, 100], raiz='//eSocial/evtPgtos/ideBenef/infoIRComplem/infoDep/descrDep', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoDep>'
        xml += self.cpfDep.xml
        xml += self.dtNascto.xml
        xml += self.nome.xml
        xml += self.depIRRF.xml
        xml += self.tpDep.xml
        xml += self.descrDep.xml
        xml += '</infoDep>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cpfDep.xml = arquivo
            self.dtNascto.xml = arquivo
            self.nome.xml = arquivo
            self.depIRRF.xml = arquivo
            self.tpDep.xml = arquivo
            self.descrDep.xml = arquivo

    xml = property(get_xml, set_xml)


class InfoDepSau(XMLNFe):
    def __init__(self):
        super(InfoDepSau, self).__init__()
        self.cpfDep = TagCaracter(nome='cpfDep', tamanho=[1, 11], raiz='//eSocial/evtPgtos/ideBenef/infoIRComplem/infoDepSau/cpfDep', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vlrSaudeDep = TagCaracter(nome='vlrSaudeDep', tamanho=[1, 14], raiz='//eSocial/evtPgtos/ideBenef/infoIRComplem/infoDepSau/vlrSaudeDep', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoDepSau>'
        xml += self.cpfDep.xml
        xml += self.vlrSaudeDep.xml
        xml += '</infoDepSau>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cpfDep.xml = arquivo
            self.vlrSaudeDep.xml = arquivo

    xml = property(get_xml, set_xml)


class PlanSaude(XMLNFe):
    def __init__(self):
        super(PlanSaude, self).__init__()
        self.cnpjOper = TagCaracter(nome='cnpjOper', tamanho=[1, 14], raiz='//eSocial/evtPgtos/ideBenef/infoIRComplem/planSaude/cnpjOper', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.regANS = TagCaracter(nome='regANS', tamanho=[1, 6], raiz='//eSocial/evtPgtos/ideBenef/infoIRComplem/planSaude/regANS', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.vlrSaudeTit = TagCaracter(nome='vlrSaudeTit', tamanho=[1, 14], raiz='//eSocial/evtPgtos/ideBenef/infoIRComplem/planSaude/vlrSaudeTit', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.infoDepSau = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<planSaude>'
        xml += self.cnpjOper.xml
        xml += self.regANS.xml
        xml += self.vlrSaudeTit.xml
        for infoDep in self.infoDepSau:
            xml += infoDep.xml
        xml += '</planSaude>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cnpjOper.xml = arquivo
            self.regANS.xml = arquivo
            self.vlrSaudeTit.xml = arquivo
            self.infoDepSau = self.le_grupo('//eSocial/evtPgtos/ideBenef/infoIRComplem/infoReembMed/infoDepSau', InfoDepSau, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class DetReembTit(XMLNFe):
    def __init__(self):
        super(DetReembTit, self).__init__()
        self.tpInsc  = TagCaracter(nome='tpInsc', tamanho=[1, 1], raiz='//eSocial/evtPgtos/ideBenef/infoIRComplem/infoReembMed/detReembTit/tpInsc', namespace=NAMESPACE_ESOCIAL)
        self.nrInsc  = TagCaracter(nome='nrInsc', tamanho=[1, 14], raiz='//eSocial/evtPgtos/ideBenef/infoIRComplem/infoReembMed/detReembTit/nrInsc', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vlrReemb  = TagDecimal(nome='vlrReemb', tamanho=[1, 14, 2], raiz='//eSocial/evtPgtos/ideBenef/infoIRComplem/infoReembMed/detReembTit/vlrReemb', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.vlrReembAnt  = TagDecimal(nome='vlrReembAnt', tamanho=[1, 14, 2], raiz='//eSocial/evtPgtos/ideBenef/infoIRComplem/infoReembMed/detReembTit/vlrReembAnt', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<detReembTit>'
        xml += self.tpInsc.xml
        xml += self.nrInsc.xml
        xml += self.vlrReemb.xml
        xml += self.vlrReembAnt.xml
        xml += '</detReembTit>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpInsc.xml = arquivo
            self.nrInsc.xml = arquivo
            self.vlrReemb.xml = arquivo
            self.vlrReembAnt.xml = arquivo

    xml = property(get_xml, set_xml)


class InfoReembDep(XMLNFe):
    def __init__(self):
        super(InfoReembDep, self).__init__()
        self.cpfBenef  = TagCaracter(nome='cpfBenef', tamanho=[1, 11], raiz='//eSocial/evtPgtos/ideBenef/infoIRComplem/infoReembMed/infoReembDep/cpfBenef', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoReembDep>'
        xml += self.cpfBenef.xml
        xml += '</infoReembDep>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cpfBenef.xml = arquivo

    xml = property(get_xml, set_xml)


class InfoReembMed(XMLNFe):
    def __init__(self):
        super(InfoReembMed, self).__init__()
        self.indOrgReemb  = TagCaracter(nome='indOrgReemb', tamanho=[1, 1], raiz='//eSocial/evtPgtos/ideBenef/infoIRComplem/infoReembMed/indOrgReemb', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.cnpjOper  = TagCaracter(nome='cnpjOper', tamanho=[1, 14],raiz='//eSocial/evtPgtos/ideBenef/infoIRComplem/infoReembMed/cnpjOper', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.regANS  = TagCaracter(nome='regANS', tamanho=[1, 6],raiz='//eSocial/evtPgtos/ideBenef/infoIRComplem/infoReembMed/regANS', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.detReembTit = []
        self.infoReembDep = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoReembMed>'
        xml += self.indOrgReemb.xml
        xml += self.cnpjOper.xml
        xml += self.regANS.xml
        for d in self.detReembTit:
            xml += d.xml
        for i in self.infoReembDep:
            xml += i.xml
        xml += '</infoReembMed>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.indOrgReemb.xml = arquivo
            self.cnpjOper.xml = arquivo
            self.regANS.xml = arquivo
            self.detReembTit = self.le_grupo('//eSocial/evtPgtos/ideBenef/infoIRComplem/infoReembMed/detReembTit', DetReembTit, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.infoReembDep = self.le_grupo('//eSocial/evtPgtos/ideBenef/infoIRComplem/infoReembMed/infoReembDep', InfoReembDep, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class InfoIRComplem(XMLNFe):
    def __init__(self):
        super(InfoIRComplem, self).__init__()
        self.dtLaudo  = TagData(nome='dtLaudo', raiz='//eSocial/evtPgtos/ideBenef/infoIRComplem/dtLaudo', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.perAnt = []
        self.infoDep = []
        self.infoIRCR = []
        self.planSaude = []
        self.infoReembMed = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoIRComplem>'
        if self.dtLaudo.xml:
            xml += self.dtLaudo.xml
        for p in self.perAnt:
            xml += p.xml
        for p in self.infoDep:
            xml += p.xml
        for p in self.infoIRCR:
            xml += p.xml
        for pl in self.planSaude:
            xml += pl.xml
        for i in self.infoReembMed:
            xml += i.xml
        xml += '</infoIRComplem>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.dtLaudo.xml = arquivo
            self.perAnt = self.le_grupo('//eSocial/evtPgtos/ideBenef/infoIRComplem/perAnt', PerAnt, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.infoDep = self.le_grupo('//eSocial/evtPgtos/ideBenef/infoIRComplem/infoDep', InfoDep, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.infoIRCR = self.le_grupo('//eSocial/evtPgtos/ideBenef/infoIRComplem/infoIRCR', InfoIRCR, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.planSaude = self.le_grupo('//eSocial/evtPgtos/ideBenef/infoIRComplem/planSaude', PlanSaude, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.infoReembMed = self.le_grupo('//eSocial/evtPgtos/ideBenef/infoIRComplem/infoReembMed', InfoReembMed, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class DedDepen(XMLNFe):
    def __init__(self):
        super(DedDepen, self).__init__()
        self.tpRend  = TagCaracter(nome='tpRend', tamanho=[1, 2], raiz='//eSocial/evtPgtos/ideBenef/infoIRComplem/infoIRCR/dedDepen/tpRend', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.cpfDep  = TagCaracter(nome='cpfDep', tamanho=[1, 15], decimais=2, raiz='//eSocial/evtPgtos/ideBenef/infoIRComplem/infoIRCR/dedDepen/cpfDep', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vlrDedDep  = TagDecimal(nome='vlrDedDep', tamanho=[1, 14], decimais=2, raiz='//eSocial/evtPgtos/ideBenef/infoIRComplem/infoIRCR/dedDepen/vlrDedDep', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<dedDepen>'
        xml += self.tpRend.xml
        xml += self.cpfDep.xml
        xml += self.vlrDedDep.xml
        xml += '</dedDepen>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpRend.xml = arquivo
            self.cpfDep.xml = arquivo
            self.vlrDedDep.xml = arquivo

    xml = property(get_xml, set_xml)


class PenAlim(XMLNFe):
    def __init__(self):
        super(PenAlim, self).__init__()
        self.tpRend = TagCaracter(nome='tpRend', tamanho=[1, 2], raiz='//eSocial/evtPgtos/ideBenef/infoIRComplem/infoIRCR/penAlim/tpRend', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.cpfDep = TagCaracter(nome='cpfDep', tamanho=[1, 11], raiz='//eSocial/evtPgtos/ideBenef/infoIRComplem/infoIRCR/penAlim/cpfDep', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vlrDedPenAlim = TagDecimal(nome='vlrDedPenAlim', tamanho=[1, 14, 2], raiz='//eSocial/evtPgtos/ideBenef/infoIRComplem/infoIRCR/penAlim/vlrDedPenAlim', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<penAlim>'
        xml += self.tpRend.xml
        xml += self.cpfDep.xml
        xml += self.vlrDedPenAlim.xml
        xml += '</penAlim>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpRend.xml = arquivo
            self.cpfDep.xml = arquivo
            self.vlrDedPenAlim.xml = arquivo

    xml = property(get_xml, set_xml)


class PrevidCompl(XMLNFe):
    def __init__(self):
        super(PrevidCompl, self).__init__()
        self.tpPrev  = TagCaracter(nome='tpPrev', tamanho=[1, 1], raiz='//eSocial/evtPgtos/ideBenef/infoIRComplem/infoIRCR/previdCompl/tpPrev', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.cnpjEntidPC  = TagCaracter(nome='cnpjEntidPC', tamanho=[1, 14], raiz='//eSocial/evtPgtos/ideBenef/infoIRComplem/infoIRCR/previdCompl/cnpjEntidPC', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vlrDedPC  = TagDecimal(nome='vlrDedPC', tamanho=[1, 14, 2], raiz='//eSocial/evtPgtos/ideBenef/infoIRComplem/infoIRCR/previdCompl/vlrDedPC', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vlrDedPC13  = TagDecimal(nome='vlrDedPC13', tamanho=[1, 14, 2], raiz='//eSocial/evtPgtos/ideBenef/infoIRComplem/infoIRCR/previdCompl/vlrDedPC13', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vlrPatrocFunp  = TagDecimal(nome='vlrPatrocFunp', tamanho=[1, 14, 2], raiz='//eSocial/evtPgtos/ideBenef/infoIRComplem/infoIRCR/previdCompl/vlrPatrocFunp', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.vlrPatrocFunp13  = TagDecimal(nome='vlrPatrocFunp13', tamanho=[1, 14, 2], raiz='//eSocial/evtPgtos/ideBenef/infoIRComplem/infoIRCR/previdCompl/vlrPatrocFunp13', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<previdCompl>'
        xml += self.tpPrev.xml
        xml += self.cnpjEntidPC.xml
        xml += self.vlrDedPC.xml
        xml += self.vlrDedPC13.xml
        xml += self.vlrPatrocFunp.xml
        xml += self.vlrPatrocFunp13.xml
        xml += '</previdCompl>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpPrev.xml = arquivo
            self.cnpjEntidPC.xml = arquivo
            self.vlrDedPC.xml = arquivo
            self.vlrDedPC13.xml = arquivo
            self.vlrPatrocFunp.xml = arquivo
            self.vlrPatrocFunp13.xml = arquivo

    xml = property(get_xml, set_xml)


class InfoProcRet(XMLNFe):
    def __init__(self):
        super(InfoProcRet, self).__init__()
        self.tpProcRet  = TagCaracter(nome='tpProcRet', tamanho=[1, 1], raiz='//eSocial/evtPgtos/ideBenef/infoIRComplem/infoIRCR/infoProcRet/tpProcRet', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.nrProcRet  = TagCaracter(nome='nrProcRet', tamanho=[1, 21], raiz='//eSocial/evtPgtos/ideBenef/infoIRComplem/infoIRCR/infoProcRet/nrProcRet', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.codSusp  = TagCaracter(nome='codSusp', tamanho=[1, 14], raiz='//eSocial/evtPgtos/ideBenef/infoIRComplem/infoIRCR/infoProcRet/codSusp', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoProcRet>'
        xml += self.tpProcRet.xml
        xml += self.nrProcRet.xml
        xml += self.codSusp.xml if self.codSusp.valor else ''
        xml += '</infoProcRet>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpProcRet.xml = arquivo
            self.nrProcRet.xml = arquivo
            self.codSusp.xml = arquivo

    xml = property(get_xml, set_xml)


class InfoIRCR(XMLNFe):
    def __init__(self):
        super(InfoIRCR, self).__init__()
        self.tpCR  = TagCaracter(nome='tpCR', tamanho=[1, 6], raiz='//eSocial/evtPgtos/ideBenef/infoIRComplem/infoIRCR/tpCR', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.dedDepen  = []
        self.penAlim = []
        self.previdCompl = []
        self.infoProcRet = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoIRCR>'
        xml += self.tpCR.xml
        for p in self.dedDepen:
            xml += p.xml
        for p in self.penAlim:
            xml += p.xml
        for p in self.previdCompl:
            xml += p.xml
        for p in self.infoProcRet:
            xml += p.xml
        xml += '</infoIRCR>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.tpCR.xml = arquivo
            self.dedDepen = self.le_grupo('//eSocial/evtPgtos/ideBenef/infoIRComplem/infoIRCR/dedDepen', DedDepen, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.penAlim = self.le_grupo('//eSocial/evtPgtos/ideBenef/infoIRComplem/infoIRCR/penAlim', PenAlim, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.previdCompl = self.le_grupo('//eSocial/evtPgtos/ideBenef/infoIRComplem/infoIRCR/previdCompl', PrevidCompl, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.infoProcRet = self.le_grupo('//eSocial/evtPgtos/ideBenef/infoIRComplem/infoIRCR/infoProcRet', InfoProcRet, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class IdeBenef(XMLNFe):
    def __init__(self):
        super(IdeBenef, self).__init__()
        self.cpfBenef       = TagCaracter(nome='cpfBenef', tamanho=[1, 11],    raiz='//eSocial/evtPgtos/ideBenef',      namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.infoPgto       = []
        self.infoIRComplem  = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideBenef>'
        xml += self.cpfBenef.xml
        if len(self.infoPgto) > 0:
            for p in self.infoPgto:
                xml += p.xml
        for info_ir_complem in self.infoIRComplem:
            xml += info_ir_complem.xml
        xml += '</ideBenef>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cpfBenef.xml = arquivo
            self.infoPgto = self.le_grupo('//eSocial/evtPgtos/ideBenef/infoPgto', InfoPgto, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')
            self.infoIRComplem = self.le_grupo('//eSocial/evtPgtos/ideBenef/infoIRComplem', InfoIRComplem, namespace=NAMESPACE_ESOCIAL, sigla_ns='res')

    xml = property(get_xml, set_xml)


class IdeEmpregador(XMLNFe):
    def __init__(self):
        super(IdeEmpregador, self).__init__()
        self.tpInsc = TagCaracter(nome='tpInsc', tamanho=[1, 1],  raiz='//eSocial/evtPgtos/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor='1')
        self.nrInsc = TagCaracter(nome='nrInsc', tamanho=[1, 15], raiz='//eSocial/evtPgtos/ideEmpregador', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

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
        self.indRetif    = TagInteiro( nome='indRetif',    tamanho=[1,  1], raiz='//eSocial/evtPgtos/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=1)
        self.nrRecibo    = TagCaracter(nome='nrRecibo',    tamanho=[1, 40], raiz='//eSocial/evtPgtos/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, obrigatorio=False)
        self.perApur     = TagCaracter(nome='perApur',     tamanho=[1,  7], raiz='//eSocial/evtPgtos/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.tpAmb       = TagInteiro( nome='tpAmb',       tamanho=[1,  1], raiz='//eSocial/evtPgtos/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=2)
        self.procEmi     = TagInteiro( nome='procEmi',     tamanho=[1,  1], raiz='//eSocial/evtPgtos/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False, valor=1)
        self.verProc     = TagCaracter(nome='verProc',     tamanho=[1, 20], raiz='//eSocial/evtPgtos/ideEvento', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideEvento>'
        xml += self.indRetif.xml
        xml += self.nrRecibo.xml
        xml += self.perApur.xml
        xml += self.tpAmb.xml
        xml += self.procEmi.xml
        xml += self.verProc.xml
        xml += '</ideEvento>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.indRetif.xml = arquivo
            self.nrRecibo.xml = arquivo
            self.perApur.xml = arquivo
            self.tpAmb.xml = arquivo
            self.procEmi.xml = arquivo
            self.verProc.xml = arquivo

    xml = property(get_xml, set_xml)


class EvtPgtos(XMLNFe):
    def __init__(self):
        super(EvtPgtos, self).__init__()
        self.Id = TagCaracter(nome='evtPgtos', propriedade='Id', raiz='//eSocial/evtPgtos', namespace=NAMESPACE_ESOCIAL, namespace_obrigatorio=False)
        self.ideEvento = IdeEvento()
        self.ideEmpregador = IdeEmpregador()
        self.ideBenef = IdeBenef()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.Id.xml
        xml += self.ideEvento.xml
        xml += self.ideEmpregador.xml
        xml += self.ideBenef.xml
        xml += '</evtPgtos>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml = arquivo
            self.ideEvento.xml = arquivo
            self.ideEmpregador.xml = arquivo
            self.ideBenef.xml = arquivo

    xml = property(get_xml, set_xml)


class S1210(XMLNFe):
    def __init__(self):
        super(S1210, self).__init__()
        self.evtPgtos = EvtPgtos()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'evtPgtos.xsd'
        self.id_evento = ''
        self.tpInsc = ''
        self.nrInsc = ''
        # self.Signature = Signature()
        self.evento = self.evtPgtos
        self.xml_assinado = ''

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        #xml += ABERTURA
        xml += '<eSocial xmlns="' + NAMESPACE_ESOCIAL + '">'
        xml += self.evtPgtos.xml

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
            self.evtPgtos.xml = arquivo
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
        self.evtPgtos.Id.valor = id_evento
        self.id_evento = id_evento

    xml = property(get_xml, set_xml)
