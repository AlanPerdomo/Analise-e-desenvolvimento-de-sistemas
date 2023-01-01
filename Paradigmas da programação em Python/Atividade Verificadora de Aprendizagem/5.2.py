#Parte 2 
def compara_pop():
    pop_a = int(input("Qual a população do país A? ->"))
    taxa_a = float(input("Qual é a taxa de crescimento da população A? ->"))
    pop_b = int(input("Qual a população do país B? ->"))
    taxa_b = float(input("Qual é a taxa de crescimento da população B? ->"))
    print("População A = ",pop_a," habitantes com taxa de crescimento de ",taxa_a,"% por ano.")
    print("População B = ",pop_b," habitantes com taxa de crescimento de ",taxa_b,"% por ano.")
    
    anos = 0   
    while(pop_a < pop_b):
        pop_a += (pop_a * (taxa_a/100))
        pop_b += (pop_b * (taxa_b/100))
        anos += 1
    print("vai demorar ",anos," anos para a população A se igualar ou ultrapassar a população B.")
    repeticao = input("Deseja repetir a operação?(Y/N) ")
    if(repeticao == "y" or repeticao == "Y"):
        compara_pop()

compara_pop()