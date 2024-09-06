import os
os.system("cls || clear")

def calcular_soma (numero_1,numero_2):
    soma = numero_1 + numero_2
    divisao = numero_1/numero_2
    multiplacacao = numero_1 * numero_2
    return soma
def calcular_subtracao (numero_1,numero_2):
    subtracao = numero_1 - numero_2
    return subtracao
def calcular_multiplacao (numero_1,numero_2):
    multiplacacao = numero_1 * numero_2
    return multiplacacao
def calcular_divisao (numero_1,numero_2):
    divisao = numero_1/numero_2
    return divisao

numero_1 = int(input("digite um numero: "))
numero_2 = int(input("digite um numero: "))

resultado_soma = calcular_soma(numero_1, numero_2)
resultado_subtracao = calcular_subtracao(numero_1, numero_2)
resultado_multiplicacao = calcular_multiplacao(numero_1, numero_2)
resultado_divisao = calcular_divisao(numero_1, numero_2)

print(f" SOMA: {resultado_soma}, SUBTRAÇAO: {resultado_subtracao}, MULTIPLICAÇAO: {resultado_multiplicacao}, DIVISAO: {resultado_divisao} ")

