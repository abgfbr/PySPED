# -*- encoding: utf-8 -*-
from __future__ import (division, print_function, unicode_literals,
                        absolute_import)

from builtins import str
import os
from pysped.xml_sped import *
from pysped.efdreinf.leiaute import ESQUEMA_ATUAL_VERSAO_2 as ESQUEMA_ATUAL

DIRNAME = os.path.dirname(__file__)

NAMESPACE_EFDREINF = 'http://www.reinf.esocial.gov.br/schemas/evt4020PagtoBeneficiarioPJ/v2_01_01'


class InfoReembDep(XMLNFe):
    def __init__(self):
        self.tpInsc = TagInteiro(nome='tpInsc', tamanho=[1, 1], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideOpSaude',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.nrInsc = TagCaracter(nome='nrInsc', tamanho=[1, 14], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideOpSaude',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.vlrReemb = TagInteiro(nome='vlrReemb', tamanho=[1, 14], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideOpSaude',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.vlrReembAnt = TagInteiro(nome='vlrReembAnt', tamanho=[1, 14], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideOpSaude',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoReembDep>'
        xml += self.tpInsc.xml
        xml += self.nrInsc.xml
        xml += self.vlrReemb.xml
        xml += self.vlrReembAnt.xml
        xml += '</infoReembDep>'

        return xml

    xml = property(get_xml)


class InfoDependPl(XMLNFe):
    def __init__(self):
        self.cpfDep = TagCaracter(nome='cpfDep', tamanho=[1, 11], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideOpSaude',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.vlrSaude = TagInteiro(nome='vlrSaude', tamanho=[1, 14], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideOpSaude',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoDependPl>'
        xml += self.cpfDep.xml
        xml += self.vlrSaude.xml
        xml += '</infoDependPl>'

        return xml

    xml = property(get_xml)


class InfoReemb(XMLNFe):
    def __init__(self):
        self.tpInsc = TagInteiro(nome='tpInsc', tamanho=[1, 1], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideOpSaude',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.nrInsc = TagCaracter(nome='nrInsc', tamanho=[1, 14], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideOpSaude',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.vlrReemb = TagInteiro(nome='vlrReemb', tamanho=[1, 14], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideOpSaude',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.vlrReembAnt = TagInteiro(nome='vlrReembAnt', tamanho=[1, 14], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideOpSaude',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoReemb>'
        xml += self.tpInsc.xml
        xml += self.nrInsc.xml
        xml += self.vlrReemb.xml
        xml += self.vlrReembAnt.xml
        xml += '</infoReemb>'

        return xml

    xml = property(get_xml)


class IdeOpSaude(XMLNFe):
    def __init__(self):
        self.nrInsc = TagCaracter(nome='nrInsc', tamanho=[1, 14], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.regANS = TagInteiro(nome='regANS', tamanho=[1, 6], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.vlrSaude = TagInteiro(nome='vlrSaude', tamanho=[1, 14], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.infoReemb = []
        self.infoDependPI = []
        self.infoReembDep = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideOpSaude>'
        xml += self.nrInsc.xml
        xml += self.regANS.xml
        xml += self.vlrSaude.xml
        for info_reemb in self.infoReemb:
            xml += info_reemb.xml
        for info_depend_pi in self.infoDependPI:
            xml += info_depend_pi.xml
        for info_reemb_dep in self.infoReembDep:
            xml += info_reemb_dep.xml
        xml += '</ideOpSaude>'

        return xml

    xml = property(get_xml)


class EndExt(XMLNFe):
    def __init__(self):
        self.dscLograd = TagCaracter(nome='dscLograd', tamanho=[1, 80], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto/infoPgtoExt',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.nrLograd = TagCaracter(nome='nrLograd', tamanho=[1, 10], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto/infoPgtoExt',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.complem = TagCaracter(nome='complem', tamanho=[1, 30], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto/infoPgtoExt',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.bairro = TagCaracter(nome='bairro', tamanho=[1, 60], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto/infoPgtoExt',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.cidade = TagCaracter(nome='cidade', tamanho=[1, 40], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto/infoPgtoExt',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.estado = TagCaracter(nome='estado', tamanho=[1, 40], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto/infoPgtoExt',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.codPostal = TagCaracter(nome='codPostal', tamanho=[1, 12], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto/infoPgtoExt',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.telef = TagCaracter(nome='telef', tamanho=[1, 15], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto/infoPgtoExt',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<endExt>'
        xml += self.dscLograd.xml
        xml += self.nrLograd.xml
        xml += self.complem.xml
        xml += self.bairro.xml
        xml += self.cidade.xml
        xml += self.estado.xml
        xml += self.codPostal.xml
        xml += self.telef.xml
        xml += '</endExt>'

        return xml

    xml = property(get_xml)


class InfoPgtoExt(XMLNFe):
    def __init__(self):
        self.indNIF = TagInteiro(nome='indNIF', tamanho=[1, 1], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.nifBenef = TagCaracter(nome='nifBenef', tamanho=[1, 30], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.frmTribut = TagCaracter(nome='frmTribut', tamanho=[1, 2], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.endExt = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoPgtoExt>'
        xml += self.indNIF.xml
        xml += self.nifBenef.xml
        xml += self.frmTribut.xml
        for end_ext in self.endExt:
            xml += end_ext.xml
        xml += '</infoPgtoExt>'

        return xml


class InfoProcJud(XMLNFe):
    def __init__(self):
        self.nrProc = TagCaracter(nome='nrProc', tamanho=[1, 21], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.indOrigRec = TagInteiro(nome='indOrigRec', tamanho=[1, 1], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.cnpjOrigRecurso = TagCaracter(nome='cnpjOrigRecurso', tamanho=[1, 14], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.desc = TagCaracter(nome='desc', tamanho=[1, 50], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.despProcJud = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoProcJud>'
        xml += self.nrProc.xml
        xml += self.indOrigRec.xml
        xml += self.cnpjOrigRecurso.xml
        xml += self.desc.xml
        for desp_proc_jud in self.despProcJud:
            xml += desp_proc_jud.xml
        xml += '</infoProcJud>'

        return xml

    xml = property(get_xml)


class IdeAdv(XMLNFe):
    def __init__(self):
        self.tpInscAdv = TagCaracter(nome='tpInscAdv', tamanho=[1, 1], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto/InfoRRA/despProcJud',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.nrInscAdv = TagInteiro(nome='nrInscAdv', tamanho=[1, 14], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto/InfoRRA/despProcJud',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.vlrAdv = TagCaracter(nome='vlrAdv', tamanho=[1, 14], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto/InfoRRA/despProcJud',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideAdv>'
        xml += self.tpInscAdv.xml
        xml += self.nrInscAdv.xml
        xml += self.vlrAdv.xml
        xml += '</ideAdv>'

        return xml


class DespProcJud(XMLNFe):
    def __init__(self):
        self.vlrDespCustas = TagInteiro(nome='tpProcRRA', tamanho=[1, 14], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto/InfoRRA',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.vlrDespAdvogados = TagInteiro(nome='tpProcRRA', tamanho=[1, 14], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto/InfoRRA',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.ideAdv = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<despProcJud>'
        xml += self.vlrDespCustas.xml
        xml += self.vlrDespAdvogados.xml
        for ide_adv in self.ideAdv:
            xml += ide_adv.xml
        xml += '</despProcJud>'

        return xml

    xml = property(get_xml)


class InfoRRA(XMLNFe):
    def __init__(self):
        self.tpProcRRA = TagInteiro(nome='tpProcRRA', tamanho=[1, 1], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto/InfoRRA',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.nrProcRRA = TagCaracter(nome='nrProcRRA', tamanho=[1, 21], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto/InfoRRA',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.indOrigRec = TagInteiro(nome='indOrigRec', tamanho=[1, 1], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto/InfoRRA',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.descRRA = TagCaracter(nome='descRRA', tamanho=[1, 50], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto/InfoRRA',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.qtdMesesRRA = TagInteiro(nome='qtdMesesRRA', tamanho=[1, 4], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto/InfoRRA',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.cnpjOrigRecurso = TagCaracter(nome='cnpjOrigRecurso', tamanho=[1, 14], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto/InfoRRA',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.despProcJud = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoRRA>'
        xml += self.tpProcRRA.xml
        xml += self.nrProcRRA.xml
        xml += self.indOrigRec.xml
        xml += self.descRRA.xml
        xml += self.qtdMesesRRA.xml
        xml += self.cnpjOrigRecurso.xml
        for desp_proc_jud in self.despProcJud:
            xml += desp_proc_jud.xml
        xml += '</infoRRA>'

        return xml

    xml = property(get_xml)


class BenefPen(XMLNFe):
    def __init__(self):
        self.cpfDep = TagCaracter(nome='cpfDep', tamanho=[0, 11], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto/benefPen',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.vlrDepenSusp = TagInteiro(nome='vlrDepenSusp', tamanho=[1, 14], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto/benefPen',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<benefPen>'
        xml += self.cpfDep.xml
        xml += self.vlrDepenSusp.xml
        xml += '</benefPen>'

        return xml

    xml = property(get_xml)


class InfoProcRet(XMLNFe):
    def __init__(self):
        super(InfoProcRet, self).__init__()
        self.tpProcRet = TagInteiro(nome='tpProcRet', tamanho=[1, 1], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto/infoProcRet',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.nrProcRet = TagCaracter(nome='nrProcRet', tamanho=[0, 21], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto/infoProcRet',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.codSusp = TagInteiro(nome='codSusp', tamanho=[1, 14], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto/infoProcRet',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.vlrBaseSuspIR = TagInteiro(nome='vlrNRetido', tamanho=[1, 14], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto/infoProcRet',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.vlrNIR = TagInteiro(nome='vlrNRetido', tamanho=[1, 14], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto/infoProcRet',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.vlrDepIR = TagInteiro(nome='vlrNRetido', tamanho=[1, 14], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto/infoProcRet',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.vlrBaseSuspCSLL = TagInteiro(nome='vlrNRetido', tamanho=[1, 14], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto/infoProcRet',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.vlrNCSLL = TagInteiro(nome='vlrNRetido', tamanho=[1, 14], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto/infoProcRet',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.vlrDepCSLL = TagInteiro(nome='vlrNRetido', tamanho=[1, 14], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto/infoProcRet',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.vlrBaseSuspCofins = TagInteiro(nome='vlrNRetido', tamanho=[1, 14], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto/infoProcRet',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.vlrNCofins = TagInteiro(nome='vlrNRetido', tamanho=[1, 14], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto/infoProcRet',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.vlrDepCofins = TagInteiro(nome='vlrNRetido', tamanho=[1, 14], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto/infoProcRet',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.vlrBaseSuspPP = TagInteiro(nome='vlrNRetido', tamanho=[1, 14], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto/infoProcRet',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.vlrNPP = TagInteiro(nome='vlrNRetido', tamanho=[1, 14], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto/infoProcRet',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.vlrDepPP = TagInteiro(nome='vlrNRetido', tamanho=[1, 14], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto/infoProcRet',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoProcRet>'
        xml += self.tpProcRet.xml
        xml += self.nrProcRet.xml
        xml += self.codSusp.xml
        xml += self.vlrNRetido.xml
        xml += self.vlrDepJud.xml
        xml += self.vlrCmpAnoCal.xml
        xml += self.vlrCmpAnoAnt.xml
        xml += self.vlrRendSusp.xml
        xml += '</infoProcRet>'

        return xml

    xml = property(get_xml)


class Retencoes(XMLNFe):
    def __init__(self):
        self.vlrBaseIR = TagDecimalVirgula(nome='vlrBaseIR', tamanho=[1, 14, 2], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto/retencoes',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.vlrIR = TagDecimalVirgula(nome='vlrIR', tamanho=[1, 14, 2], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto/retencoes',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.vlrBaseAgreg = TagDecimalVirgula(nome='vlrBaseAgreg', tamanho=[1, 14, 2], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto/retencoes',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.vlrAgreg = TagDecimalVirgula(nome='vlrAgreg', tamanho=[1, 14, 2], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto/retencoes',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.vlrBaseCSLL = TagDecimalVirgula(nome='vlrBaseCSLL', tamanho=[1, 14, 2], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto/retencoes',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.vlrCSLL = TagDecimalVirgula(nome='vlrCSLL', tamanho=[1, 14, 2], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto/retencoes',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.vlrBaseCofins = TagDecimalVirgula(nome='vlrBaseCofins', tamanho=[1, 14, 2], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto/retencoes',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.vlrCofins = TagDecimalVirgula(nome='vlrCofins', tamanho=[1, 14, 2], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto/retencoes',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.vlrBasePP = TagDecimalVirgula(nome='vlrBasePP', tamanho=[1, 14, 2], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto/retencoes',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.vlrPP = TagDecimalVirgula(nome='vlrPP', tamanho=[1, 14, 2], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto/retencoes',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<retencoes>'
        xml += self.vlrBaseIR.xml
        xml += self.vlrIR.xml
        xml += self.vlrBaseAgreg.xml
        xml += self.vlrAgreg.xml
        xml += self.vlrBaseCofins.xml
        xml += self.vlrCofins.xml
        xml += self.vlrBasePP.xml
        xml += self.vlrPP.xml
        xml += '</retencoes>'

        return xml

    xml = property(get_xml)


class InfoPgto(XMLNFe):
    def __init__(self):
        super(InfoPgto, self).__init__()
        self.dtFG = TagData(nome='dtFG', raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto',
                            namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.vlrBruto = TagDecimalVirgula(nome='vlrBruto', tamanho=[1, 14, 2], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.indFciScp = TagInteiro(nome='indFciScp', tamanho=[1, 1], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.nrInscFciScp = TagCaracter(nome='nrInscFciScp', tamanho=[0, 14], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.percSCP = TagInteiro(nome='percSCP', tamanho=[1, 4], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.indJud = TagCaracter(nome='indJud', tamanho=[0, 1], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.paisResidExt = TagCaracter(nome='paisResidExt', tamanho=[0, 3], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.retencoes = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoPgto>'
        xml += self.dtFG.xml
        xml += self.vlrBruto.xml
        xml += self.indFciScp.xml
        xml += self.nrInscFciScp.xml
        xml += self.percSCP.xml
        xml += self.indJud.xml
        xml += self.paisResidExt.xml
        for retencao in self.retencoes:
            xml += retencao.xml
        xml += '</infoPgto>'

        return xml

    def set_xml(self, arquivo):
        if self._le_arquivo(arquivo):
            self.dtFG.xml = arquivo
            self.vlrBruto.xml = arquivo
            self.indFciScp.xml = arquivo
            self.nrInscFciScp.xml = arquivo
            self.percSCP.xml = arquivo
            self.indJud.xml = arquivo
            self.paisResidExt.xml = arquivo
            self.retencoes = self.le_grupo('//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto/retencoes', Retencoes,
                                          namespace=NAMESPACE_EFDREINF)

    xml = property(get_xml, set_xml)


class IdePgto(XMLNFe):
    def __init__(self):
        super(IdePgto, self).__init__()
        self.natRend = TagInteiro(nome='natRend', tamanho=[1, 5], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.observ = TagCaracter(nome='observ', tamanho=[0, 200], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.infoPgto = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<idePgto>'
        xml += self.natRend.xml
        xml += self.observ.xml
        for info_pgto in self.infoPgto:
            xml += info_pgto.xml
        xml += '</idePgto>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.natRend.xml = arquivo
            self.observ.xml = arquivo
            self.infoPgto = self.le_grupo('//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto/infoPgto', InfoPgto,
                                         namespace=NAMESPACE_EFDREINF)

    xml = property(get_xml, set_xml)


class IdeBenef(XMLNFe):
    def __init__(self):
        super(IdeBenef, self).__init__()
        self.cnpjBenef = TagCaracter(nome='cnpjBenef', tamanho=[0, 14], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.nmBenef = TagCaracter(nome='nmBenef', tamanho=[0, 70], raiz='//Reinf/evtRetPJ/ideEstab/ideBenef',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.isenImun = TagInteiro(nome='isenImun', tamanho=[1, 1], raiz='//Reinf/evtRetPJ/ideEstab/ideBene',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.socCivil = TagInteiro(nome='socCivil', tamanho=[1, 1], raiz='//Reinf/evtRetPJ/ideEstab/ideBene',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.ideDep = []
        self.idePgto = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideBenef>'
        xml += self.cnpjBenef.xml
        xml += self.nmBenef.xml
        xml += self.isenImun.xml
        for ide_pgto in self.idePgto:
            xml += ide_pgto.xml
        xml += '</ideBenef>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cnpjBenef.xml = arquivo
            self.nmBenef.xml = arquivo
            self.isenImun.xml = arquivo
            self.idePgto = self.le_grupo(
                '//Reinf/evtRetPJ/ideEstab/ideBenef/ideDep/idePgto', IdePgto,
                namespace=NAMESPACE_EFDREINF)

    xml = property(get_xml, set_xml)


class IdeEstab(XMLNFe):
    def __init__(self):
        super(IdeEstab, self).__init__()
        self.tpInscEstab = TagInteiro(nome='tpInscEstab', tamanho=[1, 1, 1], raiz='//Reinf/evtRetPJ/ideEstab',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, valor=1)
        self.nrInscEstab = TagCaracter(nome='nrInscEstab', tamanho=[8, 14], raiz='//Reinf/evtRetPJ/ideEstab',
                                  namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.ideBenef = IdeBenef()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideEstab>'
        xml += self.tpInscEstab.xml
        xml += self.nrInscEstab.xml
        xml += self.ideBenef.xml
        xml += '</ideEstab>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.ideEstabObra.xml = arquivo

    xml = property(get_xml, set_xml)


class IdeContri(XMLNFe):
    def __init__(self):
        super(IdeContri, self).__init__()
        self.tpInsc = TagCaracter(nome='tpInsc', valor='1', raiz='//Reinf/evtRetPJ/ideContri',
                                  namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.nrInsc = TagCaracter(nome='nrInsc', tamanho=[8, 14], raiz='//Reinf/evtRetPJ/ideContri',
                                  namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)

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

    xml = property(get_xml, set_xml)


class IdeEvento(XMLNFe):
    def __init__(self):
        super(IdeEvento, self).__init__()
        self.indRetif = TagInteiro(nome='indRetif', tamanho=[1, 1, 1], raiz='//Reinf/evtRetPJ/ideEvento',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, valor=1)
        self.nrRecibo = TagCaracter(nome='nrRecibo', tamanho=[0, 52], raiz='//Reinf/evtRetPJ/ideEvento',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.perApur = TagCaracter(nome='perApur', tamanho=[1, 10], raiz='//Reinf/evtRetPJ/ideEvento',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.tpAmb = TagInteiro(nome='tpAmb', tamanho=[1, 1, 1], raiz='//Reinf/evtRetPJ/ideEvento',
                                namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, valor=2)
        self.procEmi = TagInteiro(nome='procEmi', tamanho=[1, 1, 1], raiz='//Reinf/evtRetPJ/ideEvento',
                                  namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.verProc = TagCaracter(nome='verProc', tamanho=[1, 20], raiz='//Reinf/evtRetPJ/ideEvento',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideEvento>'
        xml += self.indRetif.xml
        if self.nrRecibo.valor:
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


class EvtRetPJ(XMLNFe):
    def __init__(self):
        super(EvtRetPJ, self).__init__()
        self.Id = TagCaracter(nome='evtRetPJ', propriedade='id', raiz='//Reinf/evtRetPJ',
                              namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.ideEvento = IdeEvento()
        self.ideContri = IdeContri()
        self.ideEstab = IdeEstab()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.Id.xml
        xml += self.ideEvento.xml
        xml += self.ideContri.xml
        xml += self.ideEstab.xml
        xml += '</evtRetPJ>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml = arquivo
            self.ideEvento.xml = arquivo
            self.ideContri.xml = arquivo
            self.ideEstab.xml = arquivo

    xml = property(get_xml, set_xml)


class R4020(XMLNFe):
    def __init__(self):
        super(R4020, self).__init__()
        self.evtRetPJ = EvtRetPJ()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'evtRetPJ-v2_01_01.xsd'
        self.id_evento = ''
        self.Signature = Signature()
        self.evento = self.evtRetPJ

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        # xml += ABERTURA
        xml += '<Reinf xmlns="' + NAMESPACE_EFDREINF + '">'
        xml += self.evtRetPJ.xml

        #
        # Define a URI a ser assinada
        #
        self.Signature.URI = '#' + self.evtRetPJ.Id.valor
        xml += self.Signature.xml
        xml += '</Reinf>'

        # Define o método de assinatura
        self.Signature.metodo = 'sha256'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.evtRetPJ.xml = arquivo
            self.Signature.xml = self._le_noh('//Reinf/evtRetPJ/sig:Signature')

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
        id_evento += self.evtRetPJ.ideContri.tpInsc.valor
        id_evento += str(self.evtRetPJ.ideContri.nrInsc.valor)[0:8] + '000000'
        # id_evento += str(self.evtInfoContri.ideContri.nrInsc.valor).zfill(14)
        id_evento += data_hora
        id_evento += str(sequencia).zfill(5)

        # Define o Id
        #
        self.evtRetPJ.Id.valor = id_evento
        self.id_evento = id_evento

    xml = property(get_xml, set_xml)
