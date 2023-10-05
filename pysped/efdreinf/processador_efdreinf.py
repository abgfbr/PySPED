# -*- coding: utf-8 -*-
#
# PySPED - Python libraries to deal with Brazil's SPED Project
#
# Copyright (C) 2010-2012
# Copyright (C) Wagner Pereira <wagner.pereira at tauga.com.br>
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

import os
import sys
import requests
from datetime import datetime
import time
from uuid import uuid4
from builtins import str
from io import open
from ..nfe.processador_nfe import ProcessadorNFe, ProcessoNFe as ProcessoEFDReinf, ConexaoHTTPS

from .webservices_flags import *
from . import webservices_3
from .leiaute import SOAPEnvio_10100, SOAPRetorno_10100, SOAPConsulta_10100
from .leiaute import LoteEventoEFDReinf_v1_03_02
from .leiaute import RetornoLoteEventosEFDReinf_v1_03_02
from .leiaute import RetornoTotalizadorContribuinteEFDReinf_v1_03_02 # R-5011
from .leiaute import LoteEventoAssincronoEFDReinf_v1_00_00
from .leiaute import RetornoLoteEventosAssincronoEFDReinf_v1_00_00


class ProcessadorEFDReinf(ProcessadorNFe):
    def __init__(self):
        super(ProcessadorEFDReinf, self).__init__()
        self.tipoInscricaoContribuinte = ''
        self.numeroInscricaoContribuinte = ''
        self.numeroProtocoloFechamento = ''

    def _configura_servico(self, servico, envio, resposta, ambiente=None, somente_ambiente_nacional=False):
        if ambiente is None:
            ambiente = self.ambiente

        webservices = webservices_3
        metodo_ws = webservices.METODO_WS[ambiente]

        # Se for Consulta deve usar o SOAPConsulta ao invés do SOAPEnvio
        if servico == WS_EFDREINF_CONSULTA:
            self._soap_envio = SOAPConsulta_10100(ambiente)
            self._soap_envio.tipoInscricaoContribuinte = self.tipoInscricaoContribuinte
            self._soap_envio.numeroInscricaoContribuinte = self.numeroInscricaoContribuinte
            self._soap_envio.numeroProtocoloFechamento = self.numeroProtocoloFechamento
        else:
            self._soap_envio = SOAPEnvio_10100()
        self._soap_retorno = SOAPRetorno_10100()

        ws_a_usar = webservices.SVEFDREINF

        self._servidor = ws_a_usar[ambiente]['servidor']
        self._url      = ws_a_usar[ambiente][servico]

        self._soap_envio.webservice = metodo_ws[servico]['webservice']
        self._soap_envio.metodo     = metodo_ws[servico]['metodo']
        self._soap_envio.envio      = envio

        self._soap_retorno.webservice = self._soap_envio.webservice
        self._soap_retorno.metodo     = self._soap_envio.metodo
        self._soap_retorno.resposta   = resposta

    def enviar_lote(self, lista_eventos=[]):
        # envio = LoteEventoEFDReinf_v1_03_02()
        # resposta = RetornoLoteEventosEFDReinf_v1_03_02()
        envio = LoteEventoAssincronoEFDReinf_v1_00_00()
        resposta = RetornoLoteEventosAssincronoEFDReinf_v1_00_00()
        processo = ProcessoEFDReinf(webservice=WS_EFDREINF_ENVIO, envio=envio, resposta=resposta)

        # self.ambiente = lista_eventos[0].evtInfoContri.ideEvento.tpAmb.valor
                
        for evento in lista_eventos:            
            self.certificado.assina_xmlnfe(evento)
            evento.validar()
            
        envio.envioLoteEventos.eventos = lista_eventos
        envio.envioLoteEventos.tpInsc.valor = lista_eventos[0].evento.ideContri.tpInsc.valor
        envio.envioLoteEventos.nrInsc.valor = lista_eventos[0].evento.ideContri.nrInsc.valor
        envio.validar()

        if self.salvar_arquivos:
            for n in lista_eventos:                
                self.caminho = self.monta_caminho_efdreinf(ambiente=self.ambiente, id_evento=n.id_evento)
                arq = open(self.caminho + n.id_evento + '.xml', 'w', encoding='utf-8')
                arq.write(n.xml)
                arq.close()
                # arq.closeConsReciEFDReinf_300

            arq = open(self.caminho + n.id_evento + '-env-lot.xml', 'w')
            arq.write(envio.xml)
            arq.close()

        self._conectar_servico(WS_EFDREINF_ENVIO, envio, resposta)

        if resposta.status_code in [404]:
            raise Exception("Ambiente não encontrado !")

        ## resposta.validar()
        # if self.salvar_arquivos:
        #     nome_arq = self.caminho + str(envio.idLote.valor).strip().rjust(15, '0') + '-rec'
        #
        #     if resposta.cStat.valor != '103':
        #         nome_arq += '-rej.xml'
        #     else:
        #         nome_arq += '.xml'
        #
        #     arq = open(nome_arq, 'w', encoding='utf-8')
        #     arq.write(resposta.xml)
        #     arq.close()

        # if self.salvar_arquivos:
        #     nome_arq = self.caminho enviar_lote+ id_evento + '-rec'
        #
        #     if resposta.retornoEnvioLoteEventos.status.cdResposta.valor != '201':
        #         nome_arq += '-rej.xml'
        #     else:
        #         nome_arq += '.xml'
        #
        #     arq = open(nome_arq, 'w', encoding='utf-8')
        #     arq.write(resposta.xml)
        #     arq.close()

        return processo

    def _conectar_servico(self, servico, envio, resposta, ambiente=None, somente_ambiente_nacional=False):
        self._configura_servico(servico, envio, resposta, ambiente=ambiente,
                                somente_ambiente_nacional=somente_ambiente_nacional)

        #try:
        self.certificado.prepara_certificado_arquivo_pfx()

        #
        # Salva o certificado e a chave privada para uso na conexão HTTPS
        # Salvamos como um arquivo de nome aleatório para evitar o conflito
        # de uso de vários certificados e chaves diferentes na mesma máquina
        # ao mesmo tempo
        #
        self.caminho_temporario = self.caminho_temporario or '/tmp/'

        nome_arq_chave = self.caminho_temporario + uuid4().hex
        arq_tmp = open(nome_arq_chave, 'w', encoding='utf-8')
        arq_tmp.write(self.certificado.chave.decode('utf-8'))
        arq_tmp.close()

        nome_arq_certificado = self.caminho_temporario + uuid4().hex
        arq_tmp = open(nome_arq_certificado, 'w', encoding='utf-8')
        arq_tmp.write(self.certificado.certificado)
        arq_tmp.close()
        #import StringIO
        #nome_arq_chave = StringIO.StringIO()
        #nome_arq_chave.write(self.certificado.chave)
        #nome_arq_certificado = StringIO.StringIO()
        #nome_arq_certificado.write(self.certificado.certificado)

        #con = HTTPSConnection(self._servidor, key_file=nome_arq_chave, cert_file=nome_arq_certificado)
        con = ConexaoHTTPS(self._servidor, key_file=nome_arq_chave, cert_file=nome_arq_certificado)
        #con.request('POST', '/' + self._url, self._soap_envio.xml.decode('utf-8'), self._soap_envio.header)
        #
        # É preciso definir o POST abaixo como bytestring, já que importamos
        # os unicode_literals... Dá um pau com xml com acentos sem isso...
        #
        response = False
        if sys.version_info.major == 2:
            # con.request(b'POST', self._url.encode('utf-8'), envio.xml.encode('utf-8'), {b'Content-Type': b'application/xml'})
            if servico == 1:
                response = requests.get(
                    'https://pre-reinf.receita.economia.gov.br/consulta/lotes/{}'.format(self.numeroProtocoloFechamento),
                    cert=(nome_arq_certificado, nome_arq_chave))
            else:
                response = requests.post(
                    'https://pre-reinf.receita.economia.gov.br/recepcao/lotes',
                    envio.xml, headers={'Content-Type': 'application/xml'},
                    cert=(nome_arq_certificado, nome_arq_chave))
        else:
            con.request('POST', '/' + self._url, self._soap_envio.xml.encode('utf-8'), self._soap_envio.header)

        # resp = con.getresponse()

        #
        # Apagamos os arquivos do certificado e o da chave privada, para evitar
        # um potencial risco de segurança; muito embora o uso da chave privada
        # para assinatura exija o uso da senha, pode haver serviços que exijam
        # apenas o uso do certificado para validar a identidade, independente
        # da existência de assinatura digital
        #
        os.remove(nome_arq_chave)
        os.remove(nome_arq_certificado)

        resposta.set_xml(response.text)

        # Dados do envelope de envio salvos para possível debug
        envio.original = self._soap_envio.xml

        self._soap_retorno.resposta.status_code = response.status_code
        self._soap_retorno.resposta.reason = response.reason
        self._soap_retorno.resposta.original = response.content
        self._soap_retorno.xml = self._soap_retorno.resposta.original

        # Dados da resposta salvos para possível debug
        # self._soap_retorno.resposta.version  = resp.version
        # self._soap_retorno.resposta.status   = resp.status
        # if sys.version_info.major == 2:
        #     self._soap_retorno.resposta.reason   = resp.reason.decode('utf-8')
        # else:
        #     self._soap_retorno.resposta.reason   = resp.reason
        # self._soap_retorno.resposta.msg      = resp.msg
        # if sys.version_info.major == 2:
        #     self._soap_retorno.resposta.original = resp.read().decode('utf-8')
        # else:
        #     self._soap_retorno.resposta.original = resp.read()
        #
        # # Tudo certo!
        # if self._soap_retorno.resposta.status == 200:
        #     if sys.version_info.major == 2:
        #         self._soap_retorno.xml = self._soap_retorno.resposta.original
        #     else:
        #         self._soap_retorno.xml = self._soap_retorno.resposta.original.decode('utf-8')
        #except Exception, e:
            #raise e
        #else:
        con.close()

    def monta_caminho_efdreinf(self, ambiente, id_evento):
        caminho = self.caminho

        if ambiente == 1:
            caminho = os.path.join(caminho, 'producao/')
        else:
            caminho = os.path.join(caminho, 'homologacao/')

        # ID2035418760001332018050212504900001
        data = '20' + id_evento[19:21] + '-' + id_evento[21:23]
        caminho = os.path.join(caminho, data + '/')
        caminho = os.path.join(caminho, id_evento + '/')
        try:
            os.makedirs(caminho)
        except:
            pass

        return caminho

    def consultar_fechamento(self, ambiente=None):
        # envio = RetornoTotalizadorContribuinteEFDReinf_v1_03_02()
        # resposta = RetornoTotalizadorContribuinteEFDReinf_v1_03_02()
        envio = LoteEventoAssincronoEFDReinf_v1_00_00()
        resposta = RetornoLoteEventosAssincronoEFDReinf_v1_00_00()

        processo = ProcessoEFDReinf(webservice=WS_EFDREINF_CONSULTA, envio=False, resposta=resposta)

        if ambiente is None:
            ambiente = self.ambiente

        # envio.tpAmb.valor = ambiente
        # envio.nRec.valor  = numero_recibo

        #envio.validar()
        # if self.salvar_arquivos:
        #     arq = open(self.caminho + str(envio.nRec.valor).strip().rjust(15, '0') + '-ped-rec.xml', 'w', encoding='utf-8')
        #     arq.write(envio.xml)
        #     arq.close()

        self._conectar_servico(WS_EFDREINF_CONSULTA, envio=envio, resposta=resposta, ambiente=ambiente)

        #resposta.validar()
        # if self.salvar_arquivos:
        #     nome_arq = self.caminho + str(envio.nRec.valor).strip().rjust(15, '0') + '-pro-rec'
        #
        #     if resposta.cStat.valor != '104':
        #         nome_arq += '-rej.xml'
        #     else:
        #         nome_arq += '.xml'
        #
        #     arq = open(nome_arq, 'w', encoding='utf-8')
        #     arq.write(resposta.xml)
        #     arq.close()
        #
        #     #
        #     # Salvar os resultados dos processamentos
        #     #
        #     for pn in resposta.protMDFe:
        #         nome_arq = self.caminho + str(pn.infProt.chMDFe.valor).strip().rjust(44, '0') + '-pro-mdfe-'
        #
        #         # MDF-e autorizado
        #         if pn.infProt.cStat.valor == '100':
        #             nome_arq += 'aut.xml'
        #
        #         # MDF-e rejeitado
        #         else:
        #             nome_arq += 'rej.xml'
        #
        #         arq = open(nome_arq, 'w', encoding='utf-8')
        #         arq.write(pn.xml)
        #         arq.close()

        return processo
