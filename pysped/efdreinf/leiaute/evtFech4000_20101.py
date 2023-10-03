# -*- encoding: utf-8 -*-
from __future__ import (division, print_function, unicode_literals,
                        absolute_import)

from builtins import str
import os
from pysped.xml_sped import *
from pysped.efdreinf.leiaute import ESQUEMA_ATUAL_VERSAO_2 as ESQUEMA_ATUAL

DIRNAME = os.path.dirname(__file__)

NAMESPACE_EFDREINF = 'http://www.reinf.esocial.gov.br/schemas/evt4099FechamentoDirf/v2_01_02'


class InfoFech(XMLNFe):
    def __init__(self):
        super(InfoFech, self).__init__()
        self.fechRet = TagInteiro(nome='fechRet', tamanho=[1, 1, 1], raiz='//Reinf/evtFech/infoFech',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<infoFech>'
        xml += self.fechRet.xml
        xml += '</infoFech>'

        return xml

    xml = property(get_xml)


class IdeRespInf(XMLNFe):
    def __init__(self):
        super(IdeRespInf, self).__init__()
        self.nmResp = TagCaracter(nome='nmResp', tamanho=[1, 70], raiz='//Reinf/evtFech/ideRespInf',
                                  namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.cpfResp = TagCaracter(nome='cpfResp', tamanho=[1, 11], raiz='//Reinf/evtFech/ideRespInf',
                                  namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.telefone = TagCaracter(nome='telefone', tamanho=[1, 13], raiz='//Reinf/evtFech/ideRespInf',
                                  namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)
        self.email = TagCaracter(nome='email', tamanho=[1, 60], raiz='//Reinf/evtFech/ideRespInf',
                                  namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ideRespInf>'
        xml += self.nmResp.xml
        xml += self.cpfResp.xml
        xml += self.telefone.xml
        xml += self.email.xml
        xml += '</ideRespInf>'

        return xml

    xml = property(get_xml)


class IdeContri(XMLNFe):
    def __init__(self):
        super(IdeContri, self).__init__()
        self.tpInsc = TagCaracter(nome='tpInsc', valor='1', raiz='//Reinf/evtFech/ideContri',
                                  namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.nrInsc = TagCaracter(nome='nrInsc', tamanho=[8, 14], raiz='//Reinf/evtFech/ideContri',
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
        self.perApur = TagCaracter(nome='perApur', tamanho=[1, 10], raiz='//Reinf/evtFech/ideEvento',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.tpAmb = TagInteiro(nome='tpAmb', tamanho=[1, 1, 1], raiz='//Reinf/evtFech/ideEvento',
                                namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False, valor=2)
        self.procEmi = TagInteiro(nome='procEmi', tamanho=[1, 1, 1], raiz='//Reinf/evtFech/ideEvento',
                                  namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.verProc = TagCaracter(nome='verProc', tamanho=[1, 20], raiz='//Reinf/evtFech/ideEvento',
                                   namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)

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

    xml = property(get_xml, set_xml)


class EvtFech(XMLNFe):
    def __init__(self):
        super(EvtFech, self).__init__()
        self.Id = TagCaracter(nome='evtFech', propriedade='id', raiz='//Reinf/evtFech',
                              namespace=NAMESPACE_EFDREINF, namespace_obrigatorio=False)
        self.ideEvento = IdeEvento()
        self.ideContri = IdeContri()
        self.ideRespInf = IdeRespInf()
        self.infoFech = InfoFech()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.Id.xml
        xml += self.ideEvento.xml
        xml += self.ideContri.xml
        xml += self.ideRespInf.xml
        xml += self.infoFech.xml
        xml += '</evtFech>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml = arquivo
            self.ideEvento.xml = arquivo
            self.ideContri.xml = arquivo
            self.infoFech.xml = arquivo

    xml = property(get_xml, set_xml)


class R4099(XMLNFe):
    def __init__(self):
        super(R4099, self).__init__()
        self.evtFech = EvtFech()
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'evtFech4000-v2_01_01.xsd'
        self.id_evento = ''
        self.Signature = Signature()
        self.evento = self.evtFech

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        # xml += ABERTURA
        xml += '<Reinf xmlns="' + NAMESPACE_EFDREINF + '">'
        xml += self.evtFech.xml

        #
        # Define a URI a ser assinada
        #
        self.Signature.URI = '#' + self.evtFech.Id.valor
        xml += self.Signature.xml
        xml += '</Reinf>'

        # Define o método de assinatura
        self.Signature.metodo = 'sha256'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.evtFech.xml = arquivo
            self.Signature.xml = self._le_noh('//Reinf/evtFech/sig:Signature')

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
        id_evento += self.evtFech.ideContri.tpInsc.valor
        id_evento += str(self.evtFech.ideContri.nrInsc.valor)[0:8] + '000000'
        # id_evento += str(self.evtInfoContri.ideContri.nrInsc.valor).zfill(14)
        id_evento += data_hora
        id_evento += str(sequencia).zfill(5)

        # Define o Id
        #
        self.evtFech.Id.valor = id_evento
        self.id_evento = id_evento

    xml = property(get_xml, set_xml)
