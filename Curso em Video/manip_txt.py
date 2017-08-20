# Trabalhando com Strings

# Pode-se usar aspas '' ou ""

frase = 'Curso em Video Python'

#Fatiamento
print(frase[9::3]) #Intervalos de de tempo

#Análise
print(len(frase)) #Conta o tamanho da String
print(frase.count('o')) #Conta qualquer elemento da String
print(frase.find('deo')) #Indica a posição onde começa o elemento, caso não exista retorna -1
print('Curso' in frase) #Verifica se existe a palavra na String

#Transformação
print(frase.replace('Python', 'Android')) #Faz a substituição da palavra
print(frase.upper()) #Altera as letras em maiusculo
print(frase.lower()) #Altera as letras em minusculo
print(frase.capitalize()) #Todas as letras para minusculo, e só a primeira letra maiuscula
print(frase.title()) #Faz a captalização em cada palavra a cada espaço
print(frase.strip()) #Remove os espaços excedentes na String
print(frase.rstrip()) #Remove só os espaços do fim da String
print(frase.lstrip()) #Remove todos os espaços do inicio da String

#Divisão
print(frase.split()) #Onde houver espaços é feita uma divisão, como um novo vetor

#Junção
print('-'.join(frase)) #Onde ouver um espaço é adicionado o caractere