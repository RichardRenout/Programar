import os
os.system('cls')

login_cadastrado = input('Cadastre seu login: ')
senha_cadastrada = input('Cadastre sua senha: ')

os.system('cls')

while True:
    login = input('Digite seu login: ')
    senha = input('Digite sua senha: ')

    if login == login_cadastrado and senha == senha_cadastrada:
        print('Login realizado com sucesso!')
        break
    else:
        print('Login ou senha incorretos. Tente novamente.')