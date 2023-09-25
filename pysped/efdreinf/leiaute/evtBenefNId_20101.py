# -*- encoding: utf-8 -*-
from __future__ import (division, print_function, unicode_literals,
                        absolute_import)

from builtins import str
import os
from pysped.xml_sped import *
from pysped.efdreinf.leiaute import ESQUEMA_ATUAL_VERSAO_2 as ESQUEMA_ATUAL

DIRNAME = os.path.dirname(__file__)

NAMESPACE_EFDREINF = 'http://www.reinf.esocial.gov.br/schemas/evt4040PagtoBenefNaoIdentificado/v2_01_01'


class InfoProcRet(XMLNFe):
    def __init__(self):
        super(InfoProcRet, self).__init__()
        self.tpProcRet = TagInteiro(nome='tpProcRet', tamanho=[1, 1], raiz='//Reinf/evtBenefNId/ideEstab/ideNat/infoPgto/infoProcRet',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.nrProcRet = TagCaracter(nome='nrProcRet', tamanho=[1, 21], raiz='//Reinf/evtBenefNId/ideEstab/ideNat/infoPgto/infoProcRet',
                                  namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.codSusp = TagInteiro(nome='codSusp', tamanho=[1, 14], raiz='//Reinf/evtBenefNId/ideEstab/ideNat/infoPgto/infoProcRet',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.vlrBaseSuspIR = TagInteiro(nome='vlrBaseSuspIR', tamanho=[1, 14], raiz='//Reinf/evtBenefNId/ideEstab/ideNat/infoPgto/infoProcRet',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.vlrNIR = TagInteiro(nome='vlrNIR', tamanho=[1, 14], raiz='//Reinf/evtBenefNId/ideEstab/ideNat/infoPgto/infoProcRet',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.vlrDepIR = TagInteiro(nome='vlrDepIR', tamanho=[1, 14], raiz='//Reinf/evtBenefNId/ideEstab/ideNat/infoPgto/infoProcRet',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoProcRet>'
        xml += self.tpProcRet.xml
        xml += self.nrProcRet.xml
        xml += self.codSusp.xml
        xml += self.vlrBaseSuspIR.xml
        xml += self.vlrNIR.xml
        xml += self.vlrDepIR.xml
        xml += '</infoProcRet>'

        return xml

    xml = property(get_xml)


class InfoPgto(XMLNFe):
    def __init__(self):
        super(InfoPgto, self).__init__()
        self.dtFg = TagData(nome='dtFg', raiz='//Reinf/evtBenefNId/ideEstab/ideNat/infoPgto',
                            namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.vlrLiq = TagInteiro(nome='vlrLiq', tamanho=[1, 14], raiz='//Reinf/evtBenefNId/ideEstab/ideNat/infoPgto',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.vlrBaseIR = TagInteiro(nome='vlrLiq', tamanho=[1, 14], raiz='//Reinf/evtBenefNId/ideEstab/ideNat/infoPgto',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.vlrIR = TagInteiro(nome='vlrLiq', tamanho=[1, 14], raiz='//Reinf/evtBenefNId/ideEstab/ideNat/infoPgto',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.descr = TagCaracter(nome='descr', tamanho=[1, 200], raiz='//Reinf/evtBenefNId/ideEstab/ideNat/infoPgto',
                                  namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.infoProcRet = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoPgto>'
        xml += self.dtFg.xml
        xml += self.vlrLiq.xml
        xml += self.vlrBaseIR.xml
        xml += self.vlrIR.xml
        xml += self.descr.xml
        for info_proc_ret in self.infoProcRet:
            xml += info_proc_ret.xml
        xml += '</infoPgto>'

        return xml

    xml = property(get_xml)


class IdeNat(XMLNFe):
    def __init__(self):
        super(IdeNat, self).__init__()
        self.natRend = TagInteiro(nome='natRend', tamanho=[1, 5], raiz='//Reinf/evtBenefNId/ideEstab/ideNat',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.infoPgto = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideNat>'
        xml += self.natRend.xml
        for info_pgto in self.infoPgto:
            xml += info_pgto.xml
        xml += '</ideNat>'

        return xml

    xml = property(get_xml)


class IdeEstab(XMLNFe):
    def __init__(self):
        super(IdeEstab, self).__init__()
        self.tpInscEstab = TagInteiro(nome='tpInscEstab', tamanho=[1, 1, 1], raiz='//Reinf/evtBenefNId/ideEstab',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, valor=1)
        self.nrInscEstab = TagCaracter(nome='nrInscEstab', tamanho=[8, 14], raiz='//Reinf/evtBenefNId/ideEstab',
                                  namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.ideNat = IdeNat()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideEstab>'
        xml += self.tpInscEstab.xml
        xml += self.nrInscEstab.xml
        xml += self.ideNat.xml
        xml += '</ideEstab>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.ideEstabObra.xml = arquivo

    xml = property(get_xml, set_xml)


class IdeContri(XMLNFe):
    def __init__(self):
        super(IdeContri, self).__init__()
        self.tpInsc = TagCaracter(nome='tpInsc', valor='1', raiz='//Reinf/evtBenefNId/ideContri',
                                  namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.nrInsc = TagCaracter(nome='nrInsc', tamanho=[8, 14], raiz='//Reinf/evtBenefNId/ideContri',
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
        self.indRetif = TagInteiro(nome='indRetif', tamanho=[1, 1, 1], raiz='//Reinf/evtBenefNId/ideEvento',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, valor=1)
        self.nrRecibo = TagCaracter(nome='nrRecibo', tamanho=[0, 52], raiz='//Reinf/evtBenefNId/ideEvento',
                                    namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.perApur = TagCaracter(nome='perApur', tamanho=[1, 10], raiz='//Reinf/evtBenefNId/ideEvento',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.tpAmb = TagInteiro(nome='tpAmb', tamanho=[1, 1, 1], raiz='//Reinf/evtBenefNId/ideEvento',
                                namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, valor=2)
        self.procEmi = TagInteiro(nome='procEmi', tamanho=[1, 1, 1], raiz='//Reinf/evtBenefNId/ideEvento',
                                  namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.verProc = TagCaracter(nome='verProc', tamanho=[1, 20], raiz='//Reinf/evtBenefNId/ideEvento',
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


class EvtBenefNId(XMLNFe):
    def __init__(self):
        super(EvtBenefNId, self).__init__()
        self.Id = TagCaracter(nome='evtBenefNId', propriedade='id', raiz='//Reinf/evtBenefNId',
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
        xml += '</evtBenefNId>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml = arquivo
            self.ideEvento.xml = arquivo
            self.ideContri.xml = arquivo
            self.ideEstab.xml = arquivo

    xml = property(get_xml, set_xml)


class R4040(XMLNFe):
    def __init__(self):
        super(R4040, self).__init__()
        self.evtBenefNId = EvtBenefNId()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'evtBenefNId-v2_01_01.xsd'
        self.id_evento = ''
        self.Signature = Signature()
        self.evento = self.evtBenefNId

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        # xml += ABERTURA
        xml += '<Reinf xmlns="' + NAMESPACE_EFDREINF + '">'
        xml += self.evtBenefNId.xml

        #
        # Define a URI a ser assinada
        #
        self.Signature.URI = '#' + self.evtBenefNId.Id.valor
        xml += self.Signature.xml
        xml += '</Reinf>'

        # Define o método de assinatura
        self.Signature.metodo = 'sha256'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.evtBenefNId.xml = arquivo
            self.Signature.xml = self._le_noh('//Reinf/evtBenefNId/sig:Signature')

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
        id_evento += self.evtBenefNId.ideContri.tpInsc.valor
        id_evento += str(self.evtBenefNId.ideContri.nrInsc.valor)[0:8] + '000000'
        # id_evento += str(self.evtInfoContri.ideContri.nrInsc.valor).zfill(14)
        id_evento += data_hora
        id_evento += str(sequencia).zfill(5)

        # Define o Id
        #
        self.evtBenefNId.Id.valor = id_evento
        self.id_evento = id_evento

    xml = property(get_xml, set_xml)
