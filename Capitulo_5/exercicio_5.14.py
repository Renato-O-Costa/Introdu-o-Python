# Exercício 5.14 - Interrupção do while com break
# Capítulo 5
# Renato Costa
# 24/03/2025

soma = 0
quantidade = 0
while True:
    n = int(input("Digite um número ou zero (0) para encerrar:\n"))
    if n == 0:
        break
    soma = soma + n
    quantidade = quantidade + 1
print("Quantidade de números digitados: {}".format(quantidade))
print("Soma: {}".format(soma))
print(f"Média: {soma / quantidade:10.2f}")

    
