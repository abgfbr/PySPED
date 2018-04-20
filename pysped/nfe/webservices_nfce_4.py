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

from .webservices_flags import *

from . import webservices_4


SVRS = {
    # o servidor da consulta de cadastro é diferente dos demais...
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'                 : 'nfce.svrs.rs.gov.br',
        WS_NFE_RECEPCAO_EVENTO     : 'ws/recepcaoevento/recepcaoevento4.asmx',
        WS_NFE_AUTORIZACAO         : 'ws/NfeAutorizacao/NFeAutorizacao4.asmx',
        WS_NFE_CONSULTA_AUTORIZACAO: 'ws/NfeRetAutorizacao/NFeRetAutorizacao4.asmx',
        WS_NFE_INUTILIZACAO        : 'ws/nfeinutilizacao/nfeinutilizacao4.asmx',
        WS_NFE_CONSULTA            : 'ws/NfeConsulta/NfeConsulta4.asmx',
        WS_NFE_SITUACAO            : 'ws/NfeStatusServico/NfeStatusServico4.asmx',
    },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'                 : 'nfce-homologacao.svrs.rs.gov.br',
        WS_NFE_RECEPCAO_EVENTO     : 'ws/recepcaoevento/recepcaoevento4.asmx',
        WS_NFE_AUTORIZACAO         : 'ws/NfeAutorizacao/NFeAutorizacao4.asmx',
        WS_NFE_CONSULTA_AUTORIZACAO: 'ws/NfeRetAutorizacao/NFeRetAutorizacao4.asmx',
        WS_NFE_INUTILIZACAO        : 'ws/nfeinutilizacao/nfeinutilizacao4.asmx',
        WS_NFE_CONSULTA            : 'ws/NfeConsulta/NfeConsulta4.asmx',
        WS_NFE_SITUACAO            : 'ws/NfeStatusServico/NfeStatusServico4.asmx',
    }
}

UFAM = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'                 : 'nfce.sefaz.am.gov.br',
        WS_NFE_INUTILIZACAO        : 'nfce-services/services/NfeInutilizacao4',
        WS_NFE_CONSULTA            : 'nfce-services/services/NfeConsulta4',
        WS_NFE_SITUACAO            : 'nfce-services/services/NfeStatusServico4',
        WS_NFE_RECEPCAO_EVENTO     : 'nfce-services/services/RecepcaoEvento',
        WS_NFE_AUTORIZACAO         : 'nfce-services/services/NfeAutorizacao4',
        WS_NFE_CONSULTA_AUTORIZACAO: 'nfce-services/services/NfeRetAutorizacao4',
    },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'                 : 'homnfce.sefaz.am.gov.br',
        WS_NFE_INUTILIZACAO        : 'nfce-services/services/NfeInutilizacao4',
        WS_NFE_CONSULTA            : 'nfce-services/services/NfeConsulta4',
        WS_NFE_SITUACAO            : 'nfce-services/services/NfeStatusServico4',
        WS_NFE_RECEPCAO_EVENTO     : 'nfce-services/services/RecepcaoEvento',
        WS_NFE_AUTORIZACAO         : 'nfce-services/services/NfeAutorizacao4',
        WS_NFE_CONSULTA_AUTORIZACAO: 'nfce-services/services/NfeRetAutorizacao4',
    }
}

UFGO = webservices_4.UFGO

