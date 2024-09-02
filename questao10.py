import os
import time

os.system("cls || clear")
# Escreva um programa que calcule a soma dos números ímpares de 1 a 9 utilizando um laço `for`.
for i in range(11):
    if i % 2 == 1:
        print(f"{i}+{i} = {i+i}")
        time.sleep(1)
