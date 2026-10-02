salario = int(input("Qual o salário? R$"))
if salario >= 1250:
    salario2 = salario + (salario * 0.10) #10% de aumento
else:
    salario2 = salario + (salario * 0.15) #15% de aumento
print("Quem ganhava R${:.2f} passa a ganhar R${:.2f}".format(salario, salario2))