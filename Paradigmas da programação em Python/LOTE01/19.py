# 19 - Ler três números que representam os coeficientes de uma equação do segundo grau,imprima as raízes dessa equação

import math

a = float(input("digita o valor de a"))
b = float(input("digita o valor de b"))
c = float(input("digita o valor de c"))


delta = (b ** 2) -4 *a *c

x1 = (-b + math.sqrt(delta)) / (2*a) #Raiz no mesmo esquema que anteriormente, também é possível importar a biblioteca math.
x2 = (-b - math.sqrt(delta)) / (2*a)

print("x1:",x1,"\nx2:",x2)