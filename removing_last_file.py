import os
def excluir_ultimo_relatorio(path, file):
    arquivo = path + file

    if os.path.exists(arquivo):
        os.remove(arquivo)
        print(f'Relatório antigo removido "{file}". Prosseguindo...')
        return
    else:
        print('Não existe um relatório antigo. Prosseguindo...')
        return