#Parte 1
pop_a = 80000
taxa_a = 0.03
pop_b = 200000
taxa_b = 0.015
anos = 0
while(pop_a < pop_b):
    pop_a += (pop_a * taxa_a)
    pop_b += (pop_b * taxa_b)
    anos += 1
 
print("vai demorar ",anos," anos para a população A se igualar ou ultrapassar a população B.")