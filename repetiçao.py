import os
os.system("cls || clear")
#solicitando dados
numero = int(input("Digite um número: "))
print("Tabuada do número: {número}")
for i in range(1,11):
    print(f"{numero} x {i} = {numero * i}")