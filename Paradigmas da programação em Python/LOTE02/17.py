# 17 Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

area = float(input("Quantos metros quadrados serão pintados? "))
litros = area/6

latas = int(litros/18)
if (litros/18 != int and litros/18 != 1 ):
    latas += 1
custo_lata = latas*80

galao = int(litros/3.6)
if (litros/3.6 != int and litros/3.6 != 1 ):
    galao += 1
custo_galao = galao*25

print("comprando apenas latas de 18l serao necessarias "+str(latas)+" e o preço sera R$"+str(custo_lata))
print("comprando apenas galoes de 3.6l serao necessarios "+str(galao)+" e o preço sera R$"+str(custo_galao))

while(litros/18 >= 1 ):
    print(str(litros)+"litros")
    litros = litros % 18
    latas += 1
print(str(litros)+"litros depois das latas")
print(litros)

while(litros/3.6 >= 1):
    litros = litros % 3.6
    galao +=1
print(galao)
