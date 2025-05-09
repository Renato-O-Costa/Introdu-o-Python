# Exercício 5.26 - Obtendo o valor da divisão inteira
# Capítulo 5
# Renato Costa
# 07/04/2025

'''Escreva um programa que calcule o resto da divisão inteira entre dois
números. Utilize apenas as operações de soma e subtração para calcular o
resultado.'''

dividendo = int(input("Dividendo:\n"))
divisor = int(input("Divisor:\n"))
quociente = 0
x = dividendo
while x >= divisor:
    x -= divisor
    quociente += 1
resto = x
print(f"O resto de {dividendo} / {divisor} é {resto}")
