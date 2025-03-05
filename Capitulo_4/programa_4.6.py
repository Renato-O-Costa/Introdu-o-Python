# Programa 4.6 - Categoria x preço, usando if/else

import pdb #Módulo de debugger

pdb.set_trace()

categoria = int(input("Digite a categoria do produto:\n"))
if categoria == 1:
    preco = 10
else:
    if categoria == 2:
        preco = 18
    else:
        if categoria == 3:
            preco = 23
        else:
            if categoria == 4:
                preco = 26
            else:
                if categoria == 5:
                    preco = 31
                else:
                    print("Categoria inválida, digite um valor entre 1 e 5!")
                    preco = 0
                    
print(f"O preço do produto é:\nR${preco:5.2f}.")                    
