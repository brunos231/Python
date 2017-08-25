"""Tentando fazer Crawler mais uma vez"""

import urllib.request

content = urllib.request.urlopen("https://www.climatempo.com.br/previsao-do-tempo/cidade/558/saopaulo-sp").read()
content = str(content)
find = 'xima">'
posicao = int(content.index(find) + len(find))
maxima = content[posicao:posicao + 2]

print("Temperatura máxima: {}°".format(maxima))

find = 'nima">'
posicao = int(content.index(find) + len(find))
minima = content[posicao:posicao + 2]

print("Temperatura minima: {}°".format(minima))



