import lxml
from lxml import html
import requests
import pdb

#[0].text_content()

lista = []

#Faz o Parsing da página
url = "https://www.digitalocean.com/pricing/#droplet"
pagina = requests.get(url)
conteudo = pagina.content

root = lxml.html.fromstring(conteudo)

#Xpath que contem as div's com informações
elementos = root.xpath("/html/body/section/div[2]/section[1]/div[2]/div/div/div")


#Nome do produto/Valor por mês
for vlr in elementos:
    vlr_m = str(vlr[0][0][1].text_content()).strip()

    #Valor por Hora
    for vlr in elementos:
        vlr_hr = str(vlr[0][1].text_content()).strip()

        #Memoria - nº PC´s - Sdds - Transferencia
        for info in elementos:
            memoria = str(info[1][0][0].text_content()).strip()
            pcs = str(info[1][1][0].text_content()).strip()
            sdd = str(info[1][2][0].text_content()).strip()
            band = str(info[1][3][0].text_content()).strip()

    else:
        #Adiciona os valores em sub-listas
        lista.append([vlr_m, vlr_hr, memoria, pcs, sdd, band])

for x in lista:
    print(x)
