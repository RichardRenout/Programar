import os
import time
os.system('cls')

login_salvo = 'Richard'
senha_salva = '12345'
tentativas = 0

while tentativas < 3:
    login = input('\nDigite seu login: ')
    senha = input('\nDigite sua senha: ')

    if login == login_salvo and senha == senha_salva:
        print('Bem-Vindo!')
        break
    else:
        tentativas += 1
        print('\n Login ou senha inválidas!')
        print(f'Tentativas {tentativas} maxima de 3.')
        time.sleep(5)
        os.system('cls')

        if tentativas == 3:
            print('\nNúmero máximo de tentativas atingido!')
            print('Programa encerrado.')

