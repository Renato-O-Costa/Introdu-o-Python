# Exercício 6.4 - Usando o método pop() numa lista vazia
# Capítulo 6 - Listas, tuplas, dicionários e conjuntos
# Renato Costa
# 28/04/2025

'''O que acontece quando não verificamos se a lista está vazia antes de chamarmos o método pop?'''

alunos = []
aluno_removido = alunos.pop()
print(f"Alunos removidos: {aluno_removido}")