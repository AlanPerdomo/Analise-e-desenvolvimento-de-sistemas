#Parte 2
def valorPagamento(valor_prestacao,atraso):
    valor_real=0
    if(atraso > 0):
        valor_real = valor_prestacao + (valor_prestacao * 0.03) + (valor_prestacao*(atraso * 0.001))
        return valor_real
    else:
        return valor_prestacao

num_prestacoes = 0
total_pago = 0
valor_prestacao = 1
while True:
    valor_prestacao = float(input("informe o valor da prestação: "))
    if(valor_prestacao != 0):
        atraso = int(input("informe quantos dias em atraso: "))
        num_prestacoes += 1 
        total_pago += valorPagamento(valor_prestacao,atraso)
    else:
        break

print(num_prestacoes, "prestaçoes e um total de R$", total_pago)