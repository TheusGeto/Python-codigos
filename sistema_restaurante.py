"""
Informe o número da turma: 
Turma - 93313

Nome completo dos componentes.
1 - Itauã Guaberto.
2 - Matheus Gabriel 
"""

total = 0
pratos_selecionados = []  # Lista para armazenar os pratos escolhidos

import os
os.system("cls || clear") 

while True:
    print("""
    1- filé - R$7,50
    2- macarrão - R$5,00
    3- arroz e feijão - R$10,50
    4- mocotó - R$14,99
    5- salada - R$3,24
    6- lasanha - R$15,50
    7- strogonoff - R$17,75
    """)

    prato = input("faça sua escolha acima: ")
    match(prato):
        case "1":
            total += 7.50
            pratos_selecionados.append(("1", "filé", 7.50))
            print("filé = R$7,50")
        case "2":
            total += 5.0
            pratos_selecionados.append(("2", "macarrão", 5.0))
            print("macarrão = R$5,00")
        case "3":
            total += 10.50
            pratos_selecionados.append(("3", "arroz e feijão", 10.50))
            print("arroz e feijão = R$10,50")
        case "4":
            total += 14.99
            pratos_selecionados.append(("4", "mocotó", 14.99))
            print("mocotó = R$14,99")
        case "5":
            total += 3.24
            pratos_selecionados.append(("5", "salada", 3.24))
            print("salada = R$3,24")
        case "6":
            total += 15.50
            pratos_selecionados.append(("6", "lasanha", 15.50))
            print("lasanha = R$15,50")
        case "7":
            total += 17.75
            pratos_selecionados.append(("7", "strogonoff", 17.75))
            print("strogonoff = R$17,75")
        case _: 
            print("resposta inválida, por favor insira um código de prato válido!")

    while True:
        continuar = input("quer acrescentar mais pratos? [SIM(S)/NÃO(N)] ").strip().upper()
        if continuar in ['S', 'N']:
            break
        else:
            print("resposta inválida!!!")
    
    if continuar == 'N':
        break

# Exibindo subtotal antes de aplicar a forma de pagamento
print(f"\nSubtotal: R${total:.2f}")

# Solicitar a forma de pagamento

while True:
    print("\nFormas de pagamento:")
    print("1 - À vista (desconto de 10%)")
    print("2 - Cartão de crédito (acréscimo de 10%)")
    pagamento = input("Escolha a forma de pagamento (1 ou 2): ")

    if pagamento in ["1", "2"]:
        break
    else:
        print("Opção inválida! Escolha 1 para 'À vista' ou 2 para 'Cartão de crédito'.")

# Aplicando pagamento e desconto

if pagamento == "1":
    desconto = total * 0.10
    valor_final = total - desconto
    print(f"Forma de pagamento: À vista (desconto de 10%)")
    print(f"Desconto aplicado: R${desconto:.2f}")
elif pagamento == "2":
    acrescimo = total * 0.10
    valor_final = total + acrescimo
    print(f"Forma de pagamento: Cartão de crédito (acréscimo de 10%)")
    print(f"Acréscimo aplicado: R${acrescimo:.2f}")

# Exibindo os pratos escolhidos e o valor total a pagar

print("\nPratos escolhidos:")
for prato in pratos_selecionados:
    print(f"Código: {prato[0]}, Nome: {prato[1]}, Preço: R${prato[2]:.2f}")

print(f"\nSubtotal: R${total:.2f}")
print(f"Valor final a pagar: R${valor_final:.2f}")