UFMT = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'                 : 'nfpe.sefaz.mt.gov.br',
        WS_NFE_INUTILIZACAO        : 'nfcews/v2/services/NfeInutilizacao4',
        WS_NFE_CONSULTA            : 'nfcews/v2/services/NfeConsulta4',
        WS_NFE_SITUACAO            : 'nfcews/v2/services/NfeStatusServico4',
        WS_NFE_RECEPCAO_EVENTO     : 'nfcews/v2/services/RecepcaoEvento4',
        WS_NFE_AUTORIZACAO         : 'nfcews/v2/services/NfeAutorizacao4',
        WS_NFE_CONSULTA_AUTORIZACAO: 'nfcews/v2/services/NfeRetAutorizacao4',
    },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'                 : 'homologacao.sefaz.mt.gov.br',
        WS_NFE_INUTILIZACAO        : 'nfcews/services/NfeInutilizacao4',
        WS_NFE_CONSULTA            : 'nfcews/services/NfeConsulta4',
        WS_NFE_SITUACAO            : 'nfcews/services/NfeStatusServico4',
        WS_NFE_RECEPCAO_EVENTO     : 'nfcews/services/RecepcaoEvento4',
        WS_NFE_AUTORIZACAO         : 'nfcews/services/NfeAutorizacao4',
        WS_NFE_CONSULTA_AUTORIZACAO: 'nfcews/services/NfeRetAutorizacao4',
    }
}

UFMS = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'                 : 'nfce.fazenda.ms.gov.br',
        WS_NFE_INUTILIZACAO        : 'ws/NFeInutilizacao4',
        WS_NFE_CONSULTA            : 'ws/NFeConsultaProtocolo4',
        WS_NFE_SITUACAO            : 'ws/NFeStatusServico4',
        WS_NFE_RECEPCAO_EVENTO     : 'ws/NFeRecepcaoEvento4',
        WS_NFE_AUTORIZACAO         : 'ws/NFeAutorizacao4',
        WS_NFE_CONSULTA_AUTORIZACAO: 'ws/NFeRetAutorizacao4',
    },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'                 : 'homologacao.nfce.ms.gov.br',
        WS_NFE_INUTILIZACAO        : 'ws/NFeInutilizacao4',
        WS_NFE_CONSULTA            : 'ws/NFeConsultaProtocolo4',
        WS_NFE_SITUACAO            : 'ws/NFeStatusServico4',
        WS_NFE_RECEPCAO_EVENTO     : 'ws/NFeRecepcaoEvento4',
        WS_NFE_AUTORIZACAO         : 'ws/NFeAutorizacao4',
        WS_NFE_CONSULTA_AUTORIZACAO: 'ws/NFeRetAutorizacao4',
    }
}

UFPR = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'                 : 'nfce.sefa.pr.gov.br',
        WS_NFE_INUTILIZACAO        : 'nfce/NFeInutilizacao4',
        WS_NFE_CONSULTA            : 'nfce/NFeConsultaProtocolo4',
        WS_NFE_SITUACAO            : 'nfce/NFeStatusServico4',
        WS_NFE_RECEPCAO_EVENTO     : 'nfce/NFeRecepcaoEvento4',
        WS_NFE_AUTORIZACAO         : 'nfce/NFeAutorizacao4',
        WS_NFE_CONSULTA_AUTORIZACAO: 'nfce/NFeRetAutorizacao4',
    },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'                 : 'homologacao.nfce.sefa.pr.gov.br',
        WS_NFE_INUTILIZACAO        : 'nfce/NFeInutilizacao4',
        WS_NFE_CONSULTA            : 'nfce/NFeConsultaProtocolo4',
        WS_NFE_SITUACAO            : 'nfce/NFeStatusServico4',
        WS_NFE_RECEPCAO_EVENTO     : 'nfce/NFeRecepcaoEvento4',
        WS_NFE_AUTORIZACAO         : 'nfce/NFeAutorizacao4',
        WS_NFE_CONSULTA_AUTORIZACAO: 'nfce/NFeRetAutorizacao4',
    }
}

