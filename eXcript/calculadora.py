"""Aplicando aprendizado, Calculadora simples"""

continuar = int(1)

while continuar == 1:
    print("Qual operação deseja fazer?")
    print("         1 - Adição")
    print("         2 - Subtração")
    print("         3 - Multiplicação")
    print("         4 - Divisão")
    print("         5 - Potenciação")

    acao = int(input("Somente o numero:"))
    num1 = float(input("Primeiro digito: "))
    num2 = float(input("Fornça o segundo número: "))

    if(acao == 1):
        print("Adição")
        res = num1 + num2
        print("{} + {} = {}".format(num1, num2, res))

    elif(acao == 2):
        print("Subtração")
        res = num1 - num2
        print("{} - {} = {}".format(num1, num2, res))

    elif(acao == 3):
        print("Multiplicação")
        res = num1 * num2
        print("{} * {} = {}".format(num1, num2, res))

    elif(acao == 4):
        if(num2 == 0 or num2 == None):
            print("O segundo valor é invalido")

        else:
            res = num1 / num2
            print("{} / {} = {}".format(num1, num2, res))

    elif(acao == 5):
        if(num2 <= num1):
            print("Potência")
            res = num1 ** num2
            print("{} elevado á {} = {}".format(num1, num2, res))

        else:
            print("A elevação é maior que o numero elevado")
    else:
        print("Comando não reconhecido!")

    acao = None

    print("Deseja recalcular?")
    print("1 - Sim -/- 2 - Não")
    continuar = int(input())

    if(continuar != 1):
        break

