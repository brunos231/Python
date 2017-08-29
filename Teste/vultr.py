import lxml
from lxml import html
import requests
import sqlite3

#Cria os elementos de conexão
conn = sqlite3.connect('base')
cursor = conn.cursor()

#Cria a tabela onde serão salvos os dados
cursor.execute("""
CREATE TABLE IF NOT EXISTS vultr(
    id integer primary key autoincrement,
    nome varchar(20),
    vlr_m varchar(20),
    memoria varchar(20),
    n_pc varchar(20),
    transfer varchar(20),
    storage varchar(20)
) 
""")


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
        band = str(y[0][1][0][2].text_content())
        sdd = str(y[0][0][1].text_content())

        #Coloca os valores dentro de uma lista
        lista.append([nome, vlr_m, pcs, memoria, band, sdd])

    else:
        return lista
"""----------------------Fim da função-------------------------"""

# Faz a junção dos elementos em uma unica lista
lista = list(pesq(elementos) + pesq(elementos1))

for dados in lista:
    print("Serviço:       ", dados[0])
    print("Valor p/ Mês:  ", dados[1]+"/m")
    print("Nº de PC´s  :  ", dados[2])
    print("Memória:       ", dados[3])
    print("Storage:       ", dados[0])
    print("Bandwidth p/ M:", dados[4])
    print("     ---         ---     ")

print("Deseja salvar os dados no Banco?")
resposta = str(input("Sim[S] / Não[N]: ")).lower()

if resposta == 's':
    #Insere a lista no Banco de Dados
    cursor.executemany("""
        INSERT INTO vultr(nome, vlr_m, n_pc, memoria, transfer, storage)
            VALUES (?,?,?,?,?,?)
    """, lista)

    #Comita os dados na tabela
    conn.commit()

    print("Salvo com Sucesso")
    del(resposta)

    print("Deseja ver os dados salvos?")
    resposta = str(input("Sim[S] / Não[N]: ")).lower()

    cursor.execute("""
    SELECT * FROM vultr
    """)

    view = cursor.fetchall()

    print("Dados do Banco de Dados")
    for v in view:
        print("Chave:         ", v[0])
        print("Serviço:       ", v[1])
        print("Valor p/ Mês:  ", v[2])
        print("Nº de PC´s  :  ", v[3])
        print("Memória:       ", v[4])
        print("Storage:       ", v[5])
        print("Bandwidth p/ M:", v[6])
        print("     ---         ---     ")
else:
    print("Dados não salvos")



conn.close()  # Fecha a conexão com o Banco de Dados