UFRS = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'                 : 'nfce.sefazrs.rs.gov.br',
        WS_NFE_INUTILIZACAO        : 'ws/nfeinutilizacao/nfeinutilizacao4.asmx',
        WS_NFE_CONSULTA            : 'ws/NfeConsulta/NfeConsulta4.asmx',
        WS_NFE_SITUACAO            : 'ws/NfeStatusServico/NfeStatusServico4.asmx',
        WS_NFE_RECEPCAO_EVENTO     : 'ws/recepcaoevento/recepcaoevento4.asmx',
        WS_NFE_AUTORIZACAO         : 'ws/NfeAutorizacao/NFeAutorizacao4.asmx',
        WS_NFE_CONSULTA_AUTORIZACAO: 'ws/NfeRetAutorizacao/NFeRetAutorizacao4.asmx',
    },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'                 : 'nfce-homologacao.sefazrs.rs.gov.br',
        WS_NFE_INUTILIZACAO        : 'ws/nfeinutilizacao/nfeinutilizacao4.asmx',
        WS_NFE_CONSULTA            : 'ws/NfeConsulta/NfeConsulta4.asmx',
        WS_NFE_SITUACAO            : 'ws/NfeStatusServico/NfeStatusServico4.asmx',
        WS_NFE_RECEPCAO_EVENTO     : 'ws/recepcaoevento/recepcaoevento4.asmx',
        WS_NFE_AUTORIZACAO         : 'ws/NfeAutorizacao/NFeAutorizacao4.asmx',
        WS_NFE_CONSULTA_AUTORIZACAO: 'ws/NfeRetAutorizacao/NFeRetAutorizacao4.asmx',
    }
}

UFSP = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'                 : 'nfce.fazenda.sp.gov.br',
        WS_NFE_INUTILIZACAO        : 'ws/NFeInutilizacao4.asmx',
        WS_NFE_CONSULTA            : 'ws/NFeConsultaProtocolo4.asmx',
        WS_NFE_SITUACAO            : 'ws/NFeStatusServico4.asmx',
        WS_NFE_RECEPCAO_EVENTO     : 'ws/NFeRecepcaoEvento4.asmx',
        WS_NFE_AUTORIZACAO         : 'ws/NFeAutorizacao4.asmx',
        WS_NFE_CONSULTA_AUTORIZACAO: 'ws/NFeRetAutorizacao4.asmx',
    },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'                 : 'homologacao.nfce.fazenda.sp.gov.br',
        WS_NFE_INUTILIZACAO        : 'ws/NFeInutilizacao4.asmx',
        WS_NFE_CONSULTA            : 'ws/NFeConsultaProtocolo4.asmx',
        WS_NFE_SITUACAO            : 'ws/NFeStatusServico4.asmx',
        WS_NFE_RECEPCAO_EVENTO     : 'ws/NFeRecepcaoEvento4.asmx',
        WS_NFE_AUTORIZACAO         : 'ws/NFeAutorizacao4.asmx',
        WS_NFE_CONSULTA_AUTORIZACAO: 'ws/NFeRetAutorizacao4.asmx',
    }
}

ESTADO_WS = {
    'AC': SVRS,
    'AL': SVRS,
    'AM': UFAM,
    'AP': SVRS,
    'BA': SVRS,
    'CE': SVRS,
    'DF': SVRS,
    'ES': SVRS,
    'GO': UFGO,
    'MA': SVRS,
    'MG': UFRS,
    'MS': UFMS,
    'MT': UFMT,
    'PA': SVRS,
    'PB': SVRS,
    'PE': SVRS,
    'PI': SVRS,
    'PR': UFPR,
    'RJ': SVRS,
    'RN': SVRS,
    'RO': SVRS,
    'RR': SVRS,
    'RS': UFRS,
    'SC': SVRS,
    'SE': SVRS,
    'SP': UFSP,
    'TO': SVRS,
}

