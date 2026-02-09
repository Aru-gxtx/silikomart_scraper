import requests
from bs4 import BeautifulSoup

baseurl = 'https://www.meilleurduchef.com/en/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 OPR/126.0.0.0'
}

r = requests.get('https://www.meilleurduchef.com/en/shop/brands/silikomart.html', headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

productlist = soup.find_all('div', class_='cell produit visible')

productlinks = []

for item in productlist:
    for link in item.find_all('a', href=True):
        productlinks.append(baseurl + link['href'])

"""
for link in productlinks:
    print(link)
"""

testlink = 'https://www.meilleurduchef.com/en/shop/baking-supplies/cake-mould/shaped-moulds/sil-silicone-mould-kit-game-6-round.html'

r = requests.get(testlink, headers=headers)

soup = BeautifulSoup(r.content, 'lxml')

button = soup.find('div', class_='button img current')

if button:
    img = button.find('img')
    if img and img.has_attr('alt'):
        name = img['alt'].split(' - ')[0]
        print(name)

availability = soup.find('div', class_='disponibilite')

if availability:
    stock = availability.find('span', class_='en-stock')
    if stock:
        print(stock.get_text(strip=True))

reference = soup.find('div', class_='reference')

if reference:
    value = reference.find('span', class_='value')
    if value:
        print("Manufacturer ID: " + value.get_text(strip=True))

brand_div = soup.find('div', class_='marque')

if brand_div:
    print(f"Brand: {brand_div.get_text(strip=True)}")

