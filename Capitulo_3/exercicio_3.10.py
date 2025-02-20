# Cálculo de reajuste salarial
# Exercício 3.10 do Capítulo 3
# Renato de O. Costa
# 11/02/2025

salario = float(input("Informe o seu salário R$:\n"))
taxa_reajuste = float(input("Informe o percentual do reajuste:\n"))
valor_aumento = salario * taxa_reajuste / 100 # Calcula o valor do aumento
novo_salario = salario + valor_aumento # Adiciona o aumento ao salário
print(f"Valor do aumento R$ {valor_aumento:5.2f}")
print (f"O valor do seu salário com aumento será:\nR$ {novo_salario:5.2f}")
