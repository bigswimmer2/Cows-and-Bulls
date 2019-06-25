import requests
from bs4 import BeautifulSoup
import tkinter

url = 'http://www.nytimes.com'
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html, 'html.parser')
print(soup.find_all(class_='article'))

root = tkinter.Tk()

root.mainloop()

