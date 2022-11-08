#Parte 1
def somaImposto(taxaImposto,custo):
    taxaImposto = taxaImposto/100
    custo += custo*taxaImposto
    return custo