import os
os.system("cls || clear")

lista_notas = []
quantidade_notas = 3

for i in range(quantidade_notas):
    notas = float(input("Digite sua nota: "))
    lista_notas.append(notas)

soma = sum(lista_notas)
media = soma/quantidade_notas



for contador, notas in enumerate(lista_notas):
    print(f"Sua {contador+1}º: {notas}")

print(f"SUA MEDIA FINAL: {media}")

