import requests
from bs4 import BeautifulSoup
import tkinter

array =[]
url = 'http://www.nytimes.com'
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html, 'html.parser')

for f in soup.find_all('h2'):
    array.append(str(f))

for f in array:
    print(f + '\n')