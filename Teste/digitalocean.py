import lxml
from lxml import html
import requests
import sqlite3
import pdb

#Cria os elementos de conexão
conn = sqlite3.connect('base')
cursor = conn.cursor()

#Cria a tabela onde serão salvos os dados
cursor.execute("""
CREATE TABLE IF NOT EXISTS digitalocean(
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

for idx, dados in enumerate(lista):
    print("Serviço: ", idx)
    print("Valor p/ Mês:  ", "$"+dados[0]+"/m")
    print("Valor p/ Hora: ", dados[1])
    print("Memória:       ", dados[2])
    print("Nº PC´s:       ", dados[3])
    print("Storage:       ", dados[4])
    print("Bandwidth p/ M:", dados[5])
    print("     ---         ---     ")

print("Deseja salvar os dados no Banco?")
resposta = str(input("Sim[S] / Não[N]: ")).lower()

if resposta == 's':
    #Insere a lista no Banco de Dados
    cursor.executemany("""
        INSERT INTO digitalocean(vlr_m, vlr_hr, memoria, n_pc, storage, transfer)
            VALUES (?,?,?,?,?,?)
    """, lista)

    #Comita os dados na tabela
    conn.commit()

    print("Salvo com Sucesso")

    print("Deseja ver os dados salvos?")
    resposta = str(input("Sim[S] / Não[N]: ")).lower()

    cursor.execute("""
        SELECT * FROM digitalocean
        """)

    view = cursor.fetchall()

    print("Dados do Banco de Dados")
    for v in view:
        print("Chave:         ", v[0])
        print("Valor p/ Mês:  ", v[2])
        print("Valor p/ Hora: ", v[1])
        print("Memória:       ", v[3])
        print("Nº PC´s:       ", v[4])
        print("Storage:       ", v[5])
        print("Bandwidth p/ M:", v[6])
        print("     ---         ---     ")

else:
    print("Dados não salvos")

conn.close()  # Fecha a conexão com o Banco de Dados
