import os
os.system("cls || clear")
numero1 = int(input("digite um numero: "))
numero2 = int(input("digite outro numero: "))
numero3 = int(input("digite mais um: "))

if numero1>numero2 and numero1>numero3:
	print(f" os numeros foram:  {numero1} ,  {numero2} , {numero3} o numero maior: {numero1}")

if numero2 > numero1 and numero2 > numero3:
	print(f" os numeros foram:  {numero1} ,  {numero2} , {numero3} o numero maior: {numero2}")


if numero2 > numero1 and numero3 > numero2:
	print(f" os numeros foram:  {numero1} ,  {numero2} , {numero3} o numero maior: {numero3}")

if numero1 < numero2 and numero1< numero3:
	print(f" o numero menor: {numero1}")

if numero2 < numero1 and numero2 < numero3:
	print(f" o numero menor: {numero2}")

if numero3 < numero1 and numero3 < numero2:
	print(f" o numero menor: {numero3}")
		
		