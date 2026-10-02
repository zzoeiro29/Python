"""  Versao string

x = str(input("Digite um numero:"))
print("Analisando o numero: " , x)
print("Unidade: ", x[3])
print("dezena: ", x[2])
print("centena: ", x[1])
print("milhar: ", x[0])

"""
# outra versao matematica

x = int(input("Digite um numero:"))
u = x // 1 % 10
d = x // 10 % 10
c = x // 100 % 10
m = x // 1000 % 10
print("Analisando o numero: " , x)
print("Unidade: ", u)
print("dezena: ", d)
print("centena: ", c)
print("milhar: ", m)
