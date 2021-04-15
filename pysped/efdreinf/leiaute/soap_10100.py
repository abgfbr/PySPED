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

from __future__ import division, print_function, unicode_literals

from pysped.xml_sped import (ABERTURA, TagDecimal, TagInteiro, XMLNFe,
                             tira_abertura)

from pysped.efdreinf.webservices_flags import (
    EFDREINF_AMBIENTE_PRODUCAO, EFDREINF_AMBIENTE_HOMOLOGACAO)

import os

DIRNAME = os.path.dirname(__file__)


class SOAPEnvio(XMLNFe):
    def __init__(self):
        super(SOAPEnvio, self).__init__()
        self.webservice = ''
        self.metodo = ''
        self.cUF    = None
        self.envio  = None
        self._header = {
            b'Content-Type': b'text/xml; charset=UTF-8',
            b'Accept-Encoding': b'gzip,deflate',
            b'Connection': b'Keep-Alive',
            b'User-Agent': b'Apache-HttpClient/4.1.1 (java 1.5)',
            b'SOAPAction': b'http://sped.fazenda.gov.br/RecepcaoLoteReinf/ReceberLoteEventos'
        }

    def get_xml(self):
        # self._header[b'SOAPAction'] = b'http://sped.fazenda.gov.br/RecepcaoLoteReinf/ReceberLoteEventos' + self.webservice.encode('utf-8') + b'/' + self.metodo.encode('utf-8')
        # self._header[b'SOAPAction'] = b'http://sped.fazenda.gov.br/RecepcaoLoteReinf/ReceberLoteEventos'

        xml = XMLNFe.get_xml(self)
        #xml += ABERTURA
        xml += '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sped="http://sped.fazenda.gov.br/">'
        xml +=     '<soapenv:Header/>'
        xml +=     '<soapenv:Body>'
        xml +=         '<sped:ReceberLoteEventos>'
        xml +=             '<sped:loteEventos>'
        xml +=                 self.envio.xml
        xml +=             '</sped:loteEventos>'
        xml +=         '</sped:ReceberLoteEventos>'
        xml +=     '</soapenv:Body>'
        xml += '</soapenv:Envelope>'
        return xml

    def set_xml(self):
        pass

    xml = property(get_xml, set_xml)

    def get_header(self):
        header = self._header
        return header

    header = property(get_header)


class SOAPRetorno(XMLNFe):
    def __init__(self):
        super(SOAPRetorno, self).__init__()
        self.webservice = ''
        self.metodo = ''
        self.resposta = None

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += '<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">'
        xml +=     '<s:Body xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">'
        xml +=         '<ReceberLoteEventosResponse xmlns="http://sped.fazenda.gov.br/">'
        xml +=             '<ReceberLoteEventosResult>'
        xml +=                  self.resposta.xml
        xml +=             '</ReceberLoteEventosResult>'
        xml +=         '</ReceberLoteEventosResponse>'
        xml +=     '</s:Body>'
        xml += '</s:Envelope>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.resposta.xml = arquivo

    xml = property(get_xml, set_xml)


class SOAPConsulta(XMLNFe):
    def __init__(self, ambiente=EFDREINF_AMBIENTE_HOMOLOGACAO):
        super(SOAPConsulta, self).__init__()
        self.ambiente = ambiente
        self.webservice = ''
        self.metodo = ''
        self.cUF    = None
        self.envio  = None
        self.tipoInscricaoContribuinte = ''
        self.numeroInscricaoContribuinte = ''
        self.numeroProtocoloFechamento = ''
        soap_action = b'http://sped.fazenda.gov.br/ConsultasReinf/ConsultaInformacoesConsolidadas' if self.ambiente == EFDREINF_AMBIENTE_PRODUCAO else b'http://sped.fazenda.gov.br/ConsultasReinf/ConsultaResultadoFechamento2099'
        self._header = {
            b'Content-Type': b'text/xml; charset=UTF-8',
            b'Accept-Encoding': b'gzip,deflate',
            b'Connection': b'Keep-Alive',
            b'User-Agent': b'Apache-HttpClient/4.1.1 (java 1.5)',
            b'SOAPAction': soap_action
        }

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sped="http://sped.fazenda.gov.br/">'
        xml +=     '<soapenv:Header/>'
        xml +=     '<soapenv:Body>'
        if self.ambiente == EFDREINF_AMBIENTE_PRODUCAO:
            xml +=      '<sped:ConsultaInformacoesConsolidadas>'
            xml +=          '<sped:tipoInscricaoContribuinte>%s</sped:tipoInscricaoContribuinte>' % self.tipoInscricaoContribuinte
            xml +=          '<sped:numeroInscricaoContribuinte>%s</sped:numeroInscricaoContribuinte>' % self.numeroInscricaoContribuinte
            xml +=          '<sped:numeroProtocoloFechamento>%s</sped:numeroProtocoloFechamento>' % self.numeroProtocoloFechamento
            xml +=      '</sped:ConsultaInformacoesConsolidadas>'
        elif self.ambiente == EFDREINF_AMBIENTE_HOMOLOGACAO:
            xml += '<sped:ConsultaResultadoFechamento2099>'
            xml +=             '<sped:tpInsc>%s</sped:tpInsc>' % self.tipoInscricaoContribuinte
            xml +=             '<sped:nrInsc>%s</sped:nrInsc>' % self.numeroInscricaoContribuinte
            xml +=             '<sped:numeroProtocoloFechamento>%s</sped:numeroProtocoloFechamento>' % self.numeroProtocoloFechamento
            xml +=         '</sped:ConsultaResultadoFechamento2099>'
        xml +=     '</soapenv:Body>'
        xml += '</soapenv:Envelope>'
        return xml

    def set_xml(self):
        pass

    xml = property(get_xml, set_xml)

    def get_header(self):
        header = self._header
        return header

    header = property(get_header)
