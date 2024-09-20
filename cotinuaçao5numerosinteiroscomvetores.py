import os
os.system("cls || clear")
quantidade_numeros = 0

def ler_numeros():
    global quantidade_numeros  # Use the global variable
    numeros = []
    for i in range(5):
        numero = int(input(f"Digite o {i + 1}º número: "))
        quantidade_numeros += 1  # Increment the global variable
        numeros.append(numero)
    return numeros

def processar_numeros(numeros):
    quantidade_pares = 0
    quantidade_impares = 0
    quantidade_positivos = 0
    quantidade_negativos = 0
    quantidade_pares_positivos = 0

    for numero in numeros:
        if numero % 2 == 0:
            quantidade_pares += 1
            if numero > 0:
                quantidade_pares_positivos += 1  # Check positivity here
        else:
            quantidade_impares += 1

        if numero > 0:
            quantidade_positivos += 1
        elif numero < 0:
            quantidade_negativos += 1

    return {
        "quantidade_pares_positivos": quantidade_pares_positivos,
        "quantidade_impares": quantidade_impares,
        "quantidade_positivos": quantidade_positivos,
        "quantidade_negativos": quantidade_negativos,
        "quantidade_numeros": quantidade_numeros  # Include this in the return
    }

def exibir_estatisticas(estatisticas):
    print("\nEstatísticas dos números:")
    print(f"Quantidade de positivos pares: {estatisticas['quantidade_pares_positivos']}")
    print(f"Quantidade de ímpares: {estatisticas['quantidade_impares']}")
    print(f"Quantidade de positivos: {estatisticas['quantidade_positivos']}")
    print(f"Quantidade de negativos: {estatisticas['quantidade_negativos']}")
    print(f"Quantidade de números inseridos: {estatisticas['quantidade_numeros']}")

# Função principal para executar o programa
numeros = ler_numeros()
estatisticas = processar_numeros(numeros)
exibir_estatisticas(estatisticas)
