# Exercício 6.8 - Pesquisa sequencial modificado
# Capítulo 6 - Listas, tuplas, dicionários e conjuntos
# Autor: [Renato Costa]
# Data: [08/05/2025]

'''Enunciado: Modifique o primeiro exemplo (Programa 6.9) de forma a realizar a mesma tarefa, mas sem utilizar a variável achou. Dica: observe a condição de saída do while.'''

L = [15, 8, 23, 41, 35, 19]
p = int(input('Digite o valor a ser pesquisado:\n'))
i = 0
while i < len(L):
    if L[i] == p:
        break
    i += 1
if i < len(L):
    print(f'{p}encontrado na posição {i}.')
else:
    print(f'{p} não encontrado.')
# O código foi modificado para não utilizar a variável 'achou'. A condição de saída do loop while agora verifica se o índice 'i' é menor que o comprimento da lista e se o elemento na posição 'i' é diferente do valor pesquisado. Se o valor for encontrado, o loop é interrompido com 'break'. Após o loop, uma verificação é feita para determinar se o valor foi encontrado ou não, com base no índice 'i'.    
