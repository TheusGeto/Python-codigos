import os
os.system("cls || clear")

quantidade_notas = 3
soma = 0

for i in range(quantidade_notas):
    nota = float(input(f"Digite {i+1}º nota: "))
    soma = soma + nota
    media = soma/quantidade_notas

def checagem_media (media):
    if media >= 7:
     print("****aprovado****")
    elif media >= 4:
     print("****REcuperaçao****")
    else: 
     print("***REPROVADO****")

    return media

print(f"SUA MEDIA: {media}")

checagem_media(media)

