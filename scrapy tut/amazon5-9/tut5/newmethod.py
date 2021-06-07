from requests_html import HTMLSession
# using requests_html

urllist = [
    'https://www.amazon.com/VIZIO-Class-31-5-Diag-Smart/dp/B089JXY4SP/ref=sr_1_1?currency=INR&dchild=1&keywords=tv&qid=1621926279&s=computers-intl-ship&sr=1-1',
    'https://www.amazon.com/gp/slredirect/picassoRedirect.html/ref=pa_sp_mtf_computers-intl-ship_sr_pg1_1?ie=UTF8&adId=A01953861115659ZDUFJQ&url=%2FAll-New-Toshiba-32LF221U21-32-inch-Smart%2Fdp%2FB0872FYTWS%2Fref%3Dsr_1_5_sspa%3Fcurrency%3DINR%26dchild%3D1%26keywords%3Dtv%26qid%3D1621926279%26s%3Dcomputers-intl-ship%26sr%3D1-5-spons%26psc%3D1&qualifier=1621926279&id=1169926541682321&widgetName=sp_mtf',
    'https://www.amazon.com/gp/slredirect/picassoRedirect.html/ref=pa_sp_mtf_computers-intl-ship_sr_pg1_1?ie=UTF8&adId=A08442093AKAYDKQ3JXD3&url=%2FAll-New-Insignia-NS-39DF310NA21-39-inch-Smart%2Fdp%2FB0875M44Y5%2Fref%3Dsr_1_10_sspa%3Fcurrency%3DINR%26dchild%3D1%26keywords%3Dtv%26qid%3D1621926279%26s%3Dcomputers-intl-ship%26sr%3D1-10-spons%26psc%3D1&qualifier=1621926279&id=1169926541682321&widgetName=sp_mtf'
]

def getPrice(url):
    s = HTMLSession()
    r = s.get(url)
    r.html.render(sleep=1)

    product = {
        'title' : r.html.xpath('//*[@id="productTitle"]', first=True).text,
        'price' : r.html.xpath('//*[@id="priceblock_ourprice"]', first=True).text
    }

    print(product)
    return product


tvprices = []
for url in urllist:
    tvprices.append(getPrice(url))

print(len(tvprices))    