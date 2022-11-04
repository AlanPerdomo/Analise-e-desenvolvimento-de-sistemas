#Parte 3 
class ContaCorrente:
    def __init__(self, num_conta, nome, saldo = 0):
        self.num_conta = num_conta
        self.nome = nome
        self.saldo = saldo

    def alteraNome(self, nome):
        self.nome = nome
        return self.nome
    
    def deposito(self, valor_deposito):
        self.saldo += valor_deposito
        return self.saldo
    
    def saque(self, valor_saque):
        self.saldo -= valor_saque
        return self.saldo