#ESCREVA UM ALGORITIMO QUE SOLICITE DUAS NOTAS PARA UM ALUNO
#CASO SEJA MENOR QUE 0 OU MAIOR QUE 10, MOSTRE A PERGUNTA NOVAMENTE
#CALCULE E MOSTRE A MEDIA ARITIMETICA
import os
os.system("cls || clear")

soma = 0
quantidade_notas = 2
for i in range(quantidade_notas):
    while True:
        nota = float(input(f"Digite sua {i+1}º nota: "))
        if nota >= 0 and nota <= 10:
            break
    soma += nota
media = soma/quantidade_notas

print(f"***SUA MEDIA: {media}****")