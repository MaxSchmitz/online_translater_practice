import requests
import re
from bs4 import BeautifulSoup

key_word = input()
url = input()

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
# Find the FIRST occurrence of the key word in a paragraph
print(soup.find(string=re.compile(key_word)))


# first_word = input()
# url = input()
# response = requests.get(url)
# soup = BeautifulSoup(response.content, "html.parser")
# paragraphs = soup.find_all("p")
# for p in paragraphs:
#     text = p.text.strip()
#     if first_word in text:
#         print(text)
#         break