import requests
from bs4 import BeautifulSoup

html = '';
url = 'https://www.ourinhos.sp.gov.br/portal/noticias';

req = requests.get(url)
html = req.text
soup = BeautifulSoup(html, 'html.parser')

for kw in soup.find_all('div', attrs={"class": "ntc_titulo_noticia sw_lato_black"}):
    print(kw.text)