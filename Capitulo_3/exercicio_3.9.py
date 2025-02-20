# Conversor de tempo

dias = int(input("Informe a quantidade de dias:\n"))
horas = int(input("Informe a quantidade de horas:\n"))
minutos = int(input("Informe os minutos:\n"))
segundos = int(input("Informe os segundos:\n"))

total_segundos = (dias * 24 * 60 * 60) + (horas * 60 * 60) + minutos * 60 + segundos

print(f"Total de segundos do tempo informado: {total_segundos:5.2f}")
