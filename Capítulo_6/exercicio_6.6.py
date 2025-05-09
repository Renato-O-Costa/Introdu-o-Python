# Exercício 6.6 - Simulando uma fila de banco, com duas filas de clientes
# Capítulo 6 - Listas, tuplas, dicionários e conjuntos
# Renato Costa
# 28/04/2025

'''Modifique o programa para trabalhar com duas filas. Para facilitar seu trabalho, considere o comando A
para atendimento da fila 1; e B, para atendimento da fila 2. O mesmo para a chegada de clientes: F para
fila 1; e G, para fila 2.'''

# Variáveis globais (1-normal e 2-listas)
ultimo = 0
fila1 = []
fila2 = []
while True:
    print(f"\nExistem {len(fila1)} clientes na fila 1 e {len(fila2)} clientes na fila 2.")
    print("Fila 1 atual:", fila1)
    print("Fila 2 atual:", fila2)
    print("Digite F para adicionar um cliente ao fim da fila 1 (ou G para fila 2),")
    print("ou A para realizar o atendimento da fila 1 (ou B para fila 2). S para sair.")
    operacao = input("Operação (F, G, A, B ou S):").upper()
    x = 0 # Variável de controle do próximo loop
    sair = False
    while x < len(operacao):
        if operacao[x] == "A" or operacao[x] == "F":
            fila = fila1
        else:
            fila = fila2
        if operacao[x] == "A" or operacao[x] == "B":
            if len(fila) > 0:
                atendido = fila.pop(0) # Remove o primeiro cliente da fila
                print(f"Cliente {atendido} atendido.")
            else:
                print("Fila vazia! Ninguém para atender.")
        elif operacao[x] == "F" or operacao[x] == "G":
            ultimo += 1  # Incrementa o ticket do novo cliente
            fila.append(ultimo)
        elif operacao[x] == "S":
            sair = True
            break
        else:
            print(f"Operação inválida: {operacao[x]} na posição {x}! Digite apenas F, G, A, B ou S!")
        x = x + 1
    if sair:
        break
# Fim do programa