# Programa para cálculo de distância de viagem
# Capítulo 3
# Renato de O. Costa
# 12/02/2025

distancia_km = int(input("Informe a distância da viagem em Km:\n"))
velocidade = int(input("Informe a velocidade média em Km/h:\n"))
tempo_da_viagem = distancia_km / velocidade
print(f"A viagem será feita em {tempo_da_viagem:2.2f}h.")
