import os
import time
os.system("cls || clear")

contagem_negativos = 0

# Laço para continuar pedindo números enquanto a condição não for atendida
while True:
    # Solicita um número ao usuário
    numero = float(input("Digite um número (0 ou um número positivo para parar): "))
    
    # Verifica se o número é positivo ou zero
    if numero >= 0:
        break  # Sai do laço se o número for zero ou positivo
    
    # Se o número for negativo, incrementa a contagem
    contagem_negativos += 1

# Mostra a quantidade de números negativos inseridos
print(f"Quantidade de números negativos inseridos: {contagem_negativos}")