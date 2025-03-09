# Exercício 4.3 - Verifica qual número é maior e qual o menor

# Solicita três números para o usuário
# num_1 = int(input("Digite o primeiro número:\n"))
# num_2 = int(input("Digite o segundo número:\n"))   Obs. código da primeira solução
# num_3 = int(input("Digite o terceiro número:\n"))
a, b, c = input("Informe três números:\n").split()
a = int(a)
b = int(b)
c = int(c)

# Verificando o maior entre a e b
'''if num_1 > num_2 and num_1 > num_3: 
    maior = num_1
if num_2 > num_1 and num_2 > num_3: Obs. código da primeira solução
    maior = num_2
if num_3 > num_1 and num_3 > num_2:
    maior = num_3'''
maior_ab = (a + b + abs(a - b)) // 2


# Verificando o maior entre maior_ab e c
'''if num_1 < num_2 and num_1 < num_3:
    menor = num_1
if num_2 < num_1 and num_2 < num_3: Obs. código da primeira solução
    menor = num_2
if num_3 < num_1 and num_3 < num_2:
    menor = num_3'''
maior = (maior_ab + c + abs(maior_ab - c)) // 2

# Imprime resultado na tela
print(f"O maior número é {maior}.")


