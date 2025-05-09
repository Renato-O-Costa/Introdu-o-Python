# Exercício 5.7
# Capítulo 5
# Renato Costa
# 10/03/2025

import pdb

pdb.set_trace()


# Programa que solicita dois números ao usuário, e mostra a tabuada

n = int(input("Tabuada de: "))
inicio = int(input("De: "))
fim = int(input("Até: "))
x = inicio # Variável contadora recebe início como valor
while x <= fim:
    print(f"{n} x {x} = {n * x}")
    x += 1
