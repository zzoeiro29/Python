num = int(input("Digite um numero inteiro: "))
primo = num > 1
for i in range(2, num):
    if num % i == 0:
        primo = False
if primo:
    print("é um numero primo")
else:
    print("nao é um numero primo")



