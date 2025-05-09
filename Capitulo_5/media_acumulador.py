# Calculando média com acumuladores

x = 1
soma = 0
while x <= 5:
    n = int(input(f"{x} - Digite o número:\n"))
    soma = soma + n
    x = x + 1
print(f"Média: {soma / 5:5.2f}")
