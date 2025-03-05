# Exercício 4.9 - Liberação de empréstimo bancário
# Capítulo 4
#Renato Costa
# 27/02/2025

'''Escreva um programa para aprovar o empréstimo bancário para compra de
uma casa. O programa deve perguntar o valor da casa a comprar, o salário
e a quantidade de anos a pagar. O valor da prestação mensal não pode ser
superior a 30% do salário. Calcule o valor da prestação como sendo o
valor da casa a comprar dividido pelo número de meses a pagar. '''

valor_da_casa = float(input("Informe o valor da casa  R$:\n "))
salario = float(input("Informe seu salário mensal R$:\n"))
meses_a_pagar = int(input("Deseja pagar em quantos meses?\n"))
valor_prestacao = valor_da_casa / meses_a_pagar

if valor_prestacao > (salario * 0.30):
    print(f"O valor da prestação R$ {valor_prestacao:5.2f}, excedeu à 30% do seu salário. Empréstimo negado.")
else:
    print(f"Empréstimo aprovado! Valor da prestação mensal R$ {valor_prestacao:5.2f}. Quantidade de meses a pagar {meses_a_pagar}.")
