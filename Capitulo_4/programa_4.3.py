# Cálculo do imposto de renda

salario = float(input("Informe o valor do seu salário, para calcular o IR:\nR$: "))
base = salario
imposto = 0
if base > 3000:
    imposto = imposto + ((base - 3000) * 0.35)
    base = 3000
if base > 1000:
    imposto  = imposto + ((base - 1000) * 0.20)
print(f"Salário: R${salario:6.2f}. Imposto a pagar: R${imposto:6.2f}.")
    
