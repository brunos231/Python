# Trabalhando com módulos

# Comando de importação == import
# Comando para importar 1 item == from{nome da biblioteca} import {nome do item}

#import math - São os operadores matemáticos, vem por padrão
    #ceil - Arredonda o valor para cima
    #flor - Arredonda o valor para baixo
    #trunc - Trunca o numero sem arredondadar
    #pow - Potência
    #sqrt - Para raiz quadrada
    #factorial - Para numeros fatoriais

from math import sqrt

num = int(input('Primeiro numero: '))
raiz = sqrt(num)

print ('A raiz de {} é: {}'.format(num, raiz))

import random #Importa um numero aleatório

num = random.random(1, 10) #Randomriza numros entre 1 e 10

print(num)

