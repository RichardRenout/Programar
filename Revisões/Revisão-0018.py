import os
os.system('cls')

total_familias = 0
soma_salarios = 0.0
soma_filhos = 0
maior_salario = None
menor_salario = None

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("=" * 35)
    print("      PESQUISA DA PREFEITURA")
    print("=" * 35)
    print("Código | Descrição")
    print("  1    | Adicionar família")
    print("  2    | Sair e exibir resultados")
    print("=" * 35)
    
    opcao = input("\nEscolha uma opção: ").strip()
    
    if opcao == '1':
        print("\n--- CADASTRO DE FAMÍLIA ---")
        salario = float(input("Digite o salário da família (R$): "))
        filhos = int(input("Digite o número de filhos: "))
        
        total_familias += 1
        soma_salarios += salario
        soma_filhos += filhos
        
        if maior_salario is None or salario > maior_salario:
            maior_salario = salario
        if menor_salario is None or salario < menor_salario:
            menor_salario = salario
            
        print("\nDados da família cadastrados com sucesso!")
        input("Pressione Enter para continuar...")
        
    elif opcao == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 45)
        print("         RESULTADOS DA PESQUISA")
        print("=" * 45)
        
        if total_familias > 0:
            media_salario = soma_salarios / total_familias
            media_filhos = soma_filhos / total_familias
            
            print(f"a) Total de famílias entrevistadas: {total_familias}")[cite: 7]
            print(f"b) Média do salário da população: R$ {media_salario:.2f}")[cite: 7]
            print(f"c) Média do número de filhos: {media_filhos:.1f}")[cite: 7]
            print(f"d) Maior salário: R$ {maior_salario:.2f}")[cite: 7]
            print(f"e) Menor salário: R$ {menor_salario:.2f}")[cite: 7]
        else:
            print("Nenhuma família foi cadastrada.")
            
        print("=" * 45)
        print("\nPrograma encerrado.")
        break
        
    else:
        print("\nOpção inválida!")
        input("Pressione Enter para tentar novamente...")