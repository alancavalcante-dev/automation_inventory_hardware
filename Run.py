from bot import Bot
from file_exported import formatar_tabela
from environment import Timer
from import_google_drive import BotGoogleDrive
from removing_last_file import excluir_ultimo_relatorio
import sys
from dotenv import load_dotenv
import os

tm = Timer()

load_dotenv()

tm.long()




NEW_NAME_FILE = 'relatorio.xlsx'

ENVIROMENT = os.getenv("ENVIROMENT")

PATH_FILE_EXPORTED = os.getenv("PATH_FILE_EXPORTED").replace('/', r'\\')

PATH_NEW_FILE = PATH_FILE_EXPORTED


MSG_EMAIL_TO = os.getenv('MSG_EMAIL_TO')
MSG_TITLE = os.getenv('MSG_TITLE')
MSG_BODY = os.getenv('MSG_BODY')



# Exportando arquivo do panda
excluir_ultimo_relatorio(PATH_FILE_EXPORTED, NEW_NAME_FILE)
tm.long()

bot = Bot()
bot.entrar_site()
bot.logar()
bot.exportar()
print('Exportado com sucesso!\n')


# formatar_tabela
formatar_tabela(PATH_FILE_EXPORTED, PATH_NEW_FILE, NEW_NAME_FILE)
tm.long()



# Importar no google drive
botGD = BotGoogleDrive()
botGD.copiar_e_fechar(PATH_NEW_FILE)
botGD.entrar_site()
botGD.importar()
print('Importado para Google Drive')


shoot_email = botGD.disparar_email(
    MSG_EMAIL_TO,
    MSG_TITLE,
    MSG_BODY,
)

if shoot_email:
    print('Email enviado')
else:
    print('Não foi possível disparar o email.')

print('Automatização concluída')

sys.exit()