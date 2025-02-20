# Entrada de dados com a função input()

#nome = input("Digite seu nome:\n")
#print(f"Você digitou {nome}.")
#print(f"Olá, {nome}!")


# Convertendo os valores da entrada de dados
anos = int(input("Anos de serviço:\n"))
valor_por_ano = float(input("Valor por ano:\n"))
bonus = anos * valor_por_ano
print(f"Bônus de R${bonus:5.2f}.")

