import os
os.system('cls')

while True:
    nota = float(input('Digite sua nota de 0 a 10: '))
    if nota < 0 or nota > 10:
        print('Inválido')
        print('Tente Novamente \n')
    else:
        print(f'Nota: ',nota)
        break



