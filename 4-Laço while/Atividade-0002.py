import os
os.system('cls')

soma = 0
QUANTIDADE_DE_NOTAS = 2

for i in range(QUANTIDADE_DE_NOTAS):
    while True:
        nota = float(input(f'Digite a nota: '))
        if nota >= 0 and nota <= 10:
            soma = soma + nota
            break
        else:
            print()
            print('Inválido, tente novamente')

media = soma / QUANTIDADE_DE_NOTAS

print(f'Média: {media}')
