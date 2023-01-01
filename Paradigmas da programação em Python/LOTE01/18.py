# 18 - Ler dois números e se o segundo for diferente de zero imprimir a divisão, se for igual a zero imprimir uma mensagem indicando erro.

num1 = float(input("Digite um valor: "))
num2 = float(input("Digite outro valor: "))
if num2 == 0:
    print("Erro!")
else:
    print(str(num1)+" / "+str(num2)+" = "+str(num1/num2))