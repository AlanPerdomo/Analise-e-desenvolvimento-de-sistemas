# 15 - Ler o raio de um círculo e imprimir o perímetro e a área

import math

raio = float(input("Digite o raio do circulo: "))

print("O perimetro do circulo é "+str(2*math.pi*raio))
print("A área do circulo é "+str(math.pi*raio**2))