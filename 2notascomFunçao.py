import os
os.system("cls || clear")

def somar_nota (nota_1,nota_2):
    soma = nota_1 + nota_2
    media = soma/2
    return media

def checagem_media ():
    media = somar_nota(nota_1,nota_2)
    if media >= 7:
        print("****APROVADO PARABENS****")
    else:
        print("****REPROVADO SINTO MUITO****")
    return media


nota_1 = float(input("DIGITE SUA NOTA: "))
nota_2 = float(input("A SEGUNDA NOTA: "))

calculo_total = somar_nota(nota_1,nota_2)

print(f"SUA MEDIA: {calculo_total}")

checagem_media()

