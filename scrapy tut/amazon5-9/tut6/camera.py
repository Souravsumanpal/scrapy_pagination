from requests_html import HTMLSession
import csv
import datetime
import sqlite3

conn = sqlite3.connect('amztracker.db')
c = conn.cursor()
# c.execute('''CREATE TABLE prices(date DATE, asin TEXT, price FLOAT, title TEXT)''')


s = HTMLSession()

asins = []

with open('asins.csv','r') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        asins.append(row[0])

print(asins)        


for asin in asins:
    r = s.get(f'https://www.amazon.com/dp/{asin}')

    r.html.render(sleep=20)  
    try: 
        price = r.html.find('#priceblock_saleprice')[0].text.replace('$','').replace(',','').strip()  
    except:
        price = r.html.find('#price_inside_buybox')[0].text.replace('$','').replace(',','').strip()   
    title = r.html.find('#productTitle')[0].text.strip()
    asin = asin
    date = datetime.datetime.today()
    c.execute('''INSERT INTO prices VALUES(?,?,?,?)''', (date, asin, price, title))
    print(f'Added data for {asin},{price}')

conn.commit()  
print('Committed new entry to database')  
 