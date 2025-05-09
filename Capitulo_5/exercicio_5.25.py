# Exercício 5.25 - Cálculo da raiz com o método de Newton
# Capítulo 5
# Renato Costa
# 07/04/2025

'''Escreva um programa que calcule a raiz quadrada de um número.
Utilize o método de Newton para obter um resultado aproximado.
Sendo n o número a obter a raiz quadrada, considere a base b=2.
Calcule p usando a fórmula p=(b+(n/b))/2.
Agora, calcule o quadrado de p.
A cada passo, faça b=p e recalcule p usando a fórmula apresentada.
Pare quando a diferença absoluta entre n e o quadrado de p for menor que 0,0001.'''

n = int(input("Informe o número para saber sua raiz quadrada:\n"))
b = 2
while abs(n - (b * b)) > 0.0001:
          p = (b + (n / b)) / 2
          b = p
print(f"A raiz quadrada de {n} é aproximadamente {p:8.4f}.")
