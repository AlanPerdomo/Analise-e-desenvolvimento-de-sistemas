#Parte 1
class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
    
    def trocarCor(self,nova_cor):
        self.cor = nova_cor
    
    def mostraCor(self):
        return self.cor