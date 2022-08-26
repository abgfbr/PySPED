from __future__ import (division, print_function, unicode_literals,
                        absolute_import)

from builtins import str
import os
from pysped.xml_sped import *
from pysped.efdreinf.leiaute import ESQUEMA_ATUAL_VERSAO_2 as ESQUEMA_ATUAL

DIRNAME = os.path.dirname(__file__)

NAMESPACE_EFDREINF = 'http://www.reinf.esocial.gov.br/schemas/evt4010PagtoBeneficiarioPF/v2_01_01'


class InfoReembDep(XMLNFe):
    def __init__(self):
        self.tpInsc = TagInteiro(nome='tpInsc', tamanho=[1, 1], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideOpSaude',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.nrInsc = TagCaracter(nome='nrInsc', tamanho=[1, 14], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideOpSaude',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.vlrReemb = TagInteiro(nome='vlrReemb', tamanho=[1, 14], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideOpSaude',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.vlrReembAnt = TagInteiro(nome='vlrReembAnt', tamanho=[1, 14], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideOpSaude',
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
        self.cpfDep = TagCaracter(nome='cpfDep', tamanho=[1, 11], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideOpSaude',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.vlrSaude = TagInteiro(nome='vlrSaude', tamanho=[1, 14], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideOpSaude',
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
        self.tpInsc = TagInteiro(nome='tpInsc', tamanho=[1, 1], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideOpSaude',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.nrInsc = TagCaracter(nome='nrInsc', tamanho=[1, 14], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideOpSaude',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.vlrReemb = TagInteiro(nome='vlrReemb', tamanho=[1, 14], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideOpSaude',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.vlrReembAnt = TagInteiro(nome='vlrReembAnt', tamanho=[1, 14], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideOpSaude',
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
        self.nrInsc = TagCaracter(nome='nrInsc', tamanho=[1, 14], raiz='//Reinf/evtRetPF/ideEstab/ideBenef',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.regANS = TagInteiro(nome='regANS', tamanho=[1, 6], raiz='//Reinf/evtRetPF/ideEstab/ideBenef',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.vlrSaude = TagInteiro(nome='vlrSaude', tamanho=[1, 14], raiz='//Reinf/evtRetPF/ideEstab/ideBenef',
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
        self.dscLograd = TagCaracter(nome='dscLograd', tamanho=[1, 80], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto/infoPgtoExt',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.nrLograd = TagCaracter(nome='nrLograd', tamanho=[1, 10], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto/infoPgtoExt',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.complem = TagCaracter(nome='complem', tamanho=[1, 30], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto/infoPgtoExt',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.bairro = TagCaracter(nome='bairro', tamanho=[1, 60], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto/infoPgtoExt',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.cidade = TagCaracter(nome='cidade', tamanho=[1, 40], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto/infoPgtoExt',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.estado = TagCaracter(nome='estado', tamanho=[1, 40], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto/infoPgtoExt',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.codPostal = TagCaracter(nome='codPostal', tamanho=[1, 12], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto/infoPgtoExt',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.telef = TagCaracter(nome='telef', tamanho=[1, 15], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto/infoPgtoExt',
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
        self.indNIF = TagInteiro(nome='indNIF', tamanho=[1, 1], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.nifBenef = TagCaracter(nome='nifBenef', tamanho=[1, 30], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.frmTribut = TagCaracter(nome='frmTribut', tamanho=[1, 2], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto',
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
        self.nrProc = TagCaracter(nome='nrProc', tamanho=[1, 21], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.indOrigRec = TagInteiro(nome='indOrigRec', tamanho=[1, 1], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.cnpjOrigRecurso = TagCaracter(nome='cnpjOrigRecurso', tamanho=[1, 14], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.desc = TagCaracter(nome='desc', tamanho=[1, 50], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto',
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
        self.tpInscAdv = TagCaracter(nome='tpInscAdv', tamanho=[1, 1], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto/InfoRRA/despProcJud',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.nrInscAdv = TagInteiro(nome='nrInscAdv', tamanho=[1, 14], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto/InfoRRA/despProcJud',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.vlrAdv = TagCaracter(nome='vlrAdv', tamanho=[1, 14], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto/InfoRRA/despProcJud',
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
        self.vlrDespCustas = TagInteiro(nome='tpProcRRA', tamanho=[1, 14], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto/InfoRRA',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.vlrDespAdvogados = TagInteiro(nome='tpProcRRA', tamanho=[1, 14], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto/InfoRRA',
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
        self.tpProcRRA = TagInteiro(nome='tpProcRRA', tamanho=[1, 1], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto/InfoRRA',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.nrProcRRA = TagCaracter(nome='nrProcRRA', tamanho=[1, 21], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto/InfoRRA',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.indOrigRec = TagInteiro(nome='indOrigRec', tamanho=[1, 1], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto/InfoRRA',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.descRRA = TagCaracter(nome='descRRA', tamanho=[1, 50], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto/InfoRRA',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.qtdMesesRRA = TagInteiro(nome='qtdMesesRRA', tamanho=[1, 4], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto/InfoRRA',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.cnpjOrigRecurso = TagCaracter(nome='cnpjOrigRecurso', tamanho=[1, 14], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto/InfoRRA',
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
        self.cpfDep = TagCaracter(nome='cpfDep', tamanho=[0, 11], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto/benefPen',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.vlrDepenSusp = TagInteiro(nome='vlrDepenSusp', tamanho=[1, 14], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto/benefPen',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<benefPen>'
        xml += self.cpfDep.xml
        xml += self.vlrDepenSusp.xml
        xml += '</benefPen>'

        return xml

    xml = property(get_xml)


class DedSusp(XMLNFe):
    def __init__(self):
        self.indTpDeducao = TagInteiro(nome='indTpDeducao', tamanho=[1, 2], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto/dedSusp',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.vlrDedSusp = TagInteiro(nome='vlrDedSusp', tamanho=[1, 14], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto/dedSusp',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.benefPen = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<dedSusp>'
        xml += self.indTpDeducao.xml
        xml += self.vlrDedSusp.xml
        for benef_pen in self.benefPen:
            xml += benef_pen.xml
        xml += '</dedSusp>'

        return xml

    xml = property(get_xml)


class InfoProcRet(XMLNFe):
    def __init__(self):
        super(InfoProcRet, self).__init__()
        self.tpProcRet = TagInteiro(nome='tpProcRet', tamanho=[1, 1], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto/infoProcRet',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.nrProcRet = TagCaracter(nome='nrProcRet', tamanho=[0, 21], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto/infoProcRet',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.codSusp = TagInteiro(nome='codSusp', tamanho=[1, 14], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto/infoProcRet',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.vlrNRetido = TagInteiro(nome='vlrNRetido', tamanho=[1, 14], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto/infoProcRet',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.vlrDepJud = TagInteiro(nome='vlrDepJud', tamanho=[1, 14], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto/infoProcRet',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.vlrCmpAnoCal = TagInteiro(nome='vlrCmpAnoCal', tamanho=[1, 14], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto/infoProcRet',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.vlrCmpAnoAnt = TagInteiro(nome='vlrCmpAnoAnt', tamanho=[1, 14], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto/infoProcRet',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.vlrRendSusp = TagInteiro(nome='vlrRendSusp', tamanho=[1, 14], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto/infoProcRet',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)

        self.dedSusp = []

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
        for ded_susp in self.dedSusp:
            xml += ded_susp.xml
        xml += '</infoProcRet>'

        return xml

    xml = property(get_xml)


class RendIsento(XMLNFe):
    def __init__(self):
        super(RendIsento, self).__init__()
        self.tpIsencao = TagInteiro(nome='tpIsencao', tamanho=[1, 14], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto/rendIsento',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.vlrIsento = TagInteiro(nome='vlrIsento', tamanho=[1, 14], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto/rendIsento',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.descRendimento = TagCaracter(nome='descRendimento', tamanho=[0, 11], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto/rendIsento',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.dtLaudo = TagData(nome='dtLaudo', raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto/rendIsento',
                            namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<rendIsento>'
        xml += self.tpIsencao.xml
        xml += self.vlrIsento.xml
        xml += self.descRendimento.xml
        xml += self.dtLaudo.xml
        xml += '</rendIsento>'

        return xml

    def set_xml(self, arquivo):
        if self._le_arquivo(arquivo):
            self.tpIsencao.xml = arquivo
            self.vlrIsento.xml = arquivo
            self.descRendimento.xml = arquivo
            self.dtLaudo.xml = arquivo

    xml = property(get_xml, set_xml)


class BenefPen(XMLNFe):
    def __init__(self):
        super(BenefPen, self).__init__()
        self.cpfDep = TagCaracter(nome='cpfDep', tamanho=[0, 11], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto/detDed/benefPen',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.vlrDepen = TagInteiro(nome='vlrDepen', tamanho=[1, 14], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto/detDed/benefPen',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<benefPen>'
        xml += self.cpfDep.xml
        xml += self.vlrDepen.xml
        xml += '</benefPen>'

        return xml

    def set_xml(self, arquivo):
        if self._le_arquivo(arquivo):
            self.cpfDep.xml = arquivo
            self.vlrDepen.xml = arquivo

    xml = property(get_xml, set_xml)


class DetDed(XMLNFe):
    def __init__(self):
        super(DetDed, self).__init__()
        self.indTpDeducao = TagInteiro(nome='indTpDeducao', tamanho=[1, 2], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto/detDed',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.vlrDeducao = TagInteiro(nome='vlrDeducao', tamanho=[1, 14], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto/detDed',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.infoEntid = TagCaracter(nome='infoEntid', tamanho=[0, 1], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto/detDed',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.nrInscPrevComp = TagCaracter(nome='nrInscPrevComp', tamanho=[0, 14], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto/detDed',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.vlrPtrocFunp = TagInteiro(nome='vlrPtrocFunp', tamanho=[1, 14], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto/detDed',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.benefPen = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<detDed>'
        xml += self.indTpDeducao.xml
        xml += self.vlrDeducao.xml
        xml += self.infoEntid.xml
        xml += self.nrInscPrevComp.xml
        xml += self.vlrPtrocFunp.xml
        for benef_pen in self.benefPen:
            xml += benef_pen.xml
        xml += '</detDed>'

        return xml

    def set_xml(self, arquivo):
        if self._le_arquivo(arquivo):
            self.indTpDeducao.xml = arquivo
            self.vlrDeducao.xml = arquivo
            self.infoEntid.xml = arquivo
            self.nrInscPrevComp.xml = arquivo
            self.vlrPtrocFunp.xml = arquivo
            self.benefPen = self.le_grupo('//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto/detDed/benefPen',
                                          BenefPen, namespace=NAMESPACE_EFDREINF)

    xml = property(get_xml, set_xml)


class InfoPgto(XMLNFe):
    def __init__(self):
        super(InfoPgto, self).__init__()
        self.dtFG = TagData(nome='dtFG', raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto',
                            namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.compFP = TagCaracter(nome='compFP', tamanho=[0, 7], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.indDecTerc = TagCaracter(nome='indDecTerc', tamanho=[0, 1], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.vlrRendBruto = TagInteiro(nome='vlrRendBruto', tamanho=[1, 14], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.vlrRendTrib = TagInteiro(nome='vlrRendTrib', tamanho=[1, 14], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.vlrIR = TagInteiro(nome='vlrRendBruto', tamanho=[1, 14], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.indRRA = TagCaracter(nome='indRRA', tamanho=[0, 1], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.indFciScp = TagInteiro(nome='indFciScp', tamanho=[1, 1], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.nrInscFciScp = TagCaracter(nome='nrInscFciScp', tamanho=[0, 14], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.percSCP = TagInteiro(nome='percSCP', tamanho=[1, 4], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.indJud = TagCaracter(nome='indJud', tamanho=[0, 1], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.paisResidExt = TagCaracter(nome='paisResidExt', tamanho=[0, 3], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.detDed = []
        self.rendIsento = []
        self.infoProcRet = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoPgto>'
        xml += self.dtFG.xml
        xml += self.indDecTerc.xml
        xml += self.vlrRendBruto.xml
        xml += self.vlrRendTrib.xml
        xml += self.vlrIR.xml
        xml += self.indRRA.xml
        xml += self.indFciScp.xml
        xml += self.nrInscFciScp.xml
        xml += self.percSCP.xml
        xml += self.indJud.xml
        xml += self.paisResidExt.xml
        for det_ded in self.detDed:
            xml += det_ded.xml
        for rend_isento in self.rendIsento:
            xml += rend_isento.xml
        for info_proc_ret in self.infoProcRet:
            xml += info_proc_ret.xml
        xml += '</infoPgto>'

        return xml

    def set_xml(self, arquivo):
        if self._le_arquivo(arquivo):
            self.dtFG.xml = arquivo
            self.indDecTerc.xml = arquivo
            self.vlrRendBruto.xml = arquivo
            self.vlrRendTrib.xml = arquivo
            self.vlrIR.xml = arquivo
            self.indRRA.xml = arquivo
            self.indFciScp.xml = arquivo
            self.nrInscFciScp.xml = arquivo
            self.percSCP.xml = arquivo
            self.indJud.xml = arquivo
            self.paisResidExt.xml = arquivo
            self.detDed = self.le_grupo('//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto/detDed', DetDed,
                                          namespace=NAMESPACE_EFDREINF)
            self.rendIsento = self.le_grupo('//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto/rendIsento', RendIsento,
                                          namespace=NAMESPACE_EFDREINF)
            self.infoProcRet = self.le_grupo('//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto/infoProcRet', InfoProcRet,
                                          namespace=NAMESPACE_EFDREINF)

    xml = property(get_xml, set_xml)


class IdePgto(XMLNFe):
    def __init__(self):
        super(IdePgto, self).__init__()
        self.natRend = TagInteiro(nome='natRend', tamanho=[1, 5], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.observ = TagCaracter(nome='observ', tamanho=[0, 200], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto',
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
            self.infoPgto = self.le_grupo('//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto/infoPgto', InfoPgto,
                                         namespace=NAMESPACE_EFDREINF)

    xml = property(get_xml, set_xml)


class IdeDep(XMLNFe):
    def __init__(self):
        super(IdeDep, self).__init__()
        self.cpfDep = TagCaracter(nome='cpfBenef', tamanho=[0, 11], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.relDep = TagInteiro(nome='relDep', tamanho=[1, 2], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.descrDep = TagCaracter(nome='descrDep', tamanho=[0, 30], raiz='//Reinf/evtRetPF/ideEstab/ideBenef/ideDep',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideDep>'
        xml += self.cpfDep.xml
        xml += self.relDep.xml
        xml += self.descrDep.xml
        xml += '</ideDep>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cpfDep.xml = arquivo
            self.relDep.xml = arquivo
            self.descrDep.xml = arquivo

    xml = property(get_xml, set_xml)


class IdeBenef(XMLNFe):
    def __init__(self):
        super(IdeBenef, self).__init__()
        self.cpfBenef = TagCaracter(nome='cpfBenef', tamanho=[0, 11], raiz='//Reinf/evtRetPF/ideEstab/ideBenef',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.nmBenef = TagCaracter(nome='nmBenef', tamanho=[0, 70], raiz='//Reinf/evtRetPF/ideEstab/ideBenef',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.ideDep = []
        self.idePgto = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideBenef>'
        xml += self.cpfBenef.xml
        xml += self.nmBenef.xml
        for ide_dep in self.ideDep:
            xml += ide_dep.xml
        for ide_pgto in self.idePgto:
            xml += ide_pgto.xml
        xml += '</ideBenef>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cpfBenef.xml = arquivo
            self.nmBenef.xml = arquivo
            self.ideDep = self.le_grupo('//Reinf/evtRetPF/ideEstab/ideBenef/ideDep', IdeDep,
                                        namespace=NAMESPACE_EFDREINF)
            self.idePgto = self.le_grupo(
                '//Reinf/evtRetPF/ideEstab/ideBenef/ideDep/idePgto', IdePgto,
                namespace=NAMESPACE_EFDREINF)

    xml = property(get_xml, set_xml)


class IdeEstab(XMLNFe):
    def __init__(self):
        super(IdeEstab, self).__init__()
        self.tpInscEstab = TagInteiro(nome='tpInscEstab', tamanho=[1, 1, 1], raiz='//Reinf/evtRetPF/ideEstab',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, valor=1)
        self.nrInscEstab = TagCaracter(nome='nrInscEstab', tamanho=[8, 14], raiz='//Reinf/evtRetPF/ideEstab',
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
        self.tpInsc = TagCaracter(nome='tpInsc', valor='1', raiz='//Reinf/evtRetPF/ideContri',
                                  namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.nrInsc = TagCaracter(nome='nrInsc', tamanho=[8, 14], raiz='//Reinf/evtRetPF/ideContri',
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
        self.indRetif = TagInteiro(nome='indRetif', tamanho=[1, 1, 1], raiz='//Reinf/evtRetPF/ideEvento',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, valor=1)
        self.nrRecibo = TagCaracter(nome='nrRecibo', tamanho=[0, 52], raiz='//Reinf/evtRetPF/ideEvento',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.perApur = TagCaracter(nome='perApur', tamanho=[1, 10], raiz='//Reinf/evtRetPF/ideEvento',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.tpAmb = TagInteiro(nome='tpAmb', tamanho=[1, 1, 1], raiz='//Reinf/evtRetPF/ideEvento',
                                namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, valor=2)
        self.procEmi = TagInteiro(nome='procEmi', tamanho=[1, 1, 1], raiz='//Reinf/evtRetPF/ideEvento',
                                  namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.verProc = TagCaracter(nome='verProc', tamanho=[1, 20], raiz='//Reinf/evtRetPF/ideEvento',
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


class EvtRetPF(XMLNFe):
    def __init__(self):
        super(EvtRetPF, self).__init__()
        self.Id = TagCaracter(nome='evtRetPF', propriedade='id', raiz='//Reinf/evtRetPF',
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
        xml += '</evtRetPF>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml = arquivo
            self.ideEvento.xml = arquivo
            self.ideContri.xml = arquivo
            self.ideEstab.xml = arquivo

    xml = property(get_xml, set_xml)


class R4010(XMLNFe):
    def __init__(self):
        super(R4010, self).__init__()
        self.evtRetPF = EvtRetPF()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'evtRetPF-v2_01_01.xsd'
        self.id_evento = ''
        self.Signature = Signature()
        self.evento = self.evtRetPF

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        # xml += ABERTURA
        xml += '<Reinf xmlns="' + NAMESPACE_EFDREINF + '">'
        xml += self.evtRetPF.xml

        #
        # Define a URI a ser assinada
        #
        self.Signature.URI = '#' + self.evtRetPF.Id.valor
        xml += self.Signature.xml
        xml += '</Reinf>'

        # Define o método de assinatura
        self.Signature.metodo = 'sha256'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.evtRetPF.xml = arquivo
            self.Signature.xml = self._le_noh('//Reinf/evtRetPF/sig:Signature')

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
        id_evento += self.evtRetPF.ideContri.tpInsc.valor
        id_evento += str(self.evtRetPF.ideContri.nrInsc.valor)[0:8] + '000000'
        # id_evento += str(self.evtInfoContri.ideContri.nrInsc.valor).zfill(14)
        id_evento += data_hora
        id_evento += str(sequencia).zfill(5)

        # Define o Id
        #
        self.evtRetPF.Id.valor = id_evento
        self.id_evento = id_evento

    xml = property(get_xml, set_xml)
