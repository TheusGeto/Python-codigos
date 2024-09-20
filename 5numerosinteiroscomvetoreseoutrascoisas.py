import os
os.system("cls || clear")

def ler_numeros():
    numeros = []
    for i in range(5):
        numero = int(input(f"Digite o {i + 1}º número: "))
        numeros.append(numero)
    return numeros

def processar_numeros(numeros):
    quantidade_pares = 0
    quantidade_impares = 0
    quantidade_positivos = 0
    quantidade_negativos = 0
  

    for numero in numeros:
        if numero % 2 == 0:
            quantidade_pares += 1
            
        else:
            quantidade_impares += 1
            
        if numero > 0:
            quantidade_positivos += 1
        elif numero < 0:
            quantidade_negativos += 1

    return {
        "quantidade_pares": quantidade_pares,
        "quantidade_impares": quantidade_impares,
        "quantidade_positivos": quantidade_positivos,
        "quantidade_negativos": quantidade_negativos
        }

def exibir_estatisticas(estatisticas):
    print("\nEstatísticas dos números:")
    print(f"Quantidade de pares: {estatisticas['quantidade_pares']}")
    print(f"Quantidade de ímpares: {estatisticas['quantidade_impares']}")
    print(f"Quantidade de positivos: {estatisticas['quantidade_positivos']}")
    print(f"Quantidade de negativos: {estatisticas['quantidade_negativos']}")

numeros = ler_numeros()
estatisticas = processar_numeros(numeros)
exibir_estatisticas(estatisticas)