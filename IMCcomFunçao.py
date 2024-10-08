import os
os.system("cls || clear")



def IMC(peso, altura):
    calculo = peso/altura**2
    return calculo

def checagem_IMC(calculo):
    IMC_calculado = IMC(peso,altura)

    if IMC_calculado < 18.5:
        print(f"{IMC_calculado} Abaixo do peso,ta magrinho em meu fi, porfavor consulte um nutricionista para orientação")
    if IMC_calculado >= 18.5 and IMC_calculado < 24.9:
        print(f"{IMC_calculado} Padrão corporal, continue assim rapa")
    if IMC_calculado >= 25 and IMC_calculado < 29.9:
        print(f"{IMC_calculado} Sobrepeso, ta gordinho em fi, vai acabar quebrando minha balança, bora fazer uma dieta e atividade fisica seu sedentario")
    if IMC_calculado >= 30 and IMC_calculado < 34.9:
        print(f"{IMC_calculado} grau 1 mano, parabens em, mas isso ja pode te prejudicar, procure um medico porfavor")
    if IMC_calculado >= 35 and IMC_calculado < 39.9:
        print(f"{IMC_calculado} Obesidade grau 2,ta gordo pra porra em, ja quebrou a balança ja, procure orientação medica isso pode fazer mal a voce")
    if IMC_calculado >= 40:
        print(f"{IMC_calculado} Obesidade")

        
        
peso = float(input("digite seu peso em KG: "))
altura = float(input("digite sua altura em M: "))