lista = {}
while True:    
    produto = input('qual valor voce quer adicionar?')
    valor = input('Qual valor você desse produto?')

    lista[produto] = valor

    continuar = input("deseja adicionar mais algum produto?").lower()

    if continuar == 's':
        continue
    else:
        print(lista)
        break    