# Exercício 6.2 - Gerando listas
# Capítulo 6 - Listas, tuplas, dicionários e conjuntos
# Renato Costa
# 15/04/2025


# Cria duas listas vazias
lista_1 = []
lista_2 = []

# Gerando a primeira lista
while True:
    e = int(input("Informe um valor para a primeira lista ou (0 para encerrar):\n"))
    if e == 0:
        break
    lista_1.append(e)
# Gerando a segunda lista
while True:
    e = int(input("Informe um valor para a segunda lista ou (0 para encerrar):\n"))
    if e == 0:
        break
    lista_2.append(e)
lista_3 = lista_1[:]
lista_3.extend(lista_2)
x = 0
while x < len(lista_3):
    print("%d: %d" % (x, lista_3[x]))
    x += 1
