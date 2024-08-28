import os
os.system("cls || clear")
quantidade_tentativas = 3
contador = 1
while True:
    login =str(input(f"Digite seu login: "))
    senha = str(input("Digite sua senha: "))
    contador += 1

    if login == "Theus" and senha == "Theussola2209":
        print("****BEM VINDO THEUS O GIGANTE****")
        break
    else:
        print("****Login ou senha invalidos****")
        print(f"Tentativa: {contador}")
        if contador == 3:
            break

print("****FIM****")