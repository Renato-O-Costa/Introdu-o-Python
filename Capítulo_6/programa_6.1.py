# Programa 6.1 - Cálculo da média
# Capítulo 6
# Renato Costa
# 09/04/2025


# Cria lista de número com cinco elementos
notas = [6, 7, 5, 8, 9]
soma = 0
x = 0
while x < 5:
    soma += notas[x] # A cada loop, o valor do índice (notas[x]) é adicionado à variável soma.
    x += 1
print(f"Média: {soma / x:5.2f}")
