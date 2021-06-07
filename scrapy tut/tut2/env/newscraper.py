# from requests_html import HTMLSession
# from requests.sessions import session


# session = HTMLSession()
# url = 'https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN%3Aen'

# r = session.get(url)

# r.html.render(sleep=1, scrolldown=3)

# articles = r.html.find('article')

# newslist = []

# for item in articles:
#     try:
#         newsitem = item.find('h3', first=True)
#         newsarticles = {
#         'title' : newsitem.text,
#         'link' : newsitem.absolute_links
#         }
#         newslist.append(newsarticles)    
        
#     except:
#         pass    

# print(newslist[0])    