# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 10:06:28 2022

@author: jfeck
"""

import os
import pandas as pd
from datetime import datetime

###############################################################################################################
# Functions
###############################################################################################################
'''
def get_config_item(dict_item, var):
    config_keyvals = dict(config.items(dict_item))
    val = config_keyvals[var]
    print('INFO: ' + var + ' : ' + val)
    if not var:
        raise Exception('ERROR: ' + var + " cannot be an empty string")
    return val
'''
       
###############################################################################################################
# Get config values
###############################################################################################################

data_incoming_foldername = 'data_incoming'
data_outgoing_foldername = 'data_outgoing'

path_script = os.path.realpath(__file__)
path_project = os.path.dirname(os.path.dirname(path_script))
path_incoming = os.path.join(path_project, data_incoming_foldername)
path_outgoing = os.path.join(path_project, data_outgoing_foldername)

selic_url = 'https://www.bcb.gov.br/api/servico/sitebcb/historicotaxasjuros'

cols_to_rename = {'NumeroReuniaoCopom':'numero_reuniao_copom', 'ReuniaoExtraordinaria':'flag_reuniao_extraordinaria', 'DataReuniaoCopom':'data_reuniao_copom', 'Vies':'vies', 'UsoMetaSelic':'flag_uso_meta_selic', 'DataInicioVigencia':'data_inicio_vigencia', 'DataFimVigencia':'data_fim_vigencia', 'MetaSelic':'meta_selic', 'TaxaTban':'taxa_tban', 'TaxaSelicEfetivaVigencia':'taxa_selic_efetiva_vigencia', 'TaxaSelicEfetivaAnualizada':'taxa_selic_efetiva_anualizada'}

df = pd.read_json(selic_url)
df = df["conteudo"].apply(pd.Series)
df = df.rename(columns=cols_to_rename)
df['data_inicio_vigencia'] = pd.to_datetime(df['data_inicio_vigencia']).dt.date
df['data_fim_vigencia'] = pd.to_datetime(df['data_fim_vigencia']).dt.date
df['data_reuniao_copom'] = pd.to_datetime(df['data_reuniao_copom']).dt.date

min_data_inicio = df['data_inicio_vigencia'].min()
today_date = datetime.today()

min_data_inicio_str = min_data_inicio.strftime('%Y-%m-%d')
today_date_str = today_date.strftime('%Y-%m-%d')

df_date = pd.DataFrame({'report_date':pd.date_range(start=min_data_inicio_str, end=today_date_str)})
df_date['report_date'] = pd.to_datetime(df_date['report_date']).dt.date

df['key'] = 1
df_date['key'] = 1
df = df.merge(df_date, on='key', how='outer')
df = df.drop(columns=['key'])

df['data_fim_vigencia'] = df['data_fim_vigencia'].fillna(today_date.date())
df = df[(df['report_date'] >= df['data_inicio_vigencia']) & (df['report_date'] <= df['data_fim_vigencia'])]

out_file_path = os.path.join(path_outgoing, 'selic_historica.xlsx')
df.to_excel(out_file_path, sheet_name = 'selic_historica', index=False)

