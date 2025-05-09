# par = []
# impar = []

# # Solicita ao usuário que digite números inteiros até que ele digite 0
# while True:
#     try:
#         numero = int(input("Digite um número (ou 0 para encerrar):\n"))
#         if numero == 0: # Interrompe o loop se o usuário digitar 0
#             print("Encerrando o programa...")
#             break
#         if numero % 2 == 0: # Verifica se o número é par ou ímpar
#             par.append(numero)
#         else:
#             impar.append(numero)
#     except ValueError:
#         print("Valor inválido. Por favor, digite um número inteiro.")

# total_digitados = len(par) + len(impar)

# # Exibe mensagem mostrando quantidade de números pares e ímpares digitados
# print(f"Você digitou {total_digitados} números, sendo {len(par)} pares e {len(impar)} ímpares.")
# # Lista os números pares e ímpares digitados
# print("Números digitados:")
# print(f"Pares: {sorted(par)}")
# print(f"Ímpares: {sorted(impar)}")


'''Enunciado: Simule uma fila de atendimento onde os clientes são atendidos por ordem de chegada.'''

# atendimento_normal = list()
# atendimento_prioritario = list()

# while True:
    
#     opcao = input("Digite N para atendimento normal ou P para atendimento preferencial, (ou S  para sair):\n").upper()
#     if opcao == "S":
#         break
#     elif opcao == "N":
#         cliente = input("Digite o nome do cliente:\n")
#         atendimento_normal.append(cliente) # Adiciona o cliente na fila normal
#     elif opcao == "P":
#         cliente = input("Digite o nome do cliente:\n")
#         atendimento_prioritario.append(cliente)
#     else:
#         print("Opção inválida! Digite apenas N, P ou S!")
#         continue 
    
# print(f"Existem {len(atendimento_normal)} clientes no atendimento normal.")
# print(f"Relação de clientes no atendimento normal: {atendimento_normal}.")
# print(f"Existem {len(atendimento_prioritario)} clientes no atendimento preferencial.")
# print(f"Relação de clientes no atendimento preferencial: {atendimento_prioritario}.")


'''Crie um programa que simula uma fila de impressão. Cada documento na fila será representada por uma string com o nome do arquivo.'''

# fila_impressao = list()   

# while True:
#     documento = input("Digite o nome do arquivo para impressão (ou 'F' para finalizar):\n")
#     if documento == "F" or documento == "f": # Interrompe o loop se o usuário digitar 'F' ou 'f'
#         print("Encerrando o programa...")
#         break
#     else:
#         fila_impressao.append(documento) # Adiciona o documento na fila de impressão

# while fila_impressao: # Enquanto houver documentos na fila
#     print(f"Imprimindo: {fila_impressao[0]}") # Imprime o primeiro documento da fila
#     fila_impressao.pop(0) # Remove o documento da fila após a impressão
#     print(f"Fila de impressão: {fila_impressao}\n") # Exibe a fila de impressão atualizada


# # Exibe mensagem informando que todos os documentos foram impressos e a fila está vazia
# print("Todos os documentos foram impressos.")
# print("Fila de impressão vazia.")
    
'''Enunciado: Escreva um programa que leia uma sequência de colchetes ([ e ]) digitada pelo usuário e diga se ela está balanceada, usando uma pilha.'''
'''Exemplo de entrada e saída:

Digite a sequência de colchetes a validar: [[][]]
OK
Digite a sequência de colchetes a validar: [[[]]
Erro'''

expressao = input("Digite a sequência de colchetes a validar:")
x = 0 # Inicializa o índice x para percorrer a expressão
pilha = [] # Inicializa a pilha como uma lista vazia
while x < len(expressao):
    if expressao[x] == "[":
        pilha.append("[")
    if expressao[x] == "]":
        if len(pilha) > 0:
            topo = pilha.pop(-1)
        else:
            pilha.append("]") # Força a mensagem de erro
            break
    x = x + 1
if len(pilha) == 0:
    print("OK")
else:
    print("Erro")

