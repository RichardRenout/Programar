import os
os.system('cls')

dia = int(input('Digite seu numero(1,2,3,4,5,6,7): '))

if dia <= 7 and dia <= 1:
    print('Final de Semana')
else:
    print('\n Dia util')

match dia:
    case "1":
        print('Dia não util')
    case "2":
        print('\n Dia util')
    case "3":
        print('\n Dia util')
    case "4":
        print('\n Dia util')
    case "5":
        print('\n Dia util')
    case "6":
        print('\n Dia util')
    case "7":
        print('\n Dia não util')


#TERMINAR DE FAZER E PESQUISAR COMO SOLUCIONAR