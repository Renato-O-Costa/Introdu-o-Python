# Programa que imprime os números pares a partir do zero

fim = int(input("Informe o último número a ser impresso:\n"))
x = 0
while x <= fim:
    if x % 2 == 0:
        print(x)
    x += 1
print("Fim  execução!")


# Outra solução válida. Programas diferentes que resultam na mesma solução

final = int(input("Digite o último número a imprimir:\n"))
x = 0
while x <= final:
    print(x)
    x += 2
print("Fim da execução.")
