#Parte 2
class Retângulo:
    def __init__(self, LadoA, LadoB):
        self.LadoA = LadoA
        self.LadoB = LadoB
    
    def mudaValorLados(self,novo_LadoA,novo_LadoB):
        self.LadoA = novo_LadoA
        self.LadoB = novo_LadoB

    def mostraValorLados(self):
        return self.LadoA, self.LadoB
    
    def calcArea(self):
        return self.LadoA * self.LadoB

    def calcPerimetro(self):
        return self.LadoA * 2 + self.LadoB * 2

def prog():
    LadoA = float(input("informe o tamanho do lado A: "))
    LadoB = float(input("informe o tamanho do lado A: "))
    retangulo1 = Retângulo(LadoA,LadoB)
    print("Area = ", retangulo1.calcArea())
    print("perimetro = ", retangulo1.calcPerimetro())

prog()