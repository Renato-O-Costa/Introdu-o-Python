# Programa 6.6 - Adição de elementos à lista
# Capítulo 6 - Listas, tuplas, dicionários e conjuntos
# Renato Costa
# 14/04/2025

L = []
while True:
    name = input("Informe o nome do convidado (S para sair):\n").title()
    if name == "S" or name == "s":
        break
    L.append(name)
x = 0
while x < len(L):
    print(L[x])
    x += 1
