import lxml
from lxml import html
import requests
import pdb

#[0].text_content()

#Faz o Parsing da página
url = "https://www.digitalocean.com/pricing/#droplet"
pagina = requests.get(url)
conteudo = pagina.content

root = lxml.html.fromstring(conteudo)

#Xpath que contem as div's com informações
elementos = root.xpath("/html/body/section/div[2]/section[1]/div[2]/div/div/div")


#Nome do produto/Valor por mês
for vlr in elementos:
    vlr_m = str(vlr[0][0][1].text_content())

    #Valor por Hora
    for vlr in elementos:
        vlr_hr = str(vlr[0][1].text_content())

        #Memoria - nº PC´s - Sdds - Transferencia
        for info in elementos:
            memoria = str(info[1][0][0].text_content())
            pcs = str(info[1][1][0].text_content())
            sdd = str(info[1][2][0].text_content())
            band = str(info[1][3][0].text_content())

            print("Valor p/ mês:", vlr_m)
            print("Valor p/ hra:", vlr_hr.strip())
            print("Memória:", memoria.strip())
            print("PC´s:", pcs.strip())
            print("SDD Disc:", sdd.strip())
            print("Tranferencia:", band.strip())
            print("  ")










