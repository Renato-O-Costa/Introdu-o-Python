#Programa 4.7 - Categoria x preço, usando if/elif/else
# Capítulo 4
# Renato Costa
# 25/02/2025

# import pdb # Importa módulo de debug

# pdb.set_trace()

categoria = int(input("Informe a categoria do produto:\n"))
if categoria ==1:
    preco = 10
elif categoria == 2:
    preco = 18
elif categoria == 3:
    preco = 23
elif categoria == 4:
    preco = 26
elif categoria == 5:
    preco = 31
else:
    print("Categoria inválida, por favor insira um valor entre1 e 5.")
    preco = 0

print(f"O preço do produto é:\nR$ {preco:5.2f}")
