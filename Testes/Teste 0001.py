import os
os.system('cls')

print('\n Solicitando Dados')

salario_informado = float(input('\nDigite seu salario: '))

salario_minimo = 1621
quantidade_salarios = salario_informado / salario_minimo

print('\n Exibindo dados')
print('Quantidade de salarios: ', f'{quantidade_salarios:.3f}')