import os
os.system('cls')

while True:
    primeira_nota = float(input('Digite sua primeira nota: '))
    segunda_nota = float(input('Digite sua segunda nota: '))
    if primeira_nota and segunda_nota < 0 or primeira_nota and segunda_nota >10:
        print('Nota inválida')
    else:
        media = (primeira_nota + segunda_nota) / 2
        print(f'Sua nota é: {media}')
        break
