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
    soma_pares = 0
    soma_impares = 0
    soma_geral = sum(numeros)  # calcular a soma geral

    # Inicializa maior e menor número com o primeiro valor da lista
    maior_numero = menor_numero = numeros[0]

    for numero in numeros:
        if numero % 2 == 0:
            quantidade_pares += 1
            soma_pares += numero
        else:
            quantidade_impares += 1
            soma_impares += numero

        if numero > 0:
            quantidade_positivos += 1
        elif numero < 0:
            quantidade_negativos += 1

        if numero > maior_numero:
            maior_numero = numero
        if numero < menor_numero:
            menor_numero = numero

    # Calcula a média dos pares e ímpares verificação
    if quantidade_pares > 0:
        media_pares = soma_pares / quantidade_pares
    else:
        media_pares = 0

    if quantidade_impares > 0:
        media_impares = soma_impares / quantidade_impares
    else:
        media_impares = 0

    media_geral = soma_geral / len(numeros)

    # Inverte a lista 
    numeros_invertidos = []
    for i in range(len(numeros) - 1, -1, -1):
        numeros_invertidos.append(numeros[i])

    return {
        "quantidade_pares": quantidade_pares,
        "quantidade_impares": quantidade_impares,
        "quantidade_positivos": quantidade_positivos,
        "quantidade_negativos": quantidade_negativos,
        "maior_numero": maior_numero,
        "menor_numero": menor_numero,
        "media_pares": media_pares,
        "media_impares": media_impares,
        "media_geral": media_geral,
        "numeros_invertidos": numeros_invertidos
    }

def exibir_estatisticas(estatisticas):
    print("\nEstatísticas dos números:")
    print(f"Quantidade de pares: {estatisticas['quantidade_pares']}")
    print(f"Quantidade de ímpares: {estatisticas['quantidade_impares']}")
    print(f"Quantidade de positivos: {estatisticas['quantidade_positivos']}")
    print(f"Quantidade de negativos: {estatisticas['quantidade_negativos']}")
    print(f"Maior número: {estatisticas['maior_numero']}")
    print(f"Menor número: {estatisticas['menor_numero']}")
    print(f"Média dos números pares: {estatisticas['media_pares']:.2f}")
    print(f"Média dos números ímpares: {estatisticas['media_impares']:.2f}")
    print(f"Média de todos os números: {estatisticas['media_geral']:.2f}")
    print(f"Números na ordem inversa: {estatisticas['numeros_invertidos']}")

# exibindo dados
numeros = ler_numeros()
estatisticas = processar_numeros(numeros)
exibir_estatisticas(estatisticas)