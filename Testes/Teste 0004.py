import os
os.system('cls')

n1 = float(input('\nDigite seu primeiro numero: '))
n2 = float(input('Digite seu segundo numero: '))
op = input('Digite a operação(+,-,/,*): ')

print(f'\nO primeiro numero que você escolheu foi {n1}')
print(f'O segundo numero que você escolheu foi {n2}')
print(f'A operação que você escolheu foi {op}')

match op:
    case '+':
        print(f'\nA soma é {n1+n2}')
    case '-':
        print(f'\nA Subtração é {n1-n2}')
    case '*':
        print(f'\nA multiplicação é {n1*n2}')
    case '/':
        print(f'\nA divisão é {n1/n2}')
    case _:
        print('Situação Invalida')