import os
os.system("cls || clear")

print("""
      1- Picanha do Lula
      2- Lasanha do Garfield
      3- Strogonoff com a galinha da sua MAE 
      4- Bife Acebolado que meteu no seu RABO
      5- Pão com ovao do chefe""")

opcao = int(input("digite o numero do pedido: "))

match(opcao):
    case 1:
        print("Picanha do Lula, R$25,00")
    case 2:
        print("Lasanha do Garfield, R$20,00")
    case 3:
        print("Strogonoff com a galinha da sua MÃE, R$18,00")
    case 4:
        print("Bife acebolado, que meteu no seu rabo,R$15,00 ")
    case 5:
        print("Pão com ovão do chefe, R$5,00")
    case _:
        print("**OPÇAO INVALIDA**")