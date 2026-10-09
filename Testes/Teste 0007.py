import os
os.system('cls')

print('''               MENU                

PEDIDO              VALOR       NUMERO

PÃO                  R$: 2.00    1
PÃO COM OVO          R$: 3.00    2
PÃO COM QUEIJO       R$: 4.00    3
PÃO COM PRESUNTO     R$: 5.00    4
PÃO COM ATUM         R$: 6.00    5

''')

while True:
    numero = int(input('\nDigite o numero do pedido: '))
    if numero < 1 or numero >5:
        print('Inválido, tente novamente')
        continue

    print('\n')

    escolha = str(input('\nDeseja fazer outro pedido? (Sim ou Não)'))

    os.system('cls')

    match escolha:
        case 'Sim':
            continue
        case 'Não':
                print('\nPedido escolhido, qual a forma de pagamento?')
                break
        case _:
            print('Opção Inválida')

print('''\n           Formas de Pagamento   

Pix                 1
Dinheiro            2
Cartão de Crédito   3
Cartão de Debito    4
Vale Alimentação    5
''')

while True:
    pagamento = int(input('Digite a forma de pagamento (1 a 5): '))
    if pagamento < 1 or pagamento > 5:
        print('Inválido, tente novamente')
        continue

    print('\n')

    match pagamento:
        case 1:
            print('Sua forma de pagamento é Pix')
        case 2:
            print('Sua forma de pagamento é Dinheiro')
        case 3:
            print('Sua forma de pagamento é Cartão de Crédito')
        case 4:
            print('Sua forma de pagamento é Cartão de Debito')
        case 5:
            print('Sua forma de pagamento é Vale Alimentaçãpo')
        case _:
            print('Inválido, tente novamente')
    break