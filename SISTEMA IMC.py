import os
# ALUNO: MATHEUS GABRIEL

# Função para limpar a tela e exibir o logo
def logoSenai():
    os.system("cls || clear")
    print("=== SENAI === ")

# Função para calcular o IMC
def calcular_IMC(peso, altura):
    return peso / (altura ** 2)

# Função para analisar e checar o IMC
def checagem_IMC(imc):
    if imc < 18.5:
        return f"{imc:.2f} - Abaixo do peso. Consulte um nutricionista."
    elif 18.5 <= imc < 25:
        return f"{imc:.2f} - Peso normal. Continue assim!"
    elif 25 <= imc < 30:
        return f"{imc:.2f} - Sobrepeso. Considere uma dieta e atividade física."
    elif 30 <= imc < 35:
        return f"{imc:.2f} - Obesidade grau I. Procure um médico."
    elif 35 <= imc < 40:
        return f"{imc:.2f} - Obesidade grau II. Atenção necessária!"
    else:
        return f"{imc:.2f} - Obesidade grau III. Procure orientação médica."

#listas vazias para armazenar os dados dos usuários
nomes = []
sobrenomes = []
idades = []
alturas = []
pesos = []

# Solicitando os dados dos usuários em loop
while True:
    logoSenai()
    nome = input("Digite o nome do usuário (ou digite 'sair' para encerrar): ")
    
    # Verificando se o usuário quer sair
    if nome.lower() == 'sair':
        break
    
    sobrenome = input("Digite o sobrenome do usuário: ")
    idade = int(input("Digite a idade do usuário: "))
    altura = float(input("Digite a altura do usuário (em metros): "))
    peso = float(input("Digite o peso do usuário (em quilogramas): "))
    
    # Adicionando os dados às listas
    nomes.append(nome)
    sobrenomes.append(sobrenome)
    idades.append(idade)
    alturas.append(altura)
    pesos.append(peso)

# Exibindo os dados armazenados com o IMC
logoSenai()
print("\nDados dos usuários:")
for i in range(len(nomes)):
    imc = calcular_IMC(pesos[i], alturas[i])
    IMC = checagem_IMC(imc)
    
    print(f"Usuário {i+1}:")
    print("Nome Completo:", f"{nomes[i]} {sobrenomes[i]}")
    print("Idade:", idades[i])
    print("Altura:", alturas[i], "metros")
    print("Peso:", pesos[i], "quilogramas")
    print("IMC:", IMCsair)
    print()