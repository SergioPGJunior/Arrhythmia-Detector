import pandas as pd
import numpy as np
import wfdb
import ast
import csv

# Caminho onde os arquivos da base de dados estão armazenados
path = "C:/Users/sergi/Documents/Projeto_artigo/Bases de dados/ptb-diagnostic-ecg-database-1.0.0/"

# Cria um dataframe com os nomes dos arquivos
rec = pd.read_csv(path + "RECORDS", names="n", dtype=str)

#Leitura e armazenamento dos headers
headers = [{'arquivo': filename, 'cabecalho': wfdb.io.rdheader(path + filename)} for filename in rec.n]

sub = 'Renal insufficiency'

#Pesquisa quais pacientes possuem problemas renais e retorna o caminho para os arquivos de ECG dentro do diretório do banco
pacientes_renais = []
for pacient in headers:
    for s in pacient['cabecalho'].__dict__['comments']:
        if sub in s:
            pacientes_renais.append(pacient['arquivo'])


print(pacientes_renais)
print(len(pacientes_renais))

with open(path + 'renais.csv','w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(pacientes_renais)

# Guardei essa linha para separação dos pacientes entre fumantes e não fumantes
#pacientes_renais = [pacient['arquivo'] for pacient in headers if 'Smoker: yes' in pacient['cabecalho'].__dict__['comments']]
#218 não fumantes
#190 fumantes




