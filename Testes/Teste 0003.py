#limpa o terminal

import os
os.system('cls')

#Entrada

print('\nSolicitando Dados')

n1 = float
n2 = float

n1 = float(input('\n Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))

print('\n Clculando')

#Processamento

soma = (n1+n2)
subtracao = (n1-n2)
multiplicacao = (n1*n2)
divisao = (n1/n2)

#Saida

print('Soma: ',soma)
print('Subtracao: ',subtracao)
print('multiplicacao: ',multiplicacao)
print('divisao: ',divisao)
