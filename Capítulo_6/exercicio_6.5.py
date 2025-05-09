# Exercício 6.4 - Simulando uma fila de banco
# Capítulo 6 - Listas, tuplas, dicionários e conjuntos
# Renato Costa
# 28/04/2025

'''Enunciado: Altere o Programa 6.7 de forma a poder trabalhar com vários comandos digitados de uma só vez.
Atualmente, apenas um comando pode ser inserido por vez. Altere-o de forma a considerar operação
como uma string.
Exemplo: FFFAAAS significaria três chegadas de novos clientes, três atendimentos e, finalmente, a'''

# Simulando uma fila de banco com lista

último = 10
fila = list(range(1, último + 1))
while True:
    print(f"\nExistem {len(fila)} clientes na fila")
    print("Fila atual:", fila)
    print("Digite F para adicionar um cliente ao fim da fila,")
    print("ou A para realizar o atendimento. S para sair.")
    operação = input("Operação (F, A ou S):")
    x = 0
    sair = False
    while x < len(operação):
        if operação[x] == "A" or operação[x] == "a":
            if len(fila) > 0:
                atendido = fila.pop(0) # Remove o primeiro cliente da fila
                print(f"Cliente {atendido} atendido")
            else:
                print("Fila vazia! Ninguém para atender.")
        elif operação[x] == "F" or operação[x] == "f":
            último += 1  # Incrementa o ticket do novo cliente
            fila.append(último)
        elif operação[x] == "S" or operação[x] == "s":
            sair = True
            break
        else:
            print(f"Operação inválida: {operação[x]} na posição {x}! Digite apenas F, A ou S!")
        x = x + 1
    if sair:
        break