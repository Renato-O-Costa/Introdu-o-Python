# Contadores no Python

fim = int(input("Digite o último número a ser impresso:\n"))
x = 1 # Variável contadora
while x <= fim:
    print(x, end=", " if x < fim else "\n")  #operador ternário que verifica se acrescenta ou não o separador
    x += 1 # Incrementa mais 1 à variável contadora
print("Fim do loop!")
