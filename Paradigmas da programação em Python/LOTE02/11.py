# 11 Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#    A) o produto do dobro do primeiro com metade do segundo .
#    B) a soma do triplo do primeiro com o terceiro.
#    C) o terceiro elevado ao cubo.

num1 = int(input("Digite o primeiro numero inteiro: "))
num2 = int(input("Digite o segundo numero inteiro: "))
num3 = float(input("Digite um numero real: "))

print((num1*2)*(num2/2))
print((num1*3)+num3)
print(num3**3)