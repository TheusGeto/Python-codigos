import os
os.system("cls || clear")

nome = input("digite seu nome: ")
idade = input("digite sua idade: ")
nota1 = float(input("digite sua primeira nota: "))
nota2 = float(input("digite sua segunda nota: "))
nota3 = float(input("digite sua terceira nota: "))

notasomada = nota1+nota2+nota3
media = notasomada/3

if media >= 7:
    print(f" nome: {nome},sua idade: {idade}, sua nota final: {media} APROVADO PARABENS QUE ORGULHO")

else:
    print(f" nome: {nome},sua idade: {idade}, sua nota final: {media} REPROVADO, SINTO MUITO")