ESTADO_QRCODE = {
    'AC': {
        NFE_AMBIENTE_PRODUCAO: 'http://www.sefaznet.ac.gov.br/nfce/qrcode',
        NFE_AMBIENTE_HOMOLOGACAO: 'http://www.hml.sefaznet.ac.gov.br/nfce/qrcode',
    },
    'AL': {
        NFE_AMBIENTE_PRODUCAO: 'http://nfce.sefaz.al.gov.br/QRCode/consultarNFCe.jsp',
        NFE_AMBIENTE_HOMOLOGACAO: 'http://nfce.sefaz.al.gov.br/QRCode/consultarNFCe.jsp',
    },
    'AM': {
        NFE_AMBIENTE_PRODUCAO: 'http://sistemas.sefaz.am.gov.br/nfceweb/consultarNFCe.jsp',
        NFE_AMBIENTE_HOMOLOGACAO: 'homnfce.sefaz.am.gov.br/nfceweb/consultarNFCe.jsp',
    },
    'AP': {
        NFE_AMBIENTE_PRODUCAO: 'https://www.sefaz.ap.gov.br/nfce/nfcep.php',
        NFE_AMBIENTE_HOMOLOGACAO: 'https://www.sefaz.ap.gov.br/nfcehml/nfce.php',
    },
    'BA': {
        NFE_AMBIENTE_PRODUCAO: 'http://nfe.sefaz.ba.gov.br/servicos/nfce/modulos/geral/NFCEC_consulta_chave_acesso.aspx',
        NFE_AMBIENTE_HOMOLOGACAO: 'http://hnfe.sefaz.ba.gov.br/servicos/nfce/modulos/geral/NFCEC_consulta_chave_acesso.aspx',
    },
    'CE': {
        NFE_AMBIENTE_PRODUCAO: '',
        NFE_AMBIENTE_HOMOLOGACAO: 'http://nfceh.sefaz.ce.gov.br/pages/ShowNFCe.html',
    },
    'DF': {
        NFE_AMBIENTE_PRODUCAO: 'http://dec.fazenda.df.gov.br/ConsultarNFCe.aspx',
        NFE_AMBIENTE_HOMOLOGACAO: 'http://dec.fazenda.df.gov.br/ConsultarNFCe.aspx',
    },
    'ES': {
        NFE_AMBIENTE_PRODUCAO: '',
        NFE_AMBIENTE_HOMOLOGACAO: 'http://homologacao.sefaz.es.gov.br/ConsultaNFCe/qrcode.aspx',
    },
    'GO': {
        NFE_AMBIENTE_PRODUCAO: 'http://nfe.sefaz.go.gov.br/nfeweb/sites/nfce/danfeNFCe',
        NFE_AMBIENTE_HOMOLOGACAO: 'http://homolog.sefaz.go.gov.br/nfeweb/sites/nfce/danfeNFCe',
    },
    'MA': {
        NFE_AMBIENTE_PRODUCAO: 'http://nfce.sefaz.ma.gov.br/portal/consultarNFCe.jsp',
        NFE_AMBIENTE_HOMOLOGACAO: 'http://homologacao.sefaz.ma.gov.br/portal/consultarNFCe.jsp',
    },
    'MG': {
        NFE_AMBIENTE_PRODUCAO: '',
        NFE_AMBIENTE_HOMOLOGACAO: '',
    },
    'MS': {
        NFE_AMBIENTE_PRODUCAO: 'http://www.dfe.ms.gov.br/nfce/qrcode',
        NFE_AMBIENTE_HOMOLOGACAO: 'http://www.dfe.ms.gov.br/nfce/qrcode',
    },
    'MT': {
        NFE_AMBIENTE_PRODUCAO: 'http://www.sefaz.mt.gov.br/nfce/consultanfce',
        NFE_AMBIENTE_HOMOLOGACAO: 'http://homologacao.sefaz.mt.gov.br/nfce/consultanfce',
    },
    'PA': {
        NFE_AMBIENTE_PRODUCAO: 'https://appnfc.sefa.pa.gov.br/portal/view/consultas/nfce/nfceForm.seam',
        NFE_AMBIENTE_HOMOLOGACAO: 'https://appnfc.sefa.pa.gov.br/portal-homologacao/view/consultas/nfce/nfceForm.seam',
    },
    'PB': {
        NFE_AMBIENTE_PRODUCAO: 'http://www.receita.pb.gov.br/nfce',
        NFE_AMBIENTE_HOMOLOGACAO: 'http://www.receita.pb.gov.br/nfcehom',
    },
    'PE': {
        NFE_AMBIENTE_PRODUCAO: 'http://nfce.sefaz.pe.gov.br/nfce-web/consultarNFCe',
        NFE_AMBIENTE_HOMOLOGACAO: 'http://nfcehomolog.sefaz.pe.gov.br/nfce-web/consultarNFCe',
    },
    'PI': {
        NFE_AMBIENTE_PRODUCAO: 'http://webas.sefaz.pi.gov.br/nfceweb/consultarNFCe.jsf',
        NFE_AMBIENTE_HOMOLOGACAO: 'http://webas.sefaz.pi.gov.br/nfceweb-homologacao/consultarNFCe.jsf',
    },
    'PR': {
        NFE_AMBIENTE_PRODUCAO: 'http://www.fazenda.pr.gov.br/nfce/qrcode',
        NFE_AMBIENTE_HOMOLOGACAO: 'http://www.fazenda.pr.gov.br/nfce/qrcode',
    },
    'RJ': {
        NFE_AMBIENTE_PRODUCAO: 'http://www4.fazenda.rj.gov.br/consultaNFCe/QRCode',
        NFE_AMBIENTE_HOMOLOGACAO: 'http://www4.fazenda.rj.gov.br/consultaNFCe/QRCode',
    },
    'RN': {
        NFE_AMBIENTE_PRODUCAO: 'http://nfce.set.rn.gov.br/consultarNFCe.aspx',
        NFE_AMBIENTE_HOMOLOGACAO: 'http://hom.nfce.set.rn.gov.br/consultarNFCe.aspx',
    },
    'RO': {
        NFE_AMBIENTE_PRODUCAO: 'http://www.nfce.sefin.ro.gov.br/consultanfce/consulta.jsp',
        NFE_AMBIENTE_HOMOLOGACAO: 'http://www.nfce.sefin.ro.gov.br/consultanfce/consulta.jsp',
    },
    'RR': {
        NFE_AMBIENTE_PRODUCAO: 'https://www.sefaz.rr.gov.br/nfce/servlet/qrcode',
        NFE_AMBIENTE_HOMOLOGACAO: 'http://200.174.88.103:8080/nfce/servlet/qrcode',
    },
    'RS': {
        NFE_AMBIENTE_PRODUCAO: 'https://www.sefaz.rs.gov.br/NFCE/NFCE-COM.aspx',
        NFE_AMBIENTE_HOMOLOGACAO: 'https://www.sefaz.rs.gov.br/NFCE/NFCE-COM.aspx',
    },
    'SC': {
        NFE_AMBIENTE_PRODUCAO: '',
        NFE_AMBIENTE_HOMOLOGACAO: '',
    },
    'SE': {
        NFE_AMBIENTE_PRODUCAO: 'http://www.nfce.se.gov.br/portal/consultarNFCe.jsp',
        NFE_AMBIENTE_HOMOLOGACAO: 'http://www.hom.nfe.se.gov.br/portal/consultarNFCe.jsp',
    },
    'SP': {
        NFE_AMBIENTE_PRODUCAO: 'https://www.nfce.fazenda.sp.gov.br/qrcode',
        NFE_AMBIENTE_HOMOLOGACAO: 'https://www.homologacao.nfce.fazenda.sp.gov.br/qrcode',
    },
    'TO': {
        NFE_AMBIENTE_PRODUCAO: 'http://apps.sefaz.to.gov.br/portal-nfce/qrcodeNFCe',
        NFE_AMBIENTE_HOMOLOGACAO: 'http://apps.sefaz.to.gov.br/portal-nfce-homologacao/qrcodeNFCe',
    },
}

