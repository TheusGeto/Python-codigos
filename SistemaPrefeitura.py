import os
from dataclasses import dataclass

os.system("cls || clear")

# Estrutura de dados:
@dataclass
# Classe para representar uma família
class Familia:
    def __init__(self, salario, numero_filhos): #Inicia os atributos do objeto, define os valores iniciais dos dados
        self.salario = salario
        self.numero_filhos = numero_filhos

def limpar_terminal():  # Para limpar o terminal
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para adicionar uma família ao arquivo
def adicionar_familias(familias):
    salario = float(input("DIGITE SUA RENDA FAMILIAR (Se mais de uma pessoa trabalhar na casa, some os valores e adicione o total): "))
    numero_filhos = int(input("DIGITE A QUANTIDADE DE FILHOS QUE TEM: "))

    # Criando a nova família e salvando no arquivo
    familia = Familia(salario, numero_filhos)
    familias.append(familia)

    # Salvando no arquivo
    with open("pesquisa_prefeitura.txt", "a") as arquivo:
        arquivo.write(f"{salario},{numero_filhos}\n")  # Corrigido para 'numero_filhos'

    limpar_terminal()  # Limpa o terminal depois de adicionar uma família

# Para exibir os resultados da pesquisa
def exibir_resultados(familias):
    if not familias:
        print(" |****|Nenhuma família foi cadastrada ainda|****| ")  # Caso nada seja adicionado, isto será exibido
        return

    total_familias = len(familias)
    total_salario = sum(familia.salario for familia in familias)  # Soma dos salários
    total_filhos = sum(familia.numero_filhos for familia in familias)  # Soma dos filhos
    maior_salario = max(familia.salario for familia in familias)
    menor_salario = min(familia.salario for familia in familias)

    media_salario = total_salario / total_familias
    media_filhos = total_filhos / total_familias

    print(f"Total de famílias que responderam à pesquisa: {total_familias}")
    print(f"Média do salário da população: {media_salario:.2f}")
    print(f"Média do número de filhos: {media_filhos:.2f}")
    print(f"Maior salário: {maior_salario:.2f}")
    print(f"Menor salário: {menor_salario:.2f}")

# Para carregar os dados do arquivo
def carregar_dados():
    familias = []
    if os.path.exists("pesquisa_prefeitura.txt"):
        with open("pesquisa_prefeitura.txt", "r") as arquivo:
            for linha in arquivo:
                salario, numero_filhos = linha.strip().split(',')
                familias.append(Familia(float(salario), int(numero_filhos)))  # Corrigido para 'numero_filhos'
    return familias

# Para exibir o menu e realizar a escolha
def menu():
    familias = carregar_dados()

    while True:
        print("1 - Adicionar Família")
        print("2 - Exibir Resultados (Dados)")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_familias(familias)
        elif opcao == "2":
            limpar_terminal()
            exibir_resultados(familias)
        elif opcao == "3":
            limpar_terminal()
            print("|****|SAINDO....|****|")
            break
        else:
            limpar_terminal()
            print("|****|OPÇÃO INVÁLIDA, TENTE NOVAMENTE!!!!|****|")

# EXECUTA O PROGRAMA
menu()
