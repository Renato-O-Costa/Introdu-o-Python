# Exercício 5.13 - Cálculo para quitar dívida
# Capítulo 5
# Renato Costa
# 18/03/2025

import pdb

pdb.set_trace()

# Variáveis globais
divida = float(input("Informe o valor inicial da dívida R$:\n"))
taxa = float(input("Informe o percentual de juros:\n"))
pagto_mensal = float(input("Quanto será pago mensalmente?\nR$: "))
mes = 1

# Verifica se o juros é maior que o pagamento
if divida * (taxa / 100) >= pagto_mensal:
    print("Sua dívida dificilmente será paga, pois os juros estão muito acima do pagamento mensal.")
else:
    saldo = divida
    juros_pagos = 0
    while saldo > pagto_mensal:
        juros = saldo * taxa / 100
        saldo = saldo + juros - pagto_mensal
        juros_pagos = juros_pagos + juros
        print(f"Saldo da dívida no mês {mes} é de R$ {saldo:6.2f}.")
        mes = mes + 1
    print(f"Para pagar uma dívida de R$ {divida:8.2f}, a {taxa:5.2f} % de juros,")
    print(f"você precisará de {mes - 1} meses, pagando um total de R$ {juros_pagos:8.2f} de juros.")
    print(f"No último mês, você teria um saldo residual de R$ {saldo:8.2f} a pagar.")

    
