import os
os.system("cls || clear")

ano_nascimento = int(input("DIGITE O ANO DE NASCIMENTO: "))
ano_atual = int(input("DIGITE O ANO ATUAL: "))

def verificar__idade():
    idade = ano_atual - ano_nascimento
    return idade

idade_calculada = verificar__idade()

print(f"SUA IDADE É: {idade_calculada}")