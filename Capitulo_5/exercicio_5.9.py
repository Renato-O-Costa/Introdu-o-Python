# Exercício 5.9 - Executa a divisão de um número pela subtração
# Capítulo 5
# Renato Costa
# 11/03/2025

# Recebendo os valores
dividendo = int(input("Informe o dividendo: "))
divisor = int(input("Informe o divisor: "))
# Variáveis de controle
quociente = 0
x = dividendo
# Repetição while
while x >= divisor:
    x = x - divisor
    quociente = quociente + 1
resto = x
print(f"{dividendo} / {divisor} = {quociente} (quociente) {resto} (resto)")