ESTADO_CONSULTA_NFCE = {
    'AC': {
        NFE_AMBIENTE_PRODUCAO: 'http://www.sefaznet.ac.gov.br/nfce/',
        NFE_AMBIENTE_HOMOLOGACAO: 'http://hml.sefaznet.ac.gov.br/nfce/',
    },
    'AL': {
        NFE_AMBIENTE_PRODUCAO: 'http://nfce.sefaz.al.gov.br/consultaNFCe.htm',
        NFE_AMBIENTE_HOMOLOGACAO: 'http://nfce.sefaz.al.gov.br/consultaNFCe.htm',
    },
    'AM': {
        NFE_AMBIENTE_PRODUCAO: 'http://sistemas.sefaz.am.gov.br/nfceweb/formConsulta.do',
        NFE_AMBIENTE_HOMOLOGACAO: 'http://homnfce.sefaz.am.gov.br/nfceweb/formConsulta.do',
    },
    'AP': {
        NFE_AMBIENTE_PRODUCAO: 'https://www.sefaz.ap.gov.br/sate/seg/SEGf_AcessarFuncao.jsp?cdFuncao=FIS_1261',
        NFE_AMBIENTE_HOMOLOGACAO: 'https://www.sefaz.ap.gov.br/nfcehml/nfce.php',
    },
    'BA': {
        NFE_AMBIENTE_PRODUCAO: 'http://nfe.sefaz.ba.gov.br/servicos/nfce/default.aspx',
        NFE_AMBIENTE_HOMOLOGACAO: 'http://nfe.sefaz.ba.gov.br/servicos/nfce/default.aspx',
    },
    'CE': {
        NFE_AMBIENTE_PRODUCAO: '',
        NFE_AMBIENTE_HOMOLOGACAO: 'http://nfceh.sefaz.ce.gov.br/pages/consultaChaveAcesso.jsf',
    },
    'DF': {
        NFE_AMBIENTE_PRODUCAO: 'http://dec.fazenda.df.gov.br/nfce',
        NFE_AMBIENTE_HOMOLOGACAO: 'http://dec.fazenda.df.gov.br/nfce',
    },
    'ES': {
        NFE_AMBIENTE_PRODUCAO: '',
        NFE_AMBIENTE_HOMOLOGACAO: 'http://app.sefaz.es.gov.br/ConsultaNFCe',
    },
    'GO': {
        NFE_AMBIENTE_PRODUCAO: 'http://nfe.sefaz.go.gov.br/nfeweb/jsp/ConsultaDANFENFCe.jsf',
        NFE_AMBIENTE_HOMOLOGACAO: 'http://homolog.sefaz.go.gov.br/nfeweb/jsp/ConsultaDANFENFCe.jsf',
    },
    'MA': {
        NFE_AMBIENTE_PRODUCAO: 'http://www.nfce.sefaz.ma.gov.br/portal/consultaNFe.do',
        NFE_AMBIENTE_HOMOLOGACAO: 'http://www.hom.nfce.sefaz.ma.gov.br/portal/consultaNFe.do',
    },
    'MG': {
        NFE_AMBIENTE_PRODUCAO: '',
        NFE_AMBIENTE_HOMOLOGACAO: '',
    },
    'MS': {
        NFE_AMBIENTE_PRODUCAO: 'http://www.dfe.ms.gov.br/nfce',
        NFE_AMBIENTE_HOMOLOGACAO: 'http://www.dfe.ms.gov.br/nfce',
    },
    'MT': {
        NFE_AMBIENTE_PRODUCAO: 'http://www.sefaz.mt.gov.br/nfce/consultanfce',
        NFE_AMBIENTE_HOMOLOGACAO: 'http://homologacao.sefaz.mt.gov.br/nfce/consultanfce',
    },
    'PA': {
        NFE_AMBIENTE_PRODUCAO: 'https://appnfc.sefa.pa.gov.br/portal/view/consultas/nfce/consultanfce.seam',
        NFE_AMBIENTE_HOMOLOGACAO: 'https://appnfc.sefa.pa.gov.br/portal-homologacao/view/consultas/nfce/consultanfce.seam',
    },
    'PB': {
        NFE_AMBIENTE_PRODUCAO: 'http://www.receita.pb.gov.br/nfce',
        NFE_AMBIENTE_HOMOLOGACAO: 'http://www.receita.pb.gov.br/nfcehom',
    },
    'PE': {
        NFE_AMBIENTE_PRODUCAO: 'http://nfce.sefaz.pe.gov.br/nfce-web/consultarNFCe',
        NFE_AMBIENTE_HOMOLOGACAO: 'http://nfcehomolog.sefaz.pe.gov.br/nfce-web/consultarNFCe',
    },
    'PI': {
        NFE_AMBIENTE_PRODUCAO: '',
        NFE_AMBIENTE_HOMOLOGACAO: '',
    },
    'PR': {
        NFE_AMBIENTE_PRODUCAO: 'http://www.fazenda.pr.gov.br/',
        NFE_AMBIENTE_HOMOLOGACAO: 'http://www.fazenda.pr.gov.br/',
    },
    'RJ': {
        NFE_AMBIENTE_PRODUCAO: 'http://nfce.fazenda.rj.gov.br/consulta',
        NFE_AMBIENTE_HOMOLOGACAO: 'http://nfce.fazenda.rj.gov.br/consulta',
    },
    'RN': {
        NFE_AMBIENTE_PRODUCAO: 'http://nfce.set.rn.gov.br/portalDFE/NFCe/ConsultaNFCe.aspx',
        NFE_AMBIENTE_HOMOLOGACAO: 'http://hom.nfce.set.rn.gov.br/portalDFE/NFCe/ConsultaNFCe.aspx',
    },
    'RO': {
        NFE_AMBIENTE_PRODUCAO: 'http://www.nfce.sefin.ro.gov.br',
        NFE_AMBIENTE_HOMOLOGACAO: 'http://www.nfce.sefin.ro.gov.br/consultaAmbHomologacao.jsp',
    },
    'RR': {
        NFE_AMBIENTE_PRODUCAO: 'https://www.sefaz.rr.gov.br/nfce/servlet/wp_consulta_nfce',
        NFE_AMBIENTE_HOMOLOGACAO: 'http://200.174.88.103:8080/nfce/servlet/wp_consulta_nfce',
    },
    'RS': {
        NFE_AMBIENTE_PRODUCAO: 'https://www.sefaz.rs.gov.br/NFE/NFE-NFC.aspx',
        NFE_AMBIENTE_HOMOLOGACAO: 'https://www.sefaz.rs.gov.br/NFE/NFE-NFC.aspx',
    },
    'SC': {
        NFE_AMBIENTE_PRODUCAO: '',
        NFE_AMBIENTE_HOMOLOGACAO: '',
    },
    'SE': {
        NFE_AMBIENTE_PRODUCAO: '',
        NFE_AMBIENTE_HOMOLOGACAO: '',
    },
    'SP': {
        NFE_AMBIENTE_PRODUCAO: 'https://www.nfce.fazenda.sp.gov.br/NFCeConsultaPublica/Paginas/ConsultaQRCode.aspx',
        NFE_AMBIENTE_HOMOLOGACAO: 'https://www.homologacao.nfce.fazenda.sp.gov.br/NFCeConsultaPublica/Paginas/ConsultaPublica.aspx',
    },
    'TO': {
        NFE_AMBIENTE_PRODUCAO: '',
        NFE_AMBIENTE_HOMOLOGACAO: '',
    },
}

