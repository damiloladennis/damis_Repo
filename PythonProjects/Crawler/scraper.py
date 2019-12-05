import requests
from bs4 import BeautifulSoup
url = 'http://stash.compjour.org/samples/webpages/whitehouse-press-briefings-page-50.html'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'lxml')

urls = []
for h in soup.find_all('h3'):
    a = h.find('a')
    urls.append(a.attrs['href'])
print(urls)





