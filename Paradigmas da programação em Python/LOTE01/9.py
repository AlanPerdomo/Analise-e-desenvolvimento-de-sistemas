# 9 - Ler dois números que representam os valores dos catetos de um triângulo retângulo e imprimir o valor da hipotenusa (a2 = b2 + c2)

import math

num1 = float(input("Digite o valor do 1º cateto: "))
num2 = float(input("Digite o valor do 2º cateto: "))
num3 = num1**2 + num2**2
hipotenusa = math.sqrt(num3) 
print("O valor da hipotenusa é "+str(hipotenusa))