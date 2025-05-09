# Tabuada com repetições aninhadas

'''tabuada = 1
while tabuada <= 10:
    numero = 1
    while numero <= 10:
        print(f"{tabuada} x {numero} = {tabuada * numero}")
        numero += 1
    tabuada += 1
    print("-" * 15)
print("Tabuada finalizada!")'''

# Tabuada sem repetições aninhadas

tabuada = 1
numero = 1
while tabuada <= 10:
    print(f"{tabuada} x {numero} = {tabuada * numero}")
    numero += 1
    if numero == 11:
        numero = 1
        tabuada += 1
        print("-" * 15)
