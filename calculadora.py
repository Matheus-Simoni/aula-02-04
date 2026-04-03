import os

lista = {}

while True:
    prod = input('Qual produto você gostaria de add? ')
    quant = int(input('Qual a quantidade? '))

    if prod in lista:
        lista[prod] += quant
    else:
        lista[prod] = quant

    continuar = input('Deseja adicionar mais algum produto? ').lower()

    if continuar in ['s', 'sim']:
        os.system('cls')  
        print(lista)
        continue
    else:
        os.system('cls')
        print(lista)
        break