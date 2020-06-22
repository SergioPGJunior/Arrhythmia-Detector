
import pandas as pd
import numpy as np
import wfdb
import ast

#Caminho onde os arquivos da base de dados estão armazenados
path = "/content/drive/My Drive/mit-bih-arrhythmia-database-1.0.0/"

#Cria um dataframe com os nomes dos arquivos
rec = pd.read_csv(path + "RECORDS", names="n", dtype=str)

#Leitura e armazenamento dos dados
data = [wfdb.io.rdsamp(path + filename) for filename in rec.n]

#Leitura e armazenamento das anotações
annotation = [wfdb.io.rdann(path + filename,"atr") for filename in rec.n]

#Separa os dados em duas matrizes: MLII e V5
MLII = []
V1 = []

for i in data:
    amostra = i[0].transpose()
    MLII.append(amostra[0])
    V1.append(amostra[1])

#Teste de detecção dos rpeaks utilizando a função xqrs disponível na biblioteca wfdb
from wfdb import processing
sig = MLII[0]
xqrs = processing.xqrs_detect(sig, fs=360)

#Teste com todos os algoritmos para encontrar os rpeaks disponíveis na biblioteca NeuroKit
import neurokit2 as nk
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.externals import joblib

ecg = MLII[0]
cleaned = nk.ecg_clean(ecg, sampling_rate=360)

neurokit = nk.ecg_findpeaks(nk.ecg_clean(ecg, method="neurokit"),sampling_rate=360, method="neurokit")
pantompkins1985 = nk.ecg_findpeaks(nk.ecg_clean(ecg, method="pantompkins1985"),sampling_rate=360, method="pantompkins1985")
hamilton2002 = nk.ecg_findpeaks(nk.ecg_clean(ecg, method="hamilton2002"),sampling_rate=360, method="hamilton2002")
martinez2003 = nk.ecg_findpeaks(cleaned,sampling_rate=360, method="martinez2003")
christov2004 = nk.ecg_findpeaks(cleaned,sampling_rate=360, method="christov2004")
gamboa2008 = nk.ecg_findpeaks(nk.ecg_clean(ecg, method="gamboa2008"),sampling_rate=360, method="gamboa2008")
elgendi2010 = nk.ecg_findpeaks(nk.ecg_clean(ecg, method="elgendi2010"),sampling_rate=360, method="elgendi2010")
engzeemod2012 = nk.ecg_findpeaks(nk.ecg_clean(ecg, method="engzeemod2012"),sampling_rate=360, method="engzeemod2012")
kalidas2017 = nk.ecg_findpeaks(nk.ecg_clean(ecg, method="kalidas2017"),sampling_rate=360, method="kalidas2017")
rodrigues2020 = nk.ecg_findpeaks(cleaned,sampling_rate=360, method="rodrigues2020")

#Teste de Leitura e armazenamento das anotações da base de dados
annotation = wfdb.io.rdann("/content/drive/My Drive/mit-bih-arrhythmia-database-1.0.0/100","atr")

#Cria um dtaaframe onde a primeira coluna é a amostra e a segunda o label atribuido (chamando a fç wfdb.io.show_ann_labels() podemos ver a legenda dos labels)
data = {'sample': annotation.sample,'type': annotation.symbol}
df = pd.DataFrame(data)

#Cria um dataframe apenas com as amostras onde picos R (com label N) são encontrados
rpeaks_notes = df[df['type'] == 'N']

#help(wfdb.Annotation)