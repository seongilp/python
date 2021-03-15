from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import os
headers = {'User-Agent' : 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_1_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.1 Mobile/15E148 Safari/604.1'}
req = requests.get('https://m.dcinside.com/board/bravegirls0409?recommend=1', headers=headers)
html = req.text
soup = BeautifulSoup(html, 'html.parser')
newPost = soup.find("div", {"class" : "gall-detail-lnktb"})
newPostTitle = newPost.find("span", {"class" : "subjectin"}).text


from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import os
headers = {'User-Agent' : 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_1_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.1 Mobile/15E148 Safari/604.1'}


req = requests.get('https://finance.naver.com/item/sise_day.nhn?code=055550&page=1', headers=headers)


html = req.text
soup = BeautifulSoup(html, 'html.parser')


table = pd.read_html(html)
table[0].dropna()
