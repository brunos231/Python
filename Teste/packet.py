import lxml
from lxml import html
import requests
import pdb

#[0].text_content()

lista = []

#Faz o Parsing da página
url = "https://www.packet.net/bare-metal/"
pagina = requests.get(url)
conteudo = pagina.content

root = lxml.html.fromstring(conteudo)

#Xpath que contem as div's com informações
elementos = root.xpath('//*[@id="pricing-items"]/article')

# Pega os dados com a mesma estrutura
for info in elementos:
    inf_ext = '' #Grava as informações extras de alguns elementos

    nome = str(info[0][0].text_content()).strip()
    vlr_hr = str(info[0][1][1].text_content())
    vlr_m = str(info[0][3][1].text_content())
    nucleo_cpu = str(info[1][0][0][0].text_content())
    memoria = str(info[1][0][1].text_content())
    sdd = str(info[1][0][2][0].text_content())
    band = str(info[1][0][3].text_content())

    #Faz a organização dos elementos em posições diferentes
    if info == elementos[2]:
        memoria = str(info[1][0][2].text_content())
        inf_ext = str(info[1][0][1].text_content())

    elif info == elementos[3] or info == elementos[5]:
        band = str(info[1][0][4].text_content())
        inf_ext = str(info[1][0][3].text_content())

    elif info == elementos[6]:
        sdd = str(info[1][0][3].text_content())
        inf_ext = str(info[1][0][2][0].text_content())

    #Posiciona todos os valores em uma lista principal
    lista.append([nome, vlr_hr, vlr_m, nucleo_cpu, memoria, sdd, band, inf_ext])

#Apaga a lacuna em branco dos elementos sem info extra
del(lista[0][-1], lista[1][-1], lista[4][-1])

for x in lista:
    print(x)
