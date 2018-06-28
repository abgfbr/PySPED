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

#
# Versão 2.04.02
#
ESQUEMA_ATUAL_VERSAO_2 = 'v2.04.02'

from .soap_10100 import SOAPEnvio as SOAPEnvio_10100
from .soap_10100 import SOAPRetorno as SOAPRetorno_10100
from .soap_10100 import SOAPConsulta as SOAPConsulta_10100

from .envioLoteEventos_10101 import LoteEventosEsocial as LoteEventosEsocial_10101
from .retornoEnvioLoteEventos_10100 import RetornoLoteEventosEsocial as RetornoLoteEventosEsocial_10100
from .consultaLoteEventos_10000 import ConsultaLoteEventosEsocial as ConsultaLoteEventosEsocial_10000
from .retornoProcessamentoLote_10100 import RetornoProcessamentoLoteEsocial as RetornoProcessamentoLoteEsocial_10000

# S-1000
from .evtInfoEmpregador_20402 import S1000 as S1000_2

# S-1005
from .evtTabEstab_20402 import S1005 as S1005_2
from .evtTabEstab_20402 import InfoEntEduc as InfoEntEduc_2

# S-1010
from . evtTabRubrica_20402 import S1010 as S1010_2

# S-1020
from .evtTabLotacao_20402 import S1020 as S1020_2

# S-1030
from .evtTabCargo_20402 import S1030 as S1030_2
from .evtTabCargo_20402 import CargoPublico as S1030_CargoPublico_2

# S-1050
from .evtTabHorTur_20402 import S1050 as S1050_2
from .evtTabHorTur_20402 import HorarioIntervalo as HorarioIntervalo_2

# S-2200
from .evtAdmissao_20402 import S2200 as S2200_2
from .evtAdmissao_20402 import CTPS as S2200_CTPS_2
from .evtAdmissao_20402 import RIC as S2200_RIC_2
from .evtAdmissao_20402 import RG as S2200_RG_2
from .evtAdmissao_20402 import RNE as S2200_RNE_2
from .evtAdmissao_20402 import OC as S2200_OC_2
from .evtAdmissao_20402 import CNH as S2200_CNH_2
from .evtAdmissao_20402 import Brasil as S2200_Brasil_2
from .evtAdmissao_20402 import Dependente as S2200_Dependente_2
from .evtAdmissao_20402 import Contato as S2200_Contato_2
from .evtAdmissao_20402 import InfoCeletista as S2200_InfoCeletista_2
from .evtAdmissao_20402 import InfoEstatutario as S2200_InfoEstatutario_2
from .evtAdmissao_20402 import LocalTrabGeral as S2200_LocalTrabGeral_2
from .evtAdmissao_20402 import HorContratual as S2200_HorContratual_2
from .evtAdmissao_20402 import Horario as S2200_Horario_2
from .evtAdmissao_20402 import FiliacaoSindical as S2200_FiliacaoSindical_2
from .evtAdmissao_20402 import Observacoes as S2200_Observacoes_2
from .evtAdmissao_20402 import SucessaoVinc as S2200_SucessaoVinc_2

# S-2205
from .evtAltCadastral_20402 import S2205 as S2205_2
