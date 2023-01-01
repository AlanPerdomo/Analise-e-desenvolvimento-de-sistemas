# 18 Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho = float(input("Qual o tamanho do arquivo para download(em MB)? "))
velocidade = float(input("Qual a velocidade do link de internet(em Mbps)? "))/8
tempo = (tamanho/velocidade)/60

print("o tempo aproximado de download é: " + str(tempo) + " minutos." )