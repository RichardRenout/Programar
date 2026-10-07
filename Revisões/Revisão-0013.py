import os
os.system('cls')

soma = 0
QUANTIDADES = 3

for i in range(QUANTIDADES):
    while True:
        nota = float(input(f'Digite sua nota {i+1}: '))
        if nota >= 0 and nota <= 10:
            soma = soma + nota
            break
        else:
            print('Nota Inválida! A nota deve ser entre 0 e 10.\n')

media = soma / QUANTIDADES
print(f'\nA média é: {media:.2f}')

if media >= 7:
    print('Situação: Aprovado')
elif media >= 5:
    print('Situação: Recuperação')
else:
    print('Situação: Reprovado')