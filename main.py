

import requests
from bs4 import BeautifulSoup
from lxml import html
from logic import APP
from openpyxl import Workbook



HOST = 'https://coinmarketcap.com/'
URL = 'https://coinmarketcap.com/ru/'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}

respon = requests.get(URL).text

soup =  BeautifulSoup(respon, 'lxml')

lists = []

for link in soup.find('table').find_all('a',class_='cmc-link'):
    d = link.get('href')
    if len(d.split('/')) >=6:
        continue
    elif d in lists:
        continue
    else:
        lists.append(d)

a = APP(lists,HOST).appen()
nam= 1

  # создаем новый excel-файл
wb = Workbook()
    # добавляем новый лист
wb.create_sheet(title='Первый лист', index=0)
    # получаем лист, с которым будем работать
sheet = wb['Первый лист']

for link in a:
    print(nam)
    nam+=1
    spon = BeautifulSoup(requests.get(link).text , 'lxml')
    name = spon.find('h2', class_='sc-1q9q90x-0 iYFMbU h1___3QSYG').text
    praise = spon.find('div',class_='priceValue___11gHJ').text
    vale = spon.find('div',class_='statsValue___2iaoZ').text

    sheet.append([f'{name}', f'{praise}', f'{vale}'])
wb.save('example.xlsx')

#
#
#
# rez=[]
# volem = 0
#
# # for block in reg.xpath("//div[@class='sc-16r8icm-0 bjdvWe']"):
# #     name = block.xpath("//p[@class='sc-1eb5slv-0 iJjGCS']")[volem].text
# #     volem = volem + 1
# #     rez.append( {'name' : name})
#
#
#
# def pars (what,where,who = str(name)):
#     for block in reg.xpath(what):
#         who = block.xpath(where)[volem].text
#         volem = volem +1
#         rez .append({f'{who}':who})
#
# pars("//div[@class='sc-16r8icm-0 bjdvWe']","//p[@class='sc-1eb5slv-0 iJjGCS']")
# print(rez)
# # def get_html(url, params=''):
# #     r=requests.get(url,headers=HEADERS,params=params)
# #     return r
# #
# # def get_content(html):
# #
#
#
#
#
#
#
#
# #
# #
# # def get_content(html):
# #     soup = BeautifulSoup(html, 'html.parser')
# #     items = soup.find_all('tbody')
# #     curency = []
# #     print(items)
# #     iterashon = 0
# #     while iterashon <= 10:
# #         items
# #         name = item.find('tr').find('p',class_='coin-item-symbol').get_text()
# #         vale = item.find ( 'tr' ).find ( 'div' , class_='price___3rj7O' ).get_text()
# #         icon = item.find ( 'tr' ).find ( 'img',class_='coin-logo' ).get('src')
# #         curency.append(
# #             {
# #                 'name':name,'vale':vale,'icon':icon,
# #             })
# #         iterashon = iterashon + 1
# #         print(curency)
# # html = get_html(URL)
# # print(get_content(html.text))
# #
# # def parser():
# #     PAGENATION = input('Сколько валют запарсить? ')
# #     PAGENATION = int(PAGENATION.strip())
# #     html = get_html(URL)
# #     if html.status_code == 200:
# #         curency = []
# #         for curens in range(1,PAGENATION):
# #             print(f'Парсим крипту: {curens}')
# #             html = get_html(URL,params={'curens': curens})
# #             curency.extend(get_content(html.text))
# #         print(curency)
# #     else:
# #         print('Error - сайт не отвечает подключись к интернету ')
# #
# # parser()
# #
#
#
#
#
#


#
