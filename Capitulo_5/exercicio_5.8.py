# Programa que recebe dois números e faz a multiplição pela soma

num_1 = int(input("Informe o primeiro número:\n"))
num_2 = int(input("Informe o segundo número:\n"))
resultado = 0
x = 1

while x <= num_2:
    resultado += num_1
    x += 1
print(f"{num_1} x {num_2} = {resultado}")
    

