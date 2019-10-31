import requests
import json
import telebot
from bs4 import BeautifulSoup

BASE_URL = 'https://www.ucrf.gov.ua/ua/services/centralized-registries'
bot = telebot.TeleBot('986188148:AAEYGL6T-sihM7SOiNum9Vv5jJBQFJ50BnQ')

def get_html(BASE_URL):
    response = requests.get(BASE_URL, verify=False)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        page = soup.find('ul', class_='pagination' )
        end_page = list(page)
        page_number = end_page[23].text
        EndPageHref = ('https://www.ucrf.gov.ua/ua/services/centralized-registries?permission_num=&region=&technology=&search=&per_page=200&page='+page_number)
        print(EndPageHref)
        read_page_txt = open('page.txt', "r")
        page_txt = json.load(read_page_txt)
    else:
        print('Ошибка')
    if page_txt != page_number:
        bot.send_message(-1001168783131,'Реестр УДЦР обновлен')
        print('Сайт УДЦР обновленно')
        fullpage = open('page.txt', "w")
        json.dump(page_number, fullpage)
    else:
        bot.send_message(-1001168783131, 'Обновлений нету')
        print('Обновлений нету')


    #for end_page in page.find_all('li', limit=2)[1]):
     #   end_page_a = end_page.find_all('a')
      #  print(end_page_a)


# def parce(html):
#  soup = BeautifulSoup(html, 'lxml')
# elm = soup.find('div', class_='top-map-nav')
# print(elm.prettify())


if __name__ == '__main__':
    get_html(BASE_URL)
