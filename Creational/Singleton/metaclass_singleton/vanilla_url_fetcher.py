import requests


class UrlFetcher:
    def __init__(self):
        self.urls = []
        
    def fetch(self,url):
        resp  = requests.get(url)
        if resp.status_code == 200:
            self.urls.append(url)


if __name__ == '__main__':
    print(UrlFetcher() is UrlFetcher())
    uf = UrlFetcher()
    uf.fetch("http://www.google.com")
    uf.fetch("http://www.something.com")
    print(uf.urls)

