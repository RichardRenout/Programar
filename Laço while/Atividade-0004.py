import os
import time
os.system('cls')

print('\n Solicitando Dados')

# Mantendo os Dados.
login_salvo = 'Richard'
senha_salva = '@123'

while True:
    login = input('\nDigite o login: ')
    senha = input('\nDigite a senha: ')

    if login == login_salvo and senha == senha_salva:
        print('Bem-Vindo!')
        break
    else:
        print('\n login ou senha inválido')
        print('Tente novamente! \n')
        input('Pressione qualquer tecla para continuar: ')
        os.system('cls')