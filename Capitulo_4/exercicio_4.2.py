# Verifica velocidade  do carro, e caso haja excesso aplica multa

velocidade = int(input("Informe a velocidade em Km/h do carro:\n"))
if velocidade > 80:
    multa = (velocidade - 80) * 5
    print(f"{velocidade} Km/h. Você foi multado. Valor da multa R$ {multa:5.2f}.")
