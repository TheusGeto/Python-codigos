import os
os.system("cls || clear")

print("""
      1-
      2-
      3-
      4-
      5-
      6- 
      7-
      8-
      9-
      10-
      11-
      12-""")

opcao = int(input("digite um dos 12 numeros:  "))

match(opcao):
    case 1:
        print(" Janeiro ")
    case 2:
        print(" Fevereiro ")
    case 3:
        print(" Março ")
    case 4:
        print(" Abril ")
    case 5:
        print(" Maio ")
    case 6:
        print(" Junho ")
    case 7:
        print(" Julho ")
    case 8:
        print(" Agosto ")
    case 9:
        print(" Setembro ")
    case 10:
        print(" Outubro ")
    case 11:
        print(" Novembro ")
    case 12:
        print(" Dezembro ")
    case _:
        print(" esse mes nao existe BURRO ANIMAL ASNO QUADRUPEDE ")