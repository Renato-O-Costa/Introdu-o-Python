# Programa 6.7 - Simulando uma fila de banco
# Capítulo 6 - Listas, tuplas, dicionários e conjuntos
# Renato Costa
# 22/04/2025


# Simulando uma fila de banco com lista

ultimo = 10
fila = list(range(1, ultimo + 1))

while True:
    print(f"\nExistem {len(fila)} clientes na fila.")
    print(f"Fila atual:{fila}")
    print("Digite F para adicionar um cliente ao fim da fila.")
    print("ou A para realizar o atendimento.S para sair.")
    operacao = input("Operação (F, A ou S): ").upper().lower()
    if operacao == "A" or operacao == "a":
        if len(fila) > 0:
            atendido = fila.pop(0)
            print(f"Cliente {atendido} atendido.")
        else:
            print("Fila vazia!Ninguém para atender.")
    elif operacao == "F" or operacao == "f":
        ultimo += 1
        fila.append(ultimo)
        print(f"Cliente {ultimo} adicionado à fila.")
    elif operacao == "S" or operacao == "s":
        print("Saindo...")
        break
    else:
        print("Operação inválida!Digite F, A ou S.")