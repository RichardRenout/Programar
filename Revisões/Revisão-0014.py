import os
os.system('cls')

cardapio = {
    1: ("Picanha", 25.00),
    2: ("Lasanha", 20.00),
    3: ("Strogonoff", 18.00),
    4: ("Bife Acebolado", 15.00),
    5: ("Pão com ovo", 3.00)
}

total_pago = 0.0

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("=" * 35)
    print("           CARDÁPIO")
    print("=" * 35)
    print(f"{'Código':<8} {'Prato':<18} {'Valor':>7}")
    print("-" * 35)
    for codigo, (prato, valor) in cardapio.items():
        print(f"{codigo:<8} {prato:<18} R$ {valor:>5.2f}")
    print("=" * 35)
    
    try:
        opcao = int(input("\nDigite o código do prato desejado: "))
        
        if opcao in cardapio:
            prato_escolhido, valor = cardapio[opcao]
            total_pago += valor
            print(f"\n-> {prato_escolhido} (R$ {valor:.2f}) adicionado ao pedido!")
        else:
            print("\nCódigo inválido! Escolha uma opção do cardápio.")
            input("Pressione Enter para tentar novamente...")
            continue
            
    except ValueError:
        print("\nEntrada inválida! Digite apenas o número do código.")
        input("Pressione Enter para tentar novamente...")
        continue

    continuar = input("\nDeseja escolher outro prato? (S/N): ").strip().upper()
    if continuar != 'S':
        break

print("\n" + "=" * 35)
print(f"TOTAL A PAGAR: R$ {total_pago:.2f}")
print("=" * 35)