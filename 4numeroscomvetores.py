import os
os.system("cls || clear")

quantidade_numeros = 4
lista_numeros = []
lista_negativos = []
lista_positivos = []

def verificar_numeros_negativos(lista_numeros):
    lista_de_negativos = []

    for numero in lista_numeros:
        if numero < 0:
            lista_de_negativos.append(numero)
    
    quantidade_negativos = len(lista_de_negativos)

    return quantidade_negativos

def verificar_positivos(lista_numeros):
    lista_de_positivos = []

    for numero in lista_numeros:
        if numero > 0:
            lista_de_positivos.append(numero)
    soma__positivos = sum(lista_de_positivos)

    return soma__positivos

print("\n****SOLICITAÇAO DE NUMEROS****")
for i in range(quantidade_numeros):
    numero = float(input(f"Digite o {i+1}º:  "))
    lista_numeros.append(numero)

quantidade_de_negativos = verificar_numeros_negativos(lista_numeros)
soma_de_positivos = verificar_positivos(lista_numeros)

print("****EXIBINDO RESULTADOS****")
for contador, numero in enumerate(lista_numeros):
    print(f"{contador+1} º numeros: {numero}")

print(f"\nQuantidade de negativos: {quantidade_de_negativos}")
print(f"Soma de positivos: {soma_de_positivos}")