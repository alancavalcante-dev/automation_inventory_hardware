from bot import Bot
from file_exported import formatar_tabela
from time import sleep
from import_google_drive import BotGoogleDrive
from removing_last_file import excluir_ultimo_relatorio


PATH_FILE_EXPORTED = r'C:\\Users\\admin.alan\\Downloads\\'
PATH_NEW_FILE = r'C:\\Users\\admin.alan\\Downloads\\'
NEW_NAME_FILE = 'relatorio.xlsx'


# Exportando arquivo do panda
excluir_ultimo_relatorio(PATH_NEW_FILE, NEW_NAME_FILE)
sleep(3)

bot = Bot()
bot.entrar_site()
bot.logar()
bot.exportar()
print('Exportado com sucesso!\n')


# formatar_tabela
formatar_tabela(PATH_FILE_EXPORTED, PATH_NEW_FILE, NEW_NAME_FILE)
sleep(12)



# Importar no google drive
botGD = BotGoogleDrive()
botGD.copiar_e_fechar(PATH_NEW_FILE)
botGD.entrar_site()
botGD.importar()
print('Importado para Google Drive')


shoot_email = botGD.disparar_email('suporteti@fusp.org.br',
                    'Inventário de Hardware atualizado  com sucesso!',
                    'Olá, <br><br>Inventário de Hardware atualizado e importado para o Google Drive.<br>Clique no link ao lado para ser direcionado para a página: https://docs.google.com/spreadsheets/d/17XBjcZF2eCStKIsaS3HqL1ySbGGn1_Kg/edit#gid=825153193 <br><br>Até mês que vem!')

if shoot_email:
    print('Email enviado')
else:
    print('Não foi possível disparar o email.')
    

sleep(2)
print('Automatização concluída')