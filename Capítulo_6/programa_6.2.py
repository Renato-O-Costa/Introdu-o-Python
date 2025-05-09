# Programa 6.2 - Cálculo da média com notas digitadas
# Capítulo 6 - Listas, dicionários, tuplas e conjuntos
# Renato Costa
# 09/04/2025

# Cria lista com cinco elementos
notas = [0, 0, 0, 0, 0]
soma = 0
x = 0
while x < 5:
    notas [x] = float(input(f"Nota {x}:\n"))
    soma += notas[x]
    x += 1
x = 0
while x < 5:
    print(f"Nota {x}:{notas[x]:^6.2f}")
    x += 1
print(f"Média {soma / x:5.2f}")
