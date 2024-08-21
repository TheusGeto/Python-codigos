import os
os.system("cls || clear")

nome = str(input("digite seu nome e sobrenome: "))
idade = int(input("digite sua idade: "))

if idade < 18 or idade >= 65:
    print("**Não é obrigado a votar**")
else:
    print("**É Obrigado a votar**")