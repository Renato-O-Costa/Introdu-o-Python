# Aluguel de carros
# Capítulo 3
# Renato de O. Costa
# 13/02/2025

dias = int(input("Informe a quantidade de dias:\n"))
km_rodados = int(input("Qual a quantidade de quilometros rodados?\n"))
preco_por_dia = 60
preco_por_km = 0.15
valor_a_pagar = (dias * preco_por_dia) + (km_rodados * preco_por_km)
print(f"Quantidade de diárias: {dias}\nTotal de quilometros rodados: {km_rodados} Km")
print(f"Total à pagar R$ {valor_a_pagar:5.2f}")
