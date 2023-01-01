# 5 - Ler dois números e uma String com um operador e imprimir o resultado da operação

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operador = str(input("Qual operação deseja fazer? ( + = Soma, - = Subtração , / = Divisão , * = Multiplicação )"))

if operador == "+":
    print(str(num1) + " + " + str(num2) + " = " + str(num1 + num2))
if operador == "-":
    print(str(num1) + " - " + str(num2) + " = " + str(num1 - num2))
if operador == "/":
    print(str(num1) + " / " + str(num2) + " = " + str(num1 / num2))
if operador == "*":
    print(str(num1) + " * " + str(num2) + " = " + str(num1 * num2))