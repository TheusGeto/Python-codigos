import os
os.system("cls || clear")

quantidade_numeros = 5
lista_de_numeros = []

def verificando_numeros(lista_de_numeros):
    lista_atulizada = []

    for numero in lista_de_numeros:
        if numero < 0: #caso o numero digitado seja negativo, sera trocado por 0
            numero = 0
        lista_atulizada.append(numero)
    return lista_atulizada

print("****SOLICITANDO DADOS****")
for i in range(quantidade_numeros):
    numero = int(input(f"digite o {i+1}º numero: "))
    lista_de_numeros.append(numero)

lista_de_numeros = verificando_numeros(lista_de_numeros)

print("\n****EXIBINDO DADOS****")
for cada_numero in lista_de_numeros:
    print(cada_numero)