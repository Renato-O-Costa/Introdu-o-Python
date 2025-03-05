# Exercício 4.8 - Operações básicas
# Capítulo 4
# Renato Costa
# 25/02/2025

'''Escreva um programa que leia dois números e que pergunte qual
operação você deseja realizar. Você deve poder calcular soma (+),
subtração (-), multiplicação (*) e divisão (/). Exiba o resultado da
operação solicitada. '''

import pdb

pdb.set_trace()

a = int(input("Informe o primeiro número:\n"))
b = int(input("Informe o segundo número:\n"))
operacao = input("Escolha a operação desejada: (+, -, / , *)\n")

if operacao == '+':
    resultado = a + b    
elif operacao == '-':
    resultado = a - b    
elif operacao == '*':
    resultado = a * b    
elif operacao == '/':
    resultado = a / b    
else:
    print("Opção inválida. Selecione uma das seguintes operações (+ - * /).")
    resultado = 0
print(f"Resultado da operação: {resultado}")
