# 13 Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas:
#    A) Para homens: (72.7*h) - 58
#    B) Para mulheres: (62.1*h) - 44.7

altura = float(input("Informe a sua altura: "))
print("O peso ideal para Homens é "+str((72.7*altura)-58)+" e para Mulheres é "+str((62.1*altura)-44.7))