#Parte 4
nota_total=0
qtd_nota=0
while(True):
    nota=float(input("Qual o valor da "+str(qtd_nota + 1)+"ª nota? "))
    if(nota>=0):
        qtd_nota+=1
        nota_total+=nota
    else:
        break
print("A media das notas foi ",(nota_total/qtd_nota))

        