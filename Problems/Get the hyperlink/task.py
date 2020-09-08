import requests

from bs4 import BeautifulSoup

article_index = int(input())-1
url = input()
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
a = soup.find_all('a')
print(a[article_index].get('href'))