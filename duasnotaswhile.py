import os
os.system("cls || clear")

while True:
    nota = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    if nota < 0 or nota > 10:
        print("\n*****As notas devem ser maior ou igual a 0 e menor ou igual a 10*****")
    elif nota2 < 0 or nota2 > 10:
      print("\n*****As notas devem ser maior ou igual a 0 e menor ou igual a 10*****")
    
    else:
        break

soma = nota + nota2
media = soma/2

print(f"***SUA MEDIA: {media}****")