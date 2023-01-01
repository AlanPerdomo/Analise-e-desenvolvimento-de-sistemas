#Parte 5
qtd_temp=0
temp_total=0
temp_atual=10
temp_max=0
temp_min=10000
while(True):
    temp_atual = float(input( str(qtd_temp + 1)+"ª temperatura: "))
    if(temp_atual > 0):
        qtd_temp += 1
        temp_total += temp_atual
        if(temp_atual > temp_max):
            temp_max = temp_atual
        if(temp_atual < temp_min):
            temp_min = temp_atual
    else:
        break

print(
    "Temperatura máxima = ",temp_max,
    "\nTemperatura mínima = ",temp_min,
    "\nTemperatura média = ",(temp_total/qtd_temp)
)