# 14 - Ler dois números que representam os lados de um retângulo, imprima o perímetro e a área

lado1 = float(input("Digite o tamanho de um lado do retângulo: "))
lado2 = float(input("Digite o tamanho do outro lado do retângulo: "))

print("O perimetro do retangulo é "+str(lado1*2+lado2*2))
print("A área do retangulo é "+str(lado1*lado2))