
import pandas as pd
import requests
from bs4 import BeautifulSoup
from lxml import html
import file.logic as fl
from openpyxl import Workbook
from multiprocessing import Pool
import csv
import random
from fake_useragent import UserAgent
import os.path

ua = UserAgent()
HOST = 'https://coinmarketcap.com/'
URL = 'https://coinmarketcap.com/ru/'
HEADERS = {'User-Agent': ua.path}

nam = 10
x = 0
writers=()

class Get_Link():
    def __init__(self):
        respon = requests.get(URL, headers=HEADERS)
        self.soup = BeautifulSoup(respon.text, 'lxml')
        self.lists = []

    def link_lin(self):
        # возвращает список сылок на каждую валюту с первой страници
        if os.path.exists('link_lin.csv') == False:
            for link in self.soup.find('table').find_all('a',class_='cmc-link'):
                d = link.get('href')
                self.lists.append(d)

            list_s=fl.APP(self.lists, HOST).app_en()
            ls = pd.DataFrame(list_s)
            ls.to_csv('link_lin.csv', index=False,header=False)

        with open('link_lin.csv',newline='') as op:
            reading = csv.reader(op)
            re_ad = list(reading)
        self.lists = []
        for i in re_ad:
            self.lists.append(i[0])
        return self.lists




ls = Get_Link().link_lin()

def data (link):
    spon = BeautifulSoup(requests.get(link).text, 'lxml')
    inde_x = spon.find('small', class_='nameSymbol___1arQV').text
    name = spon.find('span', class_='sc-1eb5slv-0 sc-1308828-0 deLPiG').text
    praise = spon.find('div', class_='priceValue___11gHJ').text
    vale = spon.find('div', class_='statsValue___2iaoZ').text
    print(inde_x,name,praise,vale)
    return inde_x,name,praise,vale

def write (link):

    date_list= []
    inde_x,name,praise,vale =data(link)
    date_list.append((inde_x,name,praise,vale))                                     #{'name': [name],'praise': [praise],'vale':[vale]}
    return date_list



if __name__=='__main__':
    with Pool(processes=nam)as pool:
        w = pool.map (write,ls)

    fl.un_pak(w)

    print('finish')
#     # with open('cap.csv') as f:
#     #     print(f.read())
