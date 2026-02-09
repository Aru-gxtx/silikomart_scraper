import requests
from bs4 import BeautifulSoup

baseurl = 'https://www.silikomart.com/en/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 OPR/126.0.0.0'
}

r = requests.get('https://www.silikomart.com/en/professional/pasticceria/anelli-microforati)', headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

productlist = soup.find_all('div', class_='product name product-item-name')
print(productlist)