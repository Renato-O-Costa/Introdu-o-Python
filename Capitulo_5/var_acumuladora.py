# Variável acumuladora

n = 1
soma = 0 # Acunuladora
while n <= 10:
    x = int(input(f"Digite o {n}° número:\n"))
    soma = soma + x
    n = n + 1
print(f"Soma: {soma}")
