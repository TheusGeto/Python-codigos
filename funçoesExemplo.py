import os
os.system("cls || clear")

def calcular_media (numero_1,numero_2):
    soma = numero_1 + numero_2
    resultado = soma/2
    return resultado

numero_1 = int(input("digite um numero: "))
numero_2 = int(input("digite um numero: "))

media = calcular_media(numero_1, numero_2)
print(f" media: {media}")



          