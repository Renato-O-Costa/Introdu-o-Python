# Programa que calcula a redução do tempo do vida de um fumante
# Capítulo 3
# Renato de O. Costa
# 13/02/2025

'''Escreva um programa para calcular a redução do tempo de vida de um
fumante. Pergunte a quantidade de cigarros fumados por dia e quantos
anos ele já fumou. Considere que um fumante perde 10 minutos de vida a
cada cigarro, e calcule quantos dias de vida um fumante perderá. Exiba o
total em dias.'''

cigarros_por_dia = int(input("Quantos cigarros você fuma por dia?\n"))
anos_fumando = int(input("Quantidade de anos fumando:\n"))
reducao_em_minutos = anos_fumando * 365 * cigarros_por_dia * 10
# Um dia tem 24 x 60 minutos
reducao_em_dias = reducao_em_minutos / (24 * 60)
print(f"Redução do tempo de vida {reducao_em_dias:2.1f} dias.")
