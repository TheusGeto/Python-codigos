import os
os.system("cls || clear")

quantidade_numeros = 3
lista_pares_positivos = []

print("\n ****SOLICITANDO DADOS**** ")
for i in range(quantidade_numeros):
    while True:
        numero = int(input(f" Digite o {i+1}º numero: "))
        if numero % 2 == 0 and numero > 0:
            lista_pares_positivos.append(numero)
            break
        else:
            print("****NUMERO INVALIDO, TENTE NOVAMENTE****")

print("\n****EXIBINDO RESULTADOS****")
for numero in lista_pares_positivos:
    print(numero)