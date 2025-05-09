# Exercício 6.7 - Lendo exepressões com parênteses
# Capítulo 6 - Listas, tuplas, dicionários e conjuntos
# Renato Costa
# 04/05/2025

'''Enunciado:Faça um programa que leia uma expressão com parênteses. Usando pilhas, verifique se os parênteses foram abertos e fechados na ordem correta.
Exemplo:
(()) OK
()()(()()) OK
()) Erro
Você pode adicionar elementos à pilha sempre que encontrar abre parênteses e desempilhá-la a cada fecha parênteses. Ao desempilhar, verifique se o topo da pilha é um abre parênteses. Se a expressão estiver correta, sua pilha estará vazia no final.'''


# Solicita ao usuário que digite uma sequência de parênteses a validar
# e armazena na variável expressão

expressão = input("Digite a sequência de parênteses a validar:")
x = 0 # Inicializa o índice x para percorrer a expressão
pilha = [] # Inicializa a pilha como uma lista vazia
while x < len(expressão):
    if expressão[x] == "(":
        pilha.append("(")
    if expressão[x] == ")":
        if len(pilha) > 0:
            topo = pilha.pop(-1)
        else:
            pilha.append(")") # Força a mensagem de erro
            break
    x = x + 1
if len(pilha) == 0:
    print("OK")
else:
    print("Erro")


