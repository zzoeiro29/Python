from time import sleep
x = int(input(" insira um numero "))
y = int(input(" insira outro numero: "))
opcao = True # ou opcao = 0
while opcao: # ou opcao != 5
    print(" [1] somar")
    print(" [2] multiplicar")
    print(" [3] maior")
    print(" [4] novos numeros")
    print(" [5] sair do programa")
    n_opcao = int(input("Qual a sua opcao: "))
    if n_opcao == 1:
        soma = x + y
        print(soma)
        sleep(1)
    elif n_opcao == 2:
        multi = x * y
        print(multi)
        sleep(1)
    elif n_opcao == 3:
        if x > y:
            print("{} é o maior".format(x))
        elif x < y:
            print("{} é o maior".format(y))
        else:
            print("Sao iguais")
        sleep(1)
    elif n_opcao == 4:
        x = int(input("insira um numero: "))
        y = int(input("insira outro numero: "))
    elif n_opcao == 5:
        opcao = False
    else:
        opcao = False
        print("voce é burro?")
    print("-=-" * 10)


