# 17 - Ler três números e imprimir se o primeiro é maior ou menor que a soma dos outros dois

num1 = float(input("Digite o 1º numero: "))
num2 = float(input("Digite o 2º numero: "))
num3 = float(input("Digite o 3º numero: "))

if num1 > (num2+num3):
    print(str(num1)+" é maior que a soma de "+str(num2)+" e "+str(num3))
else:
    print(str(num1)+" é menor que a soma de "+str(num2)+" e "+str(num3))