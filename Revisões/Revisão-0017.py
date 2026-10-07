import os
os.system('cls')

total_salario = 0.0
total_pessoas = 0
maior_idade = None
menor_idade = None
mulheres_salario_alto = 0

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("=" * 30)
    print("        PESQUISA REGIONAL")
    print("=" * 30)
    print("Código | Descrição")
    print("  1    | Adicionar pessoa")
    print("  2    | Exibir resultados")
    print("  3    | Sair")
    print("=" * 30)
    
    opcao = input("\nEscolha uma opção: ").strip()
    
    if opcao == '1':
        print("\n--- CADASTRO DE PESSOA ---")
        idade = int(input("Digite a idade: "))
        
        sexo = input("Digite o sexo (M/F): ").strip().upper()
        while sexo not in ['M', 'F']:
            sexo = input("Sexo inválido! Digite M ou F: ").strip().upper()
            
        salario = float(input("Digite o salário (R$): "))
        
        total_salario += salario
        total_pessoas += 1
        
        if maior_idade is None or idade > maior_idade:
            maior_idade = idade
        if menor_idade is None or idade < menor_idade:
            menor_idade = idade
            
        if sexo == 'F' and salario >= 5000.00:
            mulheres_salario_alto += 1
            
        print("\nPessoa adicionada com sucesso!")
        input("Pressione Enter para voltar ao menu...")
        
    elif opcao == '2':
        print("\n--- RESULTADOS DA PESQUISA ---")
        if total_pessoas > 0:
            media_salario = total_salario / total_pessoas
            print(f"a) Média de salário do grupo: R$ {media_salario:.2f}")[cite: 6]
            print(f"b) Maior idade: {maior_idade} anos | Menor idade: {menor_idade} anos")[cite: 6]
            print(f"c) Mulheres com salário a partir de R$ 5.000,00: {mulheres_salario_alto}")[cite: 6]
        else:
            print("Nenhuma pessoa foi cadastrada ainda.")
            
        input("\nPressione Enter para voltar ao menu...")
        
    elif opcao == '3':
        print("\nPrograma encerrado.")
        break
        
    else:
        print("\nOpção inválida!")
        input("Pressione Enter para tentar novamente...")