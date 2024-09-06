import os
os.system("cls || clear")


def checar_pares_impares():
    pares = 0
    impares =0
    for i in range(6):
        numero = int(input(f"Digite {i+1}º numero: "))
    
        if numero % 2 == 0:
            pares = pares + 1
        else:
            impares = impares + 1
    print(f" Quantidade de pares: {pares}")
    print(f"Quantidade de impares: {impares}")

checar_pares_impares()





