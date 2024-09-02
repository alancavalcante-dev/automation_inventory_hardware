import pandas as pd
import csv


def formatacao(path_file_exported, arquivo_csv, path_new_file, new_name_file):

    arquivo_csv = path_file_exported + arquivo_csv
    relatorio_gerado = path_new_file + new_name_file
    

    with open(arquivo_csv, 'r',encoding='latin1') as f:
        reader = csv.reader((x.replace('\0', '')for x in f), delimiter=';') 
        lista = []
        for row in reader:
            if len(row) != 0:
                lista.append(row)


    coluna = lista[0]
    for linha in coluna:
        formatado = linha.replace("\t","\n")
        coluna_formatada = formatado.splitlines()
    coluna = coluna_formatada


    valores = lista[1:]
    novos_valores = []
    for linha in valores:
        for caracter in linha:
            formatado = caracter.replace("\t","\n")
            valores_formatada = formatado.splitlines()
            novos_valores.append(valores_formatada)


    df = pd.DataFrame(novos_valores, columns=coluna)

    df = df.rename(columns={'ÿþCliente': 'Cliente'})


    df = df.drop(['Cliente','Domínio','Grupo','Versão do agente','Plataforma','Última ligação','CPU-2 Número de núcleos','CPU-2 Número de processadores lógicos','Disco-1 Partições','Disco-2 Capacidade', 'Disco-2 Partições', 'Disco-3 Capacidade','Disco-3 Partições','Disco-4 Partições','Versão de especificações de TPM','Disco-4 Capacidade'], axis=1)

    df_descricao = df['Descrição'].str.split('-')

    numero_patrimonio = df_descricao.str.get(0)
    Data_Compra = df_descricao.str.get(1)
    modelo_monitor = df_descricao.str.get(2)
    numero_patrimonio_monitor = df_descricao.str.get(3)
    data_compra_monitor = df_descricao.str.get(4)
    windows = df_descricao.str.get(5)

    df['Número patrimônio'] = numero_patrimonio
    df['Data compra desktop'] = Data_Compra
    df['Modelo monitor'] = modelo_monitor
    df['Número patrimônio monitor'] = numero_patrimonio_monitor
    df['Data compra monitor'] = data_compra_monitor
    df['Windows 11'] = windows

    df = df.drop('Descrição', axis=1)

    df = df[['Tipo de computador','Computador', 'Endereço IP', 'Sistema', 'Número patrimônio','Data compra desktop', 'Modelo monitor', 'Número patrimônio monitor','Data compra monitor', 'Sistema operativo',  'Windows 11', 'CPU-1', 'CPU-1 Número de núcleos',
        'CPU-1 Número de processadores lógicos', 'CPU-2', 'Memória',
        'Disco-1 Capacidade', 'Número de série BIOS']]

    df = df.rename(columns={'Sistema operativo': 'Sistema operacional', 'Disco-1 Capacidade': 'Disco-1 capacidade'})

    df["Número patrimônio"] = df["Número patrimônio"].str.replace('"', '')
    df["Windows 11"] = df["Windows 11"].str.replace('"', '')
    df = df.sort_values("Computador")

    df.to_excel(relatorio_gerado, index=False)
    print('Relatório gerado!')
    return
    