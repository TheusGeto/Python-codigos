import os
os.system("cls || clear")

soma = 0

for i in range(5):
    numero = int(input(f"Digite {i+1}º numero: "))
    soma = soma + numero

print(f"Soma: {soma}")