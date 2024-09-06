from selenium import webdriver
from selenium.webdriver.common.by import By
import os, psutil, smtplib, email.message
import pyautogui as auto
from environment import Timer
from dotenv import load_dotenv


class BotGoogleDrive:
    def __init__(self) -> None:     
        self.tm = Timer()

        
        load_dotenv()


        self.EMAIL = os.getenv("EMAIL_GD")
        self.PASSWORD = os.getenv("PASSWORD_GD")
        self.SITE_LINK = os.getenv("LINK_SITE_GD")
        

        self.SITE_MAPA = {
            "buttons": {
                'email'  : {'xpath' : '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input',
                            'xpath2' :'/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div[1]/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input'},

                'seguinte':{'xpath' : '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/span',
                            'xpath2': '/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button'},

                'senha'  : {'xpath' : '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input',
                            'xpath2': '/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input'},

                'acessar':{'xpath' : '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/span',
                           'xpath2': '/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button'}
            }
        }



    def copiar_e_fechar(self, path_file):
        self.tm.small()
        os.chdir(path_file)
        os.system('Start relatorio.xlsx')
        self.tm.long()
        auto.hotkey('ctrl','shiftright','shiftleft','end')
        self.tm.small()
        auto.hotkey('ctrl', 'c')
        self.tm.small()




    def fechar_excel(self):
        try:
            # Iterar sobre todos os processos em execução
            for processo in psutil.process_iter(['pid', 'name']):
                # Verifica se o nome do processo é "EXCEL.EXE"
                if "EXCEL.EXE" in processo.info['name']:
                    try:
                        # Tenta encerrar o processo do Excel
                        psutil.Process(processo.info['pid']).terminate()
                        print("Todas as instâncias do Excel foram encerradas.")
                        break
                    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                        pass
        except Exception as e:
            print(f"Erro: {e}")






    def entrar_site(self):
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36"  
       
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument(f'--user-agent={user_agent}')

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()

        self.tm.small()
        self.driver.get(self.SITE_LINK)
        self.tm.small()

        self.driver.find_element(By.XPATH ,self.SITE_MAPA['buttons']['email']['xpath2']).send_keys(self.EMAIL)
        self.tm.small()
        
        self.driver.find_element(By.XPATH ,self.SITE_MAPA['buttons']['seguinte']['xpath2']).click()
        self.tm.small()

        self.driver.find_element(By.XPATH ,self.SITE_MAPA['buttons']['senha']['xpath2']).send_keys(self.PASSWORD)
        self.tm.small()

        self.driver.find_element(By.XPATH ,self.SITE_MAPA['buttons']['acessar']['xpath2']).click()
        self.tm.small()
        

    def importar(self):
        self.tm.long()
        auto.hotkey('ctrl', 'a')
        self.tm.long()

        auto.press('del')
        self.tm.long()

        auto.hotkey('ctrl', 'v')
        self.tm.long()

        self.driver.close()
        self.tm.small()
        self.fechar_excel()


   

    def disparar_email(self, email_destinatario, titulo, corpo):
        try:
            key = os.getenv("KEY_SHOOT_EMAIL")

            msg = email.message.Message()
            msg['Subject'] = titulo # Título
            msg['From'] = 'guimera.sistem@gmail.com' # Remetente
            msg['To'] = f'{email_destinatario}' # destinatário

            msg.add_header('Content-Type', 'text/html') # Configurações site html
            msg.set_payload(corpo) # Corpo email/descrição

            s = smtplib.SMTP('smtp.gmail.com: 587') # Servidor e porta de acesso ao Gmail
            s.starttls() # Executação da porta e servidor
            # Login Credentials for sending the mail
            s.login(msg['From'], key) # Login da conta: email, e a senha
            s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8')) # Envio da mensagem

            return True
        except:
            return False

