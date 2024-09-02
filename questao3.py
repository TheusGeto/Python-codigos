import os
import time

os.system("cls || clear")
#Desenvolva um programa que use um laço `for` para imprimir todos os números pares de 2 a 10.

for i in range(11):
    if i % 2 == 0:
        print(f"{i}")
        time.sleep(1)
