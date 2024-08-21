import os
os.system("cls || clear")

print("""
      1- Domingo
      2- Segunda feira
      3- Terça feira
      4- Quarta feira
      5- Quinta feira
      6- Sexta feira
      7- Sábado""")

opcao = int(input("digite o numero de um dia da semana: "))

match(opcao):
    case 1:
        print("Final de semana, mas é domingo...chore amanha tem trabalho")
    case 2:
        print(" Dia util vai trabalhar ou estudar")
    case 3:
        print(" Dia util vai trabalhar ou estudar")
    case 4:
        print(" Dia util vai trabalhar ou estudar")
    case 5:
        print(" Dia util vai trabalhar ou estudar")
    case 6:
        print(" Dia util, SEXTOU MANO")
    case 7:
        print("FINAL DE SEMANA, DESCANSE")
    case _:
        print(" ESSE DIA NEM EXISTE BURRO ")