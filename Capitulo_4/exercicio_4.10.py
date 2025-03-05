# Exercício 4.10 - Cálculo de consumo de energia
# Capítulo 4
# Renato Costa
# 27/02/2025

''' Escreva um programa que calcule o preço a pagar pelo fornecimento de
energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de
instalação: R para residências, I para indústrias e C para comércios.
Calcule o preço a pagar de acordo com a tabela a seguir.

+---------------------------------------+ 
|        Preço por tipo e faixa de               |
+---------------------------------------+ 
| Tipo       | Faixa (kWh)      | Preço           |
+========================+
|Residencial | Até 500              | R$ 0,40 | 
                     | Acima de 500    | R$ 0,65 |
+---------------------------------------+
|Comercial | Até 1000              | R$ 0,55 |
|                  | Acima de 1000    | R$ 0,60 |
+---------------------------------------+
| Industrial   | Até 5000            | R$ 0,55 |
|                    | Acima de 5000  | R$ 0,60 |
+---------------------------------------+'''

kwh = int(input("Informe o consumo em kWh:\n"))
tipo = input("Informe o tipo de instalação:\nR - Residencial\nC - Comercial\nI - Industrial\n").upper()

if tipo == 'R':
    preco = 0.40 if kwh <= 500 else 0.65
elif tipo == 'C':
    preco = 0.55 if kwh <= 1000 else 0.60 # Uso do operador ternário, para deixar o código mais limpo.
elif tipo == 'I':
    preco = 0.55 if kwh <= 5000 else 0.60
else:
    print("Tipo de instalação inválido. Insira R, C ou I.")
    exit() # Encerra o programa no caso de entradas inválidas.
valor = kwh * preco
print(f"Total de kWh consumidos: {kwh}.\nValor da conta R$: {valor:.2f}")

