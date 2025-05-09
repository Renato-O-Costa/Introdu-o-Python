# Exercício 5.6
# Capítulo 5
# Renato Costa
# 10/03/2025

# Tabuada
print("Seja bem-vindo(a)!")
numero = int(input("Digite um número para ver sua tabuada:\n"))
x = 1
print(f"Tabuada de {numero}")
while x <= 10:
    print(f"{numero} x {x} = {numero * x}")
    x += 1
print("Tabuada encerrada.")
