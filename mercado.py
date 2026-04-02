import os
lista = {}
while True:    
    produto = input('Qual valor voce quer adicionar? ')
    valor = float(input('Qual valor você desse produto? '))

    if produto in lista:
        print('Produto ja exite, valor alterado')
    lista[produto] = valor

    continuar = input('Deseja adicionar mais algum produto? ').lower()

    if continuar in ['s', 'sim']:
        os.system('cls')
        print('\nLista de produtos:')
        for produto, valor in lista.items():
            print(f'{produto}: R$ {valor:.2f}')
        continue
    else:
        os.system('cls')
        print('\nLista de produtos:')
        for produto, valor in lista.items():
            print(f'{produto}: R$ {valor:.2f}')
        break    