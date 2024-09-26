import os
from dataclasses import dataclass
os.system("cls || clear")

#CRUD:

#CREATED
#READ
#UPDATE
#DELETE

#ESTRUTURA DE DADOS
@dataclass

class Aluno:
    nome: str
    idade: int

quantidade_alunos = 2

lista_de_alunos = []

print("\n****SOLICINTANDO DADOS DOS ALUNOS****")
for i in range(quantidade_alunos):
    aluno = Aluno(
        nome = input("digite seu nome: "),
        idade = int(input("digite sua idade: "))
    )
    lista_de_alunos.append(aluno)

print("\n**** EXIBINDO DADOS DOS ALUNOS****")
for aluno in lista_de_alunos:
    print(f"Nome: {aluno.nome}")
    print(f"Idade: {aluno.idade}")

#DEFININDO ARQUIVO PARA SALVAR OS DADOS
nome_do_arquivo = "lista_de_alunos_SENAI.txt"

#ABRINDO ARQUIVO E DEFININDO QUE SERA FEITA A ESCRITA DE DADOS
with open(nome_do_arquivo, "a") as arquivo_alunos:
    
    for aluno in lista_de_alunos:
        #escrevendo no arquivo uma linha de cada vez
        arquivo_alunos.write(f"{aluno.nome}, {aluno.idade}\n")

#FECHANDO ARQUIVO
arquivo_alunos.close()
print("\n****DADOS ARMAZENADOS COM SUCESSO****")

#CREATED [X] FEITO ACIMA

#LENDO DADOS DE UM ARQUIVO
lista_de_alunos = []
print("\n**ACESSANDO DADOS DO ARQUIVO**")
with open(nome_do_arquivo, "r") as arquivo_de_origem:
    for linha in arquivo_de_origem:
        nome, idade = linha.strip().split(",")
        lista_de_alunos.append(Aluno(nome=nome, idade = int(idade)))

#FECHA A CONEXÃO COM O ARQUIVO
arquivo_alunos.close()

print("\n****EXIBINDO DADOS DO ARQUIVO****")
for aluno in lista_de_alunos:
    print(f"Nome: {aluno.nome}")
    print(f"Idade: {aluno.idade}")

#READ[X] FEITO ACIMA

