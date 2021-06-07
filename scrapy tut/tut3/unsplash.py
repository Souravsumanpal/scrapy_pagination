import requests
import os



class Unsplash:
    def __init__(self, search_term, per_page=20, quality="thumb"):
        self.search_term = search_term
        self.per_page = per_page
        self.page = 0
        self.quality = quality
        self.headers = {
            "Accept" :	"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding" :	"gzip, deflate, br",
            "Accept-Language" :	"en-US,en;q=0.5",
            "Host" :	"unsplash.com",	
            "User-Agent" :	"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0"
        }

    def set_url(self):
        return f"https://unsplash.com/napi/search?query={self.search_term}&per_page={self.per_page}&xp={self.page}" 

    def make_request(self):
        url = self.set_url() 
        return requests.request('GET', url, headers=self.headers) 

    def get_data(self):
        self.data = self.make_request().json()

    def save_path(self,name):
        download_dir = "unsplash"
        if not os.path.exists(download_dir):
            os.mkdir(download_dir)
        return f"{os.path.join(os.path.realpath(os.getcwd()),download_dir,name)}.jpg"

    def download(self,url,name):
        filepath = self.save_path(name)
        with open(filepath,"wb") as f:
            f.write(requests.request("GET",url,headers=self.headers).content)

    def scrapper(self,pages):
        for page in range(0,pages+1):
            self.make_request()
            self.get_data()
            for item in self.data['collections']['results']:
                name = item['id']
                url = item['cover_photo']['urls'][self.quality]
                self.download(url,name)
               



scrapper = Unsplash("cars")
scrapper.scrapper(1)















# r = requests.get(url)
# data = r.json()

# for item in data['collections']['results']:
#     name = item['id']
#     url = item['cover_photo']['urls']['thumb']
#     with open(name+'.jpg','wb') as f:
#         f.write(requests.get(url).content)
