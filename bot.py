from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui as auto
from dotenv import load_dotenv
from environment import Timer
import os



class Bot:
    def __init__(self) -> None:     
        
        load_dotenv()


        self.tm = Timer()

        self.EMAIL = os.getenv("EMAIL_PD")
        self.PASSWORD = os.getenv("PASSWORD_PD")
        self.SITE_LINK = os.getenv("LINK_SITE_PD")

        
        self.SITE_MAPA = {
            "buttons": {
                'email'  : {'xpath' : '/html/body/article/main/div/section/form/section/div/input[1]'},
                'senha'  : {'xpath' : '/html/body/article/main/div/section/form/section/div/input[2]'},
                'captcha': {'xpath' : '/html/body/div[2]/div[3]/div[1]/div/div/span/div[1]'},
                'login'  : {'xpath' : '/html/body/article/main/div/section/form/section/div/input[4]'},
                'endpoint':{'xpath' : '/html/body/app-root/ui-view/app-services-view/div/div[1]/div/app-service-card[1]/div/mat-card/mat-card-content'},
                'hardware':{'xpath' : '/html/body/article/div/aside/div[3]/div/div[7]/div[2]/div/div[1]/a/span'},
                'exportar':{
                    'xpath1' : '/html/body/article/div/section/div[1]/div/div[1]/div[1]/form/div[3]/div/div/div[3]/a/i',
                    'xpath2' : '/html/body/article/div/section/div[1]/div/div[1]/div[1]/form/div[2]/div/div/div[3]/a'
                    }
            }
        }

        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36"  
       
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument(f'--user-agent={user_agent}')

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()



    def entrar_site(self):
        self.tm.small()
        self.driver.get(self.SITE_LINK)
        self.tm.small()

    def logar(self):
        self.driver.find_element(By.XPATH ,self.SITE_MAPA['buttons']['email']['xpath']).send_keys(self.EMAIL)
        self.tm.small()
        self.driver.find_element(By.XPATH ,self.SITE_MAPA['buttons']['senha']['xpath']).send_keys(self.PASSWORD)
        self.tm.small()

        try:
            auto.locateCenterOnScreen('captcha.PNG', confidence=0.8)

            self.driver.find_element(By.XPATH ,self.SITE_MAPA['buttons']['captcha']['xpath']).click()
            self.tm.small()

            self.driver.find_element(By.XPATH ,self.SITE_MAPA['buttons']['login']['xpath']).click()
            self.tm.small()
        except:

            self.driver.find_element(By.XPATH ,self.SITE_MAPA['buttons']['login']['xpath']).click()
            self.tm.small()

    def exportar(self):
        self.driver.find_element(By.XPATH ,self.SITE_MAPA['buttons']['exportar']['xpath2']).click()
        self.tm.small()
        self.driver.quit()




