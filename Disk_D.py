import requests
import bs4 import BeautifulSoup

url = ''

res = requests.get(url)
soup = Beautiful(res.request, 'html.parser')
links = soup.find('div',attrs = {'id' : 'comic-area'})

for link in links.find_all('img'):
	print(link.get('src'))
