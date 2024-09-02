import os
os.system("cls || clear")
#Desenvolva um programa que utilize dois laços `for` (um dentro do outro) para imprimir um retângulo de 4 linhas por 6  colunas de asteriscos (`*`).


numero_linhas = 4
numero_colunas = 6

for i in range(numero_linhas):

    for j in range(numero_colunas):
        print('*', end='')
    print()