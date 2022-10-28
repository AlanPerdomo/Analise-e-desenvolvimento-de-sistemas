#parte 1
#pop_a = 80000
#taxa_a = 0.03
#pop_b = 200000
#taxa_b = 0.015
#anos = 0
#while(pop_a < pop_b):
#    pop_a += (pop_a * taxa_a)
#    pop_b += (pop_b * taxa_b)
#    anos += 1

#print("vai demorar ",anos," anos para a população A se igualar ou ultrapassar a população B.")


#parte 2 
def compara_pop():
    pop_a = int(input("Qual a o população do pais A? ->"))
    taxa_a = float(input("Qual é a taxa de crecimento da população A? ->"))

    pop_b = int(input("Qual a o população do pais B? ->"))
    taxa_b = float(input("Qual é a taxa de crecimento da população B? ->"))
    anos = 0
    while(pop_a < pop_b):
        pop_a += (pop_a * (taxa_a/100))
        pop_b += (pop_b * (taxa_b/100))
        anos += 1
    print("vai demorar ",anos," anos para a população A se igualar ou ultrapassar a população B.")
    repetição = input("Deseja repetir a operação?(Y/N) ")
    if(repetição == "y" or "Y"):
        compara_pop()

start=input("deseja iniciar o comparador?(y/n) ")
print(start)
if(start == "y" or "Y"):
    compara_pop()
else:
    print("ok")