"""Adicionando informações no Banco de Dados"""

import sqlite3

path = '../Crawlers'

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

nome = str(input("Nome: "))
sobrenome = str(input("Sobrenome: "))
idade = int(input("Idade: "))

lista = []
#lista.append([nome, sobrenome, idade])

cursor.execute("""
CREATE TABLE IF NOT EXISTS pessoa(
    id integer primary key autoincrement,
    nome varchar(30),
    sobrenome varchar(30),
    idade integer
);
""")


cursor.executemany("""
INSERT INTO pessoa(nome, sobrenome, idade)
    VALUES(?,?,?)
""", lista)

conn.commit()

cursor.execute("""
SELECT * FROM pessoa
""")

lista = cursor.fetchall()

conn.close()

for x in lista:
    print(x)
