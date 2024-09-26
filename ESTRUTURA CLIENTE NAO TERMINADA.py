import os

from dataclasses import dataclass

os.system("cls || clear")

#estrutura de dados:
@dataclass
class Cliente:
    nome: str
    sobrenome: str
    idade: int
    peso: float
    altura: float

quantidade_cliente = 4

lista_de_clientes = []

print("\n****SOLICINTANDO DADOS DOS CLIENTES****")
for i in range(quantidade_cliente):
    cliente = Cliente(
        nome = input("Digite seu nome: "),
        sobrenome = input("Digite seu sobrenome: "),
        idade = int(input("Digite sua idade: ")),
        peso = float(input("Digite seu peso: ")),
        altura = float(input("Digite sua altura: "))
    )
    lista_de_clientes.append(cliente)

print("\n**** EXIBINDO DADOS DOS CLIENTE****")
for cliente in lista_de_clientes:
    print(f"Nome: {cliente.nome}")
    print(f"Idade: {cliente.idade}")

#DEFININDO ARQUIVO PARA SALVAR OS DADOS
nome_do_arquivo = "lista_de_clientes_LOJINHA DO THEUS.txt"

#ABRINDO ARQUIVO E DEFININDO QUE SERA FEITA A ESCRITA DE DADOS
with open(nome_do_arquivo, "a") as arquivo_clientes:
    
    for aluno in lista_de_clientes:
        #escrevendo no arquivo uma linha de cada vez
        arquivo_clientes.write(f"{cliente.nome}, {cliente.idade}. {cliente.sobrenome}, {cliente.peso}, {cliente.altura}\n")

#FECHANDO ARQUIVO
arquivo_clientes.close()
print("\n****DADOS ARMAZENADOS COM SUCESSO****")

#CREATED [X] FEITO ACIMA

#LENDO DADOS DE UM ARQUIVO
lista_de_clientes = []
print("\n**ACESSANDO DADOS DO ARQUIVO**")
with open(nome_do_arquivo, "r") as arquivo_de_origem:
    for linha in arquivo_de_origem:
        nome, idade = linha.strip().split(",")
        lista_de_clientes.append(Cliente(nome=nome, idade = int(idade)), sobrenome=sobrenome, )

#FECHA A CONEXÃO COM O ARQUIVO
arquivo_alunos.close()

print("\n****EXIBINDO DADOS DO ARQUIVO****")
for aluno in lista_de_alunos:
    print(f"Nome: {aluno.nome}")
    print(f"Idade: {aluno.idade}")

#READ[X] FEITO ACIMA