# Programa 6.9 - Pesquisa sequencial
# Capítulo 6 - Listas, tuplas, dicionários e conjuntos
# Renato Costa
# 08/05/2025

L = [23, 68, 54, 12, 33]
p = int(input('Digite o valor a procurar:\n')) # Solicita o valor a procurar
achou = False # Inicializa a variável achou como False
x = 0 # Inicializa o índice x como 0
print('Iniciando a pesquisa...')

while x < len(L): # Enquanto x for menor que o tamanho da lista L
    print(f'Analisando o elemento {L[x]} na posição {x}.')
    if L[x] == p:
        achou = True
        break
    x += 1
if achou:
    print("Match!")
    print(f'Valor {p} encontrado na posição {x}.')
else:
    print(f'Valor {p} não encontrado.')
    
print('Fim da pesquisa.')