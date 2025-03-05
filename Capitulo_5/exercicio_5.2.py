# Exercício 5.2 - Contador de 50 a 100
# Capítulo 5
# Renato Costa
# 05/03/2025

x = 50
while x <= 100:
    print(x, end=", " if x < 100 else "\n" )
    x += 1
print("Loop encerrado!")
