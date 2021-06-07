import requests
from bs4 import BeautifulSoup
import json


mystocks = ['VAST.L','ICON.L','PREM.L','BZT.L']
stockdata = []

def getData(symbol):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
    url = f'https://finance.yahoo.com/quote/{symbol}'

    r = requests.get(url)

    soup = BeautifulSoup(r.text, 'html.parser')
    stock = {
        'symbol': symbol,
        'price' : soup.find('div', {'class':'D(ib) Mend(20px)'}).find_all('span')[0].text,
        'change' : soup.find('div', {'class':'D(ib) Mend(20px)'}).find_all('span')[1].text
    }

    return stock


for item in mystocks:
    stockdata.append(getData(item))
    print('Getting :', item)

with open('Stockdata.json','w') as f:
    json.dump(stockdata,f)      

  


    # price = soup.find('span', {'class':'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text
    # change = soup.find('span', {'class': 'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px)'}).text

    # print(price,change)
