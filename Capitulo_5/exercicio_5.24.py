# Exercício 5.24 - Imprimindo números primos
# Capítulo
# Renato Costa
# 06/04/2025

qtd_de_primos = int(input("Digite a quantidade de primos a gerar:\n"))
# Valida o número fornecido
if qtd_de_primos < 0:
    print("Número inválido. Digite apenas valores positivos.")
else:
    if qtd_de_primos >= 1:
        print("2")
# Variáveis de controle
    primos_gerados = 1 # Começa a partir do um, devido o número dois ja ser contabilizado
    proximo_primo = 3
# Loop principal
    while primos_gerados < qtd_de_primos:
        divisor = 3
# Loop aninhado verifica os próximos números primos
        while divisor < proximo_primo:
            if proximo_primo % divisor == 0:
                break
            divisor += 2
        if divisor == proximo_primo:
            print(proximo_primo)
            primos_gerados += 1
        proximo_primo += 2
