# Exercício 4.6 - Calculando preço da viagem
# Capítulo 4
# Renato Costa
# 23/02/2025

# Solicita qual a distância da viagem
distancia = float(input("Informe qual a distância da viagem em Km:\n"))
distancia_viagem = distancia
preco_passagem = 0
if distancia_viagem <= 200:
    preco_passagem =  distancia_viagem * 0.50
else:
    preco_passagem = distancia_viagem * 0.45

print(f"Para uma viagem de {distancia_viagem} Km, o preço da passagem será de R$: {preco_passagem:5.2f}.")
