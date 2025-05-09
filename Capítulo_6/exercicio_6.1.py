# Exercício 6.1 - Atualização do programa 6.2
# Capítulo 6 - Listas, tuplas, dicionários e conjuntos
# Renato Costa
# 14/04/2025

notas = [0, 0, 0, 0, 0, 0, 0] # Lista com valores zerados
soma = 0
x = 0

# Loop que solicita a entrada das notas, e as incrementa na variável soma.
while x < 7:
    notas[x] = float(input(f"Informe a nota {x}:\n"))
    soma += notas[x]
    x += 1
x = 0

# Loop que imprime nota a nota
while x < 7:
    print(f"Nota {x}: {notas[x]:6.2f}")
    x += 1
print(f"Total das notas: {soma:5.2f}") # Mostra o total somado das notes
print(f"Média: {soma / x:5.2f}") # Exibe a média final na tela
