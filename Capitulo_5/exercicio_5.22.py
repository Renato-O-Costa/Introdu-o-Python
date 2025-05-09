# Exercício 5.22 - Calculadora simples
# Capítulo 5
# Renato Costa
# 01/04/2025

'''Problema: Escreva um programa que exiba uma lista de opções (menu): adição, subtração, divisão, multiplicação e sair.
Imprima a tabuada da operação escolhida.
Repita até que a opção saída seja escolhida.'''

while True:
    # Lista de opções percorrida pelo loop for
    operacoes = ["1 - Adição", "2 - Subtração", "3 - Multiplicação", "4 - Divisão", "5 - Sair"]
    for operacao in operacoes:
        print(operacao)
    opcao = int(input("Escolha uma operação:\n"))
    # Encerra o programa caso a opção seja 5
    if opcao == 5:
        break
    elif opcao >= 1 and opcao < 5:
        n = int(input("Tabuada de:\n"))
        x = 1
        # Loop que efetua a operação escolhida 
        while x <= 10:
            if opcao == 1:
                print(f"{n} + {x} = {n + x}")
            elif opcao == 2:
                print(f"{n} - {x} = {n - x}")
            elif opcao == 3:
                print(f"{n} x {x} = {n * x}")
            elif opcao == 4:
                print(f"{n} / {x} = {n / x:5.4f}")
            x += 1
        print("-" * 20)
    else:
        print("Opção inválida!")
