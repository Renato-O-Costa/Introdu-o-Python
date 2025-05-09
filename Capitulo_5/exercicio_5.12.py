# Exercício 5.12 - Calculo de juros sobre depósitos mensais
# Capítulo 5
# Renato Costa
# 18/03/2025

# import pdb

# Módulo debbuger linha a linha
# pdb.set_trace()

deposito = float(input("Informe o valor do depósito inicial R$:\n"))
taxa = float(input("Informe o percentual de juros mensais:\n"))
valor_investido = float(input("Quanto será o valor do depósito mensal R$:\n"))
mes = 1
saldo = deposito

while mes <= 12:
    saldo = saldo + (saldo * (taxa / 100) +  valor_investido)
    print(f"Rendimento do {mes}° mês R$:\n {saldo:5.2f}.")
    mes += 1
print(f"O ganho obtido com os juros foi de R$:\n {saldo - deposito:5.2f}.")
