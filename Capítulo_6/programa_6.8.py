# Programa que simula uma pilha de pratos
# LIFO - Last in First Out (último a entrar, primeiro a sair)
# A pilha é uma estrutura de dados onde o último elemento adicionado é o primeiro a ser removido.   

prato = 5
pilha = list(range(1, prato + 1)) # Cria uma pilha de pratos numerados de 1 a 5
while True:
    print(f"\nExistem {len(pilha)} pratos na pilha.")
    print(f"Pratos na pilha: {pilha}")
    print("Digite E para empilhar um novo prato, ")
    print("D para desempilhar um prato ou S para sair.")
    opcao = input("Opção (E, D ou S):\n")
    if opcao == "E" or opcao == "e":
        prato += 1
        pilha.append(prato) # Adiciona um novo prato à pilha
    elif opcao == "D" or opcao == "d":
        if len(pilha) > 0:
            lavado = pilha.pop(-1) # Remove o último prato da pilha
            print(f"Prato {lavado} foi lavado.")
        else:
            print("Pilha vazia. Nada para lavar.")
    elif opcao == "S" or opcao == "s":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida! Digite apenas E, D ou S!")
        continue