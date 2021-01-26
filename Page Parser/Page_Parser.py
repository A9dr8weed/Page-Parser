import requests
from bs4 import BeautifulSoup
import csv

def getHtml(url):
    r = requests.get(url)
    r.encoding = 'utf8'

    return r.text

def csvSave(data):
    with open("C://Users//Andrew//Desktop//data.csv", 'w', newline = '') as file:
        writer = csv.writer(file)
        writer.writerow((data['head'], data['link']))

def getData(html):
    soup = BeautifulSoup(html, 'lxml')
    head = soup.find('section', class_='content content_type_catalog').find_all('a', class_="goods-tile__heading")
    for i in head:
        link = i.get('href')
        heads = i.find('span').get_text()
        data = {'head': heads, 'link': link}

        csvSave(data)

def main():
    data = getData(getHtml('https://rozetka.com.ua/ua/notebooks/c80004/'))

if __name__ == "__main__":
    main()