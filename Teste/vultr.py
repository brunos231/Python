import lxml
from lxml import html
import requests

#Faz o Parsing da página
url = "https://www.vultr.com/pricing/"
pagina = requests.get(url)
conteudo = pagina.content

root = lxml.html.fromstring(conteudo)

#Xpath que contem as div's com informações
elementos = root.xpath("/html/body/div[1]/div[3]/div/div[2]/div/div")
elementos1 = root.xpath("/html/body/div[1]/div[3]/div/div[3]/div/div")
# **** Não possui elemento global que englobe todos os valores ****

"""Método que pesquisa as posições correspondentes"""
def pesq(xpath):
    lista = []

    #Percorre o site atras das informações, e faz as atribuições
    for y in xpath:
        nome = str(y[0][0][1].text_content())
        vlr_m = str(y[0][0][2].text_content())
        pcs = str(y[0][1][0][0].text_content())
        memoria = str(y[0][1][0][1].text_content())
        transfer = str(y[0][1][0][2].text_content())

        #Coloca os valores dentro de uma lista
        lista.append([nome, vlr_m, pcs, memoria, transfer])

    else:
        return lista
"""----------------------Fim do método-------------------------"""

for x in pesq(elementos):
    print(x)

for x in pesq(elementos1):
    print(x)

