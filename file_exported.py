import os.path
from datetime import datetime
from take_report import formatacao

def formatar_tabela(path_file_exported, path_new_file, new_name_file):
    lista_arquivos = os.listdir(path_file_exported)
    data_horario_atual = datetime.now()

    data_atual = data_horario_atual.strftime('%Y%m%d')
    hora = data_horario_atual.strftime('%H')
    hora = str(hora)

    for arquivo_csv in lista_arquivos: # Iterando sobre todos os arquivos de downloads
        if data_atual == arquivo_csv[23:31] and '.csv' == arquivo_csv[38:]: # Arquivos CSV exportados
            minutos = data_horario_atual.strftime('%M')

            for i in range(5):
                minutos = int(minutos)
                if minutos < 10 and minutos >= 0:
                    minutos = '0' + str(minutos)
                minutos = str(minutos)
                horario_atual = hora + minutos
                
                if horario_atual == arquivo_csv[32:36]: # Pegando mesma data e hora e minuto correspondente
                    formatacao(path_file_exported, arquivo_csv, path_new_file, new_name_file)          
                else:
                    minutos = int(minutos)
                    if minutos >= 1:
                        minutos -=1
                        continue

