from binance.client import Client
import time
import threading
import os
import ast
import datetime
import smtplib
import random
import keys
from binance.exceptions import BinanceAPIException, BinanceWithdrawException
from binance.enums import *


client = Client(api_key=api_pub, api_secret=api_sec)

time_res = client.get_server_time()

coin_list = ['BNBBTC']




prices = client.get_all_tickers()
for item in prices:
    #print (item)
    if [coin for coin in coin_list if coin==item['symbol'] in coin_list]:
        order_coin(item)