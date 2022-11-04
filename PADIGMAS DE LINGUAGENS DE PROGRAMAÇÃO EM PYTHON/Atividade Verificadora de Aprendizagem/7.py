def calcular():
    class Calculadora:
        def __init__(self,primeiroOperando, segundoOperando):
            self.primeiroOperando = primeiroOperando
            self.segundoOperando = segundoOperando
        
        def adicao(self):
            return (primeiroOperando + segundoOperando)

        def subtracao(self):
            return (primeiroOperando - segundoOperando)
    
        def multiplicacao(self):
            return (primeiroOperando * segundoOperando)

        def divisao(self):
            return (primeiroOperando / segundoOperando)
        
    primeiroOperando = float(input("primeiro operando: "))
    segundoOperando = float(input("segundo operando: "))
    conta1 = Calculadora(primeiroOperando, segundoOperando)
    operador = input("Selecione a operação desejada: \n( + para adição  - para subtração  * para multiplicação  / para divisão) ")
    
    if (operador == "+"):
        print(conta1.adicao())
    if (operador == "-"):
        print(conta1.subtracao())
    if (operador == "*"):
        print(conta1.multiplicacao())
    if (operador == "/"):
        print(conta1.divisao())

calcular()