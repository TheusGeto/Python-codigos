import os

def limpar_terminal():
    # Limpa o terminal com Windows e Linux
    os.system("cls || clear")

def calcular_inss(salario):
    if salario <= 1100:
        inss = salario * 0.075
    elif salario <= 2203.48:
        inss = salario * 0.09
    elif salario <= 3305.22:
        inss = salario * 0.12
    elif salario <= 6433.57:
        inss = salario * 0.14
    else:
        inss = 854.36  # Valor máximo de desconto do INSS
    return inss

def calcular_irrf(salario, dependentes):
    faixa_isenta = 2259.20
    deducao_dependente = 189.59
    salario_com_dependentes = salario - (dependentes * deducao_dependente)
    
    if salario_com_dependentes <= faixa_isenta:
        return 0
    elif salario_com_dependentes <= 2826.65:
        return salario_com_dependentes * 0.075 - 142.80  # Dedução fixa de R$ 142,80
    elif salario_com_dependentes <= 3751.05:
        return salario_com_dependentes * 0.15 - 354.80  # Dedução fixa de R$ 354,80
    elif salario_com_dependentes <= 4664.68:
        return salario_com_dependentes * 0.225 - 636.13  # Dedução fixa de R$ 636,13
    else:
        return salario_com_dependentes * 0.275 - 869.36  # Dedução fixa de R$ 869,36

def calcular_vale_transporte(salario):
    return salario * 0.06

def calcular_vale_refeicao(valor_refeicao):
    return valor_refeicao * 0.20

def calcular_plano_saude(dependentes):
    return dependentes * 150.00

def calcular_salario_liquido(salario, inss, irrf, vale_transporte, vale_refeicao, plano_saude):
    total_descontos = inss + irrf + vale_transporte + vale_refeicao + plano_saude
    salario_liquido = salario - total_descontos
    return salario_liquido, total_descontos

def main():
    limpar_terminal()  # Limpa o terminal a cada execução do menu
    
    print("Sistema de Cálculo de Folha de Pagamento\n")

    # Entrada de dados
    matricula = input("Informe a matrícula do funcionário: ")
    senha = input("Informe a senha do funcionário: ")

    salario = float(input("Informe o salário base do funcionário (R$): "))
    dependentes = int(input("Informe o número de dependentes do funcionário: "))
    vale_transporte_opcao = input("Deseja receber vale transporte (s/n)? ").strip().lower()
    vale_refeicao = float(input("Informe o valor do vale refeição fornecido pela empresa (R$): "))
    
    # Cálculos
    inss = calcular_inss(salario)
    irrf = calcular_irrf(salario, dependentes)
    
    if vale_transporte_opcao == "s":
        vale_transporte = calcular_vale_transporte(salario)
    else:
        vale_transporte = 0
    
    vale_refeicao = calcular_vale_refeicao(vale_refeicao)
    plano_saude = calcular_plano_saude(dependentes)
    
    salario_liquido, total_descontos = calcular_salario_liquido(salario, inss, irrf, vale_transporte, vale_refeicao, plano_saude)

    # Exibindo resultados
    print("\nResumo de Cálculo:")
    print(f"Salário Base: R$ {salario:.2f}")
    print(f"Desconto INSS: R$ {inss:.2f}")
    print(f"Desconto IRRF: R$ {irrf:.2f}")
    print(f"Desconto Vale Transporte: R$ {vale_transporte:.2f}")
    print(f"Desconto Vale Refeição: R$ {vale_refeicao:.2f}")
    print(f"Desconto Plano de Saúde (dependente): R$ {plano_saude:.2f}")
    print(f"Total de Descontos: R$ {total_descontos:.2f}")
    print(f"Salário Líquido: R$ {salario_liquido:.2f}")

if __name__ == "__main__":
    main()
