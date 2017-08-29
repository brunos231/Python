import lxml
from lxml import html
import requests
import sqlite3

#Cria os elementos de conexão
conn = sqlite3.connect('digitalocean')
cursor = conn.cursor()

#Cria a tabela onde serão salvos os dados
cursor.execute("""
CREATE TABLE IF NOT EXISTS box(
    id integer primary key autoincrement,
    vlr_hr varchar(20),
    vlr_m varchar(20),
    memoria varchar(20),
    n_pc varchar(20),
    storage varchar(20),
    transfer varchar(20)
) 
""")

lista = []

#Faz o Parsing da página
url = "https://www.digitalocean.com/pricing/#droplet"
pagina = requests.get(url)
conteudo = pagina.content

root = lxml.html.fromstring(conteudo)

#Xpath que contem as div's com informações
elementos = root.xpath("/html/body/section/div[2]/section[1]/div[2]/div/div/div")

# Faz a coleta das informações
for info in elementos:
    vlr_m = str(info[0][0][1].text_content()).strip()
    vlr_hr = str(info[0][1].text_content()).strip()
    memoria = str(info[1][0][0].text_content()).strip()
    pcs = str(info[1][1][0].text_content()).strip()
    sdd = str(info[1][2][0].text_content()).strip()
    band = str(info[1][3][0].text_content()).strip()

    # Adiciona os valores em sub-listas
    lista.append((vlr_m, vlr_hr, memoria, pcs, sdd, band))

#Insere a lista no Banco de Dados
cursor.executemany("""
    INSERT INTO box(vlr_m, vlr_hr, memoria, n_pc, storage, transfer)
        VALUES (?,?,?,?,?,?)
""", lista)

#Comita os dados na tabela
conn.commit()

#Faz a consulta dos elementos da tabela
cursor.execute("""
SELECT * FROM box
""")

#Atribui a consulta para uma lista
lista1 = cursor.fetchall()

conn.close() #Fecha a conexão com o Banco de Dados

#Mostra os elementos da consulta
for x in lista1:
    print(x)

