# from selenium import webdriver
from bs4 import BeautifulSoup
from openpyxl import Workbook

import pandas as pd
from pathlib import Path
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# import time
#
# BASE_DIR = Path(__file__).resolve().parent
# chrome_path = f'{BASE_DIR}/chromedriver.exe'
# chrome_options = Options()
# chrome_service = Service(executable_path=chrome_path)
# driver = webdriver.Chrome(options=chrome_options, service=chrome_service)
# driver.maximize_window()
# products=[]
# prices=[]
# ratings=[]
# driver.get("https://www.flipkart.com/6bo/b5g/~cs-sjfhc23o76/pr?sid=6bo,b5g&collection-tab-name=Top+Deals&otracker=hp_banner_3_4.bannerX3.BANNER_PH0FVCVGYSYA&fm=neo%2Fmerchandising&iid=M_c73c33fc-50e4-4d43-96ce-afba0eced98d_4.PH0FVCVGYSYA&ppt=hp&ppn=homepage&ssid=c5kkvxgnq80000001665122727407")
# content = driver.page_source
# soup = BeautifulSoup(content)
# for a in soup.findAll('a', href=True, attrs={'class': '_1fQZEK'}):
#     name=a.find('div', attrs={'class': '_4rR01T'})
#     price=a.find('div', attrs={'class': '_3tbKJL'})
#     rating=a.find('div', attrs={'class': 'gUuXy-'})
#     products.append(name.text)
#     prices.append(price.text)
#     ratings.append(rating.text)
#     df = pd.DataFrame({'Product Name': products, 'Price': prices, 'Rating': ratings})
#     df.to_csv('products.csv', index=False, encoding='utf-8')

import requests
import pandas as pd
products=[]
prices=[]
ratings=[]
url = "https://www.flipkart.com/6bo/b5g/~cs-sjfhc23o76/pr?sid=6bo,b5g&collection-tab-name=Top+Deals&otracker=hp_banner_3_4.bannerX3.BANNER_PH0FVCVGYSYA&fm=neo%2Fmerchandising&iid=M_c73c33fc-50e4-4d43-96ce-afba0eced98d_4.PH0FVCVGYSYA&ppt=hp&ppn=homepage&ssid=c5kkvxgnq80000001665122727407"
html = requests.get(url)

soup = BeautifulSoup(html.text, 'html.parser')
for a in soup.findAll('a', href=True, attrs={'class': '_1fQZEK'}):
    name=a.find('div', attrs={'class': '_4rR01T'})
    price = a.find('div', attrs={'class': '_3tbKJL'})
    rating=a.find('div', attrs={'class': 'gUuXy-'})
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text)
df = pd.DataFrame({'Product Name': products, 'Price': prices, 'Rating': ratings})
df.to_csv('products.csv', index=False, encoding='utf-8')
df.to_excel('products.xlsx', sheet_name="Sheet1")

print(df)