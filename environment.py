import os
from dotenv import load_dotenv
from time import sleep


class Timer:

    def __init__(self) -> None:
        load_dotenv()

        self.ENVIROMENT = os.getenv("ENVIROMENT")

        # default
        self._sm = 10
        self._lg = 10

        if self.ENVIROMENT == "development":
            self._sm = 3
            self._lg = 8

        if self.ENVIROMENT == "production":
            self._sm = 15
            self._lg = 30
    
    
    def small(self):
        sleep(self._sm)
            
    def long(self):
        sleep(self._lg)

    def any(self, number):
        sleep(number)