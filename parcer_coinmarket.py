import requests
from bs4 import BeautifulSoup
import csv

def csv_writer(data):
    with open('crypto.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(list(data.values()))


def get_html(url):
    response = requests.get(url)
    if response.status_code == requests.codes.ok:
        return response.text
    else:
        raise Exception('Something went wrong')


def common_price(price):
    price = price.replace(',', '')
    price = price.replace('<', '')
    price = price.replace('>', '')
    price = price.replace('-', '')
    price = price.replace('!', '')
    return price

def get_number_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    number_of_pages = soup.find('div', class_='grid').find('div').find('div', class_='sc-4r7b5t-3 bvcQcm').find_all('li')[-2].find('a').text
    return int(number_of_pages)

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    trs = soup.find('tbody').find_all('tr')
    for td in trs:
        if len(td) > 5:
            try:
                name = td.find('p', class_='sc-1eb5slv-0 iworPT').text
            except:
                name = ''
            try:
                symbol = td.find('p', class_='sc-1eb5slv-0 gGIpIK coin-item-symbol').text
            except:
                symbol = ''
            try:
                price = common_price(td.find('div', class_='sc-131di3y-0 cLgOOr').find('span').text)
            except:
                price = ''
        else:
            try:
                name = td.find_all('td')[2].find_all('span')[1].text
            except:
                name = ''
            try:
                symbol = td.find_all('td')[2].find_all('span')[2].text
            except:
                symbol = ''
            try:
                price = common_price(td.find_all('td')[3].find('span').text)
            except:
                price = ''

        data = {
            'name': name,
            'symbol': symbol,
            'price': price
        }

        csv_writer(data)

def main():
    url = 'https://coinmarketcap.com/'
    pages = get_number_pages(get_html(url))

    for i in range(2, pages + 1):
        url = url + f'?page={i}'
        get_data(get_html(url))


if __name__ == '__main__':
    main()
