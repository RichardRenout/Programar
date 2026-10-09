import os
os.system('cls')

while True:
    nota = int(input('Digite sua nota: '))
    if nota <=0 or nota >=10:
        print('Nota inválida, tente novamente')
    else:
        print('Parabêns, sua nota é: ',nota)
        break

