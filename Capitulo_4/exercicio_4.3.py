# Exercício 4.3 - Verifica qual número é maior e qual o menor

# Solicita três números para o usuário
num_1 = int(input("Digite o primeiro número:\n"))
num_2 = int(input("Digite o segundo número:\n"))
num_3 = int(input("Digite o terceiro número:\n"))

# Verificando o maior
if num_1 > num_2 and num_1 > num_3:
    maior = num_1
if num_2 > num_1 and num_2 > num_3:
    maior = num_2
if num_3 > num_1 and num_3 > num_2:
    maior = num_3

# Verificando o menor
if num_1 < num_2 and num_1 < num_3:
    menor = num_1
if num_2 < num_1 and num_2 < num_3:
    menor = num_2
if num_3 < num_1 and num_3 < num_2:
    menor = num_3

# Imprime resultado na tela
print(f"O maior número é {maior} e o menor número é {menor}.")


