# Exercício 6.3 - Gerando listas a partir de outras listas
# Capítulo 6 - Listas, tuplas, dicionários e conjuntos
# Renato Costa
# 16/04/2025

# Enunciado:
# Crie duas listas e gere uma terceira lista que seja a união das duas primeiras, sem elementos repetidos.

lista1 = [1, 2, 3, 4, 5, 6, 7, 8,]
lista2 = [3, 4, 5, 6, 5, 7, 8, 9, 10]

lista3 = []
for item in lista1 + lista2: # Concatena as duas listas
    if item not in lista3:
        lista3.append(item)
print(f"Lista 3: {lista3}")