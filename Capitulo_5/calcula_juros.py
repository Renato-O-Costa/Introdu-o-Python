# Exercício 5.11 - Calculador simples de juros mensais de conta.
# Capítulo 5
# Renato Costa
# 17/03/2025

import pdb

# Módulo debugger linha a linha
pdb.set_trace()

deposito = float(input(f"Informe o valor do depósito R$:\n"))
taxa = float(input("Informe o percentual de juros mensais:\n"))
mes = 1
saldo = deposito
while mes <= 24:
    saldo +=  (saldo * (taxa / 100))
    print(f"Rendimento do {mes}° mês R$:\n {saldo:5.2f}.")
    mes += 1
print(f"O ganho obtido com os juros foi de R$ {saldo - deposito:8.2f}.")
