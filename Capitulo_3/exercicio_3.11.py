# Programa que calcula desconto sobre produtos
# Capítulo 3
#12/02/2025
# Renato de O. Costa

preco_produto = float(input("Informe o preço do produto.\nR$ "))
p_desconto = float(input("Qual o percentual de desconto?\n"))
valor_desconto = preco_produto * p_desconto / 100
preco_final = preco_produto - valor_desconto
print(f"Valor do desconto.\n R$: {valor_desconto:5.2f}")
print(f"Preço final do produto com desconto.\nR$: {preco_final:5.2f}")

