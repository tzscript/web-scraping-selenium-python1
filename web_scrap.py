from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as soup
driver = webdriver.Chrome()
import requests
from bs4 import BeautifulSoup as soup

page = requests.get('http://dataquestio.github.io/web-scraping-pages/simple.html')

result = soup(page.content , 'html.parser')

# print(result.prettify())
# print(type(result))

print(result.find_all('p',class_=’outer-text’))
