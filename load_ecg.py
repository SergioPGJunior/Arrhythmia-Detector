import wfdb

def load_ecg(file):
    # Leitura e armazenamento dos dados
    record = wfdb.rdrecord(file)

    # Leitura e armazenamento das anotações
    annotation = wfdb.rdann(file, "atr")

    #Extrai o sinal
    p_signal = record.p_signal

    #Verifica se a frequência é 360
    assert record.fs == 360, "Frequência de amostragem não é 360"

    #Extrai os símbolos e anotações
    atr_sym = annotation.symbol
    atr_sample = annotation.sample

    return p_signal, atr_sym, atr_sample