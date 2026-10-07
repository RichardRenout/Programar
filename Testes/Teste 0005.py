import os
os.system('cls')

print('\n                Cardápio')

print('\n Numero do pedido: 1 | Picanha        | R$: 25,00 ')
print('\n Numero do pedido: 2 | Lasanha        | R$: 20,00 ')
print('\n Numero do pedido: 3 | Strogonoff     | R$: 18,00 ')
print('\n Numero do pedido: 4 | Bife Acebolado | R$: 15,00 ')
print('\n Numero do pedido: 5 | Pão com Ovo    | R$: 5,00 ')

pedido = input('\n Digite o numero do seu pedido: ')
print('\n O prato que você escolheu é o: ',pedido)

match pedido:
    case "1":
        print('\nVocê escolheu Picanha')
        print('\nValor de R$: 25,00 ')
    case "2":
        print('\nVocê escolheu Lasanhar')
        print('\nValor de R$: 20,00 ')
    case "3":
        print('\nVocê escolheu Strogonoff')
        print('\nValor de R$: 18,00 ')
    case "4":
        print('\nVocê escolheu Bife Acebolado')
        print('\nValor de R$: 15,00')
    case "5":
        print('\nVocê escolheu Pão com ovo')
        print('\nValor de R$: 5,00')
    case _:
        print('\nPedido Invalido')
