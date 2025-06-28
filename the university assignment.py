#import rotatescreen
from PIL import Image #--> pillow
import pyzbar
from bs4 import BeautifulSoup
import qrcode
import schedule
#import pyudev
import watchdog
import pyautogui
# from usb import core
# from usb import util
import platform
import requests

import psutil
import cv2
from flask import Flask
from Crypto.Cipher import AES
import threading
from time import asctime
class bank():
    def __init__(self,name, amount,date):
        self.__name=name
        self.__amount=amount
        self.__date=date
    def get_payment(self):
        return self.__amount
    def register(self):
        self.clients={
            'name':self.__name,
            'amount':self.__amount,
            'date':self.__date,
        }
class creditCard(bank):
    def __init__(self, name, amount, date,card_number,card_expiration):
        super().__init__(name, amount, date)
        self.__card_number=card_number
        self.__card_expiration=card_expiration
    def process_payment(self):
        print(f"you paid {super().get_payment()} with your credit card number {self.__card_number}")
class cashcard(bank):
    def __init__(self, name, amount, date,currency):
        super().__init__(name, amount, date)
        self.currency=currency
    def process_payment(self):
        print(f"you paid {super().get_payment()} in cash, currency[{self.currency}]")
class payment_system:
    def process_all(self,payments):
        for payment in payments:
            payment.process_payment()
payment=[creditCard(name="Basem",amount=200,date=asctime(),card_expiration='2025/2/4',card_number=1),
         cashcard(name="Yousif",date='2026.7.7',amount=300,currency="Yemeni")]
payment_system().process_all(payment)
