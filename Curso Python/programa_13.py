x = float(input("Qual é o salario do funcionario: R$"))
s = x + (x*15/100)
print("Um funcionario que ganhava R$ {}, com 15% de aumento, passsa a receber R$ {:.2f}".format(x,s))