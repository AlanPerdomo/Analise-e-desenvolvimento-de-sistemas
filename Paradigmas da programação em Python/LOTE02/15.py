# 15 Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#    A) salário bruto.
#    B) quanto pagou ao INSS.
#    C) quanto pagou ao sindicato.
#    D) o salário líquido.
#    E) calcule os descontos e o salário líquido, conforme a tabela abaixo:
#        + Salário Bruto : R$
#        - IR (11%) : R$
#        - INSS (8%) : R$
#        - Sindicato ( 5%) : R$
#        = Salário Liquido : R$
#        Obs.: Salário Bruto - Descontos = Salário Líquido.

salario = float(input("Quanto você ganha por hora? "))
horas = float(input("Quantas horas você trabalhou neste mês? "))
salario_bruto = salario*horas
ir=salario_bruto*0.11
inss = salario_bruto*0.08
sindicato = salario_bruto*0.05
salario_liquido = salario_bruto-(inss+sindicato+ir)

print("A) O salario bruto foi de R$"+str(salario_bruto))
print("B) Foram pagos R$"+str(inss)+" ao INSS.")
print("C) Foram pagos R$"+str(sindicato)+" ao Sindicato.")
print("D) O salario líquido é R$"+ str(salario_liquido))
print("E)\t+ Salário Bruto : R$"+str(salario_bruto)+"\n\t- IR (11%) : R$"+str(ir)+"\n\t- INSS (8%) : R$"+str(inss)+"\n\t- Sindicato ( 5%) : R$"+str(sindicato)+"\n\t= Salário Liquido : R$"+str(salario_liquido))