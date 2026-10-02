import os
os.system('cls')

for i in range(3):
    media = float(input('Digite sua media: '))
    media = media + 1 / 2

print(f'Media: {media}')
if media >= 7:
    print('Aprovado')
elif media >=4:
    print('Recuperação')
else:
    print('Reprovado')