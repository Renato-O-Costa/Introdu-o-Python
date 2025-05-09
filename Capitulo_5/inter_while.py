# Interronpendo o loop while

import pdb

pdb.set_trace()

s = 0
while True:
    v = int(input("Digite um número para somar ou 0 para sair:\n"))
    if v == 0:
        break
    s += v
print(f"Soma total dos números digitados: {s}")
