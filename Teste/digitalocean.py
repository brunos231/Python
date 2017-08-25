import lxml
from lxml import html
import requests
import pdb

#[0].text_content()

url = "https://www.vultr.com/pricing/"
pagina = requests.get(url)
conteudo = pagina.content

root = lxml.html.fromstring(conteudo)
valor = root.xpath("/html/body/div[1]/div[3]/div/div[2]/div")

for x in valor:
