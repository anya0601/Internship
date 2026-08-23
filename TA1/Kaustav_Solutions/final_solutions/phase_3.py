import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/catalogue/page-1.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find first book title
book = soup.find('article', class_='product_pod')
title = book.h3.a['title']
price = book.find('p', class_='price_color').text
print(f"Sample: {title} - {price}")