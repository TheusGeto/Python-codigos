import os
import time
from dataclasses import dataclass

os.system("cls || clear")

# Estrutura de dados:
@dataclass
# Classe para representar uma pessoa
class Pessoa:
    def __init__(self, salario, sexo, idade):  # Inicia os atributos do objeto, define os valores iniciais dos dados
        self.salario = salario
        self.sexo = sexo
        self.idade = idade

def limpar_terminal():  # Para limpar o terminal
    os.system('cls' if os.name == 'nt' else 'clear')

def adicionar_pessoas(pessoas):
    sexo = str(input("DIGITE SEU SEXO (M ou F): ")).upper()
    idade = int(input("DIGITE SUA IDADE: "))
    salario = float(input("DIGITE SEU SALARIO: "))

    # Criando a nova pessoa e salvando no arquivo
    pessoa = Pessoa(salario, sexo, idade)
    pessoas.append(pessoa)

    # Salvando no arquivo `pesquisa_regional.txt`
    with open("pesquisa_regional.txt", "a") as arquivo:
        arquivo.write(f"{sexo},{idade},{salario}\n")

    limpar_terminal()  # Limpa o terminal depois de adicionar uma pessoa

def exibir_resultados(pessoas):
    if not pessoas:
        print(" |****| Nenhuma pessoa foi cadastrada ainda |****| ")  # Caso nada seja adicionado
        return

    total_pessoas = len(pessoas)
    total_salario = sum(pessoa.salario for pessoa in pessoas)  # Soma dos salários
    maior_idade = max(pessoa.idade for pessoa in pessoas)
    menor_idade = min(pessoa.idade for pessoa in pessoas)

    # Contar mulheres com salário >= 5000
    total_mulheres5mil = sum(1 for pessoa in pessoas if pessoa.sexo == 'F' and pessoa.salario >= 5000)

    media_salario = total_salario / total_pessoas

    print(f"Total de Pessoas que responderam à pesquisa: {total_pessoas}")
    print(f"Média do salário da população: {media_salario:.2f}")
    print(f"Maior idade do grupo: {maior_idade}")
    print(f"Menor idade do grupo: {menor_idade}")
    print(f"Quantidade de mulheres com salário superior a R$ 5.000,00: {total_mulheres5mil}")

def carregar_dados():
    pessoas = []
    # Lendo dados do arquivo `pesquisa_regional.txt`
    if os.path.exists("pesquisa_regional.txt"):
        with open("pesquisa_regional.txt", "r") as arquivo:
            for linha in arquivo:
                sexo, idade, salario = linha.strip().split(',')
                pessoas.append(Pessoa(float(salario), str(sexo), int(idade)))
    return pessoas

def menu():
    pessoas = carregar_dados()

    while True:
        print("1 - Adicionar Pessoa")
        print("2 - Exibir Resultados")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_pessoas(pessoas)
        elif opcao == "2":
            limpar_terminal()
            exibir_resultados(pessoas)
        elif opcao == "3":
            limpar_terminal()
            print("SAINDO...")
            time.sleep(0.5)
            break
        else:
            limpar_terminal()
            print("======| OPÇÃO INVÁLIDA, TENTE NOVAMENTE! |======")

# EXECUTA O PROGRAMA
menu()

