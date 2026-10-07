import os

os.system('cls')

nome = input('Digite seu nome: ')
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
sexo = input('Digite M para masculino ou F para feminino: ').upper()

match sexo:
    case 'M':
        peso_ideal = (72.7 * altura) - 58

        print(f'\nNome: {nome}')
        print(f'Peso atual: {peso:.2f} kg')
        print(f'Peso ideal: {peso_ideal:.2f} kg')

    case 'F':
        peso_ideal = (62.1 * altura) - 44.7

        print(f'\nNome: {nome}')
        print(f'Peso atual: {peso:.2f} kg')
        print(f'Peso ideal: {peso_ideal:.2f} kg')

    case _:
        print('\nSexo inválido! Digite apenas M ou F.')
