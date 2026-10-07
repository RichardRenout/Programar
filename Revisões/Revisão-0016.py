import os
os.system(cls)

soma = 0
quantidade = 0

while True:
    valor = int(input("Digite um valor inteiro positivo (ou um número negativo para sair): "))
    
    if valor < 0:
        break
    
    soma += valor
    quantidade += 1

if quantidade > 0:
    media = soma / quantidade
    print(f"\nA média aritmética dos {quantidade} números digitados é: {media:.2f}")
else:
    print("\nNenhum número positivo foi digitado.")