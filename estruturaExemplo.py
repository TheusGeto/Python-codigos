import os
from dataclasses import dataclass
os.system("cls || clear")

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