print("-" * 25)
print("Sequencia de fibonacci")
print("-" * 25)
n_termos = int(input("Quantos termos voce quer mostrar? "))
t1 = 0
t2 = 1
cont = 3
print("{} -> {}".format(t1,t2), end= "")
while cont <= n_termos:
    t3 = t1 + t2
    print(" -> {} ".format(t3), end="")
    t1 = t2
    t2 = t3
    cont += 1
print(" -> FIM")
