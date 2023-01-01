import math 

tam = float(input("Digite o tamanho(em M²) da área que será pintada: ")) 

quantpm = 1/3 

tamt = tam * quantpm 

l18q = math.ceil(tamt/18) 

l18p = round(float(l18q*80), 2) 

print("Comprando apenas latas de 18 litros, é preciso comprar " + str(l18q) + " lata(s), no preço de " + str(l18p) + "R$.") 