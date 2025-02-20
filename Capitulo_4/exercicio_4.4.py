# Programa para cálculo de reajuste salarial
# Exercício 4.4
# Renato de O. Costa
# 19/02/2025


# Solicita o valor do salário do usuário
salario = float(input("Informe o valor do seu salário R$:\n"))
base = salario
aumento = 0
novo_salario = 0

# Verificando as condições para o aumento proporcional
if base > 1250:
    aumento = base * 0.10
    novo_salario = base + aumento
if base <= 1250:
    aumento = base * 0.15
    novo_salario = base + aumento

# Imprime na tela as informações fornecidas
print(f"Salário informado R$: {base:5.2f}")
print(f"Valor do aumento R$: {aumento:5.2f}")
print(f"Valor do novo salário com aumento R$: {novo_salario:5.2f}")

