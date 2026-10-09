import os
import time
os.system('cls')

print('                          Solicitando Dados \n')

print(''' \n                                MENU 

Pão com ovo  ,Pão manteiga  ,Pão com queijo  ,Pão com presunto  ,Pão com mortadela
(1)R$:5,00    (2)R$:2,00     (3)R$:5,30       (4)R$:5,50         (5)R$:5,60

''')

while True:
    pedido = int(input('Digite o número do pedido: '))
    os.system('cls')
    if pedido < 1 or pedido > 5:
        print('Pedido inválido, tente novamente')
    else:
        print('Seu pedido é o número: ',pedido)
        match pedido:
            case 1:
                print('O valor é: 5,00')
            case 2:
                print('O valor é: 2,00')
            case 3:
                print('O valor é: 5,30')
            case 4:
                print('O valor é: 5,50')
            case 5:
                print('O valor é: 5,60')
        break 