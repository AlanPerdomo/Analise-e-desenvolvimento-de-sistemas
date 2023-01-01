# 20 - Ler um número e imprimir a tabuada de 0 a 10 daquele número

num = float(input("digite um numero: "))
for x in range(11):
    print(str(num)+" * "+ str(x)+" = "+str(num*x))