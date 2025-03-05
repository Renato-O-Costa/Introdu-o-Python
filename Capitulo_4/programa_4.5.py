# Programa 4.5 - Conta de telefone
# Capítulo 4
# Renato Costa
# 24/02/2025

minutos = int(input("Quantos minutos você utilizou este mês?\n"))
if minutos < 200:
    preco= 0.20
else:
    if minutos < 400: # estrutura aninhada dentro do primeiro if/else
        preco = 0.18
    else:
        preco = 0.15
print(f"Você vai pagar este mês:\nR${minutos * preco:6.2f}") # Imprime a mensagem na tela com o cálculo do valor.

