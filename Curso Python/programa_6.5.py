n1 = int(input("um valor: "))
n2 = int(input("outro valor: "))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2 # divisao inteira
e = n1 ** n2 #potencia

print("a soma vale {}, o protduto é {} e a divisao {:.1f}".format(s, m, d), end=" ")
print("divisao inteira {} e potencia {}".format(di, e))

# numero de casas decimais :.xf por exemplo: :.3f n,nnn outro :.2f n,nn
# end desquebrar linha contraio \n
#\n serve pra quebrar a linha q nem no c++