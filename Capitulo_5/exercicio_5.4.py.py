# Programa que imprime os números ímpares

fim = int(input("Informe o último número a ser impresso:\n"))
x = 0
while x <= fim:
    if x % 2 != 0:
        print(x, end=", " if x < fim else "\n")
    x += 1
