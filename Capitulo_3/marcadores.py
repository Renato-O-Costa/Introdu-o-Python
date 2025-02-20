# Usando marcadores em Python

nome = "João Vítor"
idade = 28
saldo = 235

# Marcador %

print("O cliente %s tem %d anos de idade, e seu saldo atual é de R$ %5.2f.\n" % (nome, idade, saldo))
print("O cliente %12s tem %03d anos de idade, e seu saldo atual é de R$ %5.2f.\n" % (nome, idade, saldo))

# Usando o método .format

print("{} tem {} anos de idade e seu saldo é de R$ {:5.2f}\n".format(nome, idade, saldo))
print("{:12} tem {:3} anos de idade e seu saldo é de R$ {:5.2f}.".format(nome, idade, saldo))

# Usando f Strings

print(f"{nome:<12s} tem {idade:<3} anos de idade e seu saldo atual é de R$ {saldo:5.2f}.")
