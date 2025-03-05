# Calculando áreas diversas

a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)
pi = 3.14159
triangulo = a * c / 2
circulo = pi * c ** 2
trapezio = (a + b) * c / 2
quadrado = b ** 2
retangulo = a * b

print(f"Triângulo: {triangulo:.3f}")
print(f"Círculo: {circulo:.3f}")
print(f"Trapézio: {trapezio:.3f}")
print(f"Quadrado: {quadrado:.3f}")
print(f"Retângulo: {retangulo:.3f}")
