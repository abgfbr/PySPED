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
        }

    def get_xml(self):
        self._header[b'SOAPAction'] =  b'http://www.esocial.gov.br/servicos/empregador/lote/eventos/envio/v1_1_0/' + self.webservice.encode('utf-8') + b'/' + self.metodo.encode('utf-8')

        xml = XMLNFe.get_xml(self)
        #xml += ABERTURA
        xml += '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:v1="http://www.esocial.gov.br/servicos/empregador/lote/eventos/envio/v1_1_0">'
        xml +=     '<soapenv:Header/>'
        xml +=     '<soapenv:Body>'
        xml +=         '<v1:EnviarLoteEventos>'
        xml +=             '<v1:loteEventos>'
        xml +=                 self.envio.xml
        xml +=             '</v1:loteEventos>'
        xml +=         '</v1:EnviarLoteEventos>'
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
        xml +=     '<s:Body>'
        xml +=         '<EnviarLoteEventosResponse xmlns="http://www.esocial.gov.br/servicos/empregador/lote/eventos/envio/v1_1_0">'
        xml +=             '<EnviarLoteEventosResult>'
        xml +=                  self.resposta.xml
        xml +=             '</EnviarLoteEventosResult>'
        xml +=         '</EnviarLoteEventosResponse>'
        xml +=     '</s:Body>'
        xml += '</s:Envelope>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.resposta.xml = arquivo

    xml = property(get_xml, set_xml)


class SOAPConsulta(XMLNFe):
    def __init__(self):
        super(SOAPConsulta, self).__init__()
        self.webservice = ''
        self.metodo = ''
        self.cUF    = None
        self.envio  = None
        self._header = {
            b'Content-Type': b'text/xml; charset=UTF-8',
            b'Accept-Encoding': b'gzip,deflate',
            b'Connection': b'Keep-Alive',
            b'User-Agent': b'Apache-HttpClient/4.1.1 (java 1.5)',
        }

    def get_xml(self):
        self._header[b'SOAPAction'] =  b'http://www.esocial.gov.br/servicos/empregador/lote/eventos/envio/consulta/retornoProcessamento/v1_1_0/' + self.webservice.encode('utf-8') + b'/' + self.metodo.encode('utf-8')

        xml = XMLNFe.get_xml(self)
        #xml += ABERTURA
        xml += '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:v1="http://www.esocial.gov.br/servicos/empregador/lote/eventos/envio/consulta/retornoProcessamento/v1_1_0">'
        xml +=     '<soapenv:Header/>'
        xml +=     '<soapenv:Body>'
        xml +=         '<v1:ConsultarLoteEventos>'
        xml +=             '<v1:consulta>'
        xml +=                 self.envio.xml
        xml +=             '</v1:consulta>'
        xml +=         '</v1:ConsultarLoteEventos>'
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
