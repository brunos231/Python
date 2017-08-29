import lxml
from lxml import html
import requests
import sqlite3

#Cria os elementos de conexão
conn = sqlite3.connect('base')
cursor = conn.cursor()

#Cria a tabela onde serão salvos os dados
cursor.execute("""
CREATE TABLE IF NOT EXISTS packet(
    id integer primary key autoincrement,
    nome varchar(20),
    vlr_hr varchar(20),
    vlr_m varchar(20),
    n_pc varchar(20),
    memoria varchar(20),
    storage varchar(20),
    transfer varchar(30),
    info_ext varchar(40)
) 
""")

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

    elif info == elementos[-1]:
        memoria = str(info[1][0][1][0].text_content())
        sdd = str(info[1][0][3][0].text_content())
        inf_ext = str(info[1][0][2][0].text_content())

    #Posiciona todos os valores em uma lista principal
    lista.append([nome, vlr_hr, vlr_m, nucleo_cpu, memoria, sdd, band, inf_ext])

#Exibe as informações ao usúario
for dados in lista:
    print("Serviço:            ", dados[0])
    print("Valor p/ Hora:      ", "$"+dados[1]+"/hr")
    print("Valor p/ Mês:       ", "$"+dados[2]+"/m")
    print("Nucleos p/ serviço: ", dados[3])
    print("Memória:            ", dados[4])
    print("Storage:            ", dados[5])
    print("Bandwidth p/ M:     ", dados[6])

    #Alguns elementos possuem dados extras
    if dados[2] or dados[3] or dados[5] or dados[6]:
        print("Extra:              ", dados[-1])

    print("     ----            ----      ")

#Pergunta se deseja gravar os dados
print("Deseja salvar os dados no Banco?")
resposta = str(input("Sim[S] / Não[N]: ")).lower()

#Se for sim, faz a gravação
if resposta == 's':
    #Insere a lista no Banco de Dados
    cursor.executemany("""
        INSERT INTO packet(nome, vlr_hr, vlr_m, n_pc, memoria, storage, transfer, info_ext)
            VALUES (?,?,?,?,?,?,?,?)
    """, lista)

    #Comita os dados na tabela
    conn.commit()

    print("Salvo com Sucesso")

    print("Deseja ver os dados salvos?")
    resposta = str(input("Sim[S] / Não[N]: ")).lower()

    cursor.execute("""
            SELECT * FROM packet
            """)

    view = cursor.fetchall()

    print("Dados do Banco de Dados")
    for v in view:
        print("Chave:              ", v[0])
        print("Serviço:            ", v[1])
        print("Valor p/ Hora:      ", v[2])
        print("Valor p/ Mês:       ", v[3])
        print("Nucleos p/ serviço: ", v[4])
        print("Memória:            ", v[5])
        print("Storage:            ", v[6])
        print("Bandwidth p/ M:     ", v[7])
        print("     ----      ----       ")

else:
    print("Dados não salvos")

conn.close()  # Fecha a conexão com o Banco de Dados