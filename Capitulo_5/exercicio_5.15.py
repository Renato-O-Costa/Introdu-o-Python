# Exercício 5.15 - Máquina registradora
# Capítulo 5
# Renato Costa
# 25/03/2025

a_pagar = 0
while True:
    codigo = int(input("Informe o código do produto ou tecle zero (0) para sair:\n"))
    if codigo == 0:
        break    
    elif codigo == 1:
        preco = 0.50
    elif codigo == 2:
        preco = 1.00
    elif codigo == 3:
        preco = 4.00
    elif codigo == 5:
        preco = 7.00
    elif codigo == 9:
        preco = 8.00
    else:
        print("Código inválido!") # Em caso de código inexistente, mostra mensagem na tela
    if preco != 0:
        quantidade = int(input("Informe a quantidade desejada:\n"))
        a_pagar = a_pagar + (preco * quantidade)
print(f"Valor total da compra R$ {a_pagar:5.2f}")


