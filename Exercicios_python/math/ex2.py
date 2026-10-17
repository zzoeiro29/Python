def fibonaci(numero):
    a = 0
    b = 1
    for i in range(numero):
        print(a)
        temp = a + b
        a = b
        b = temp

n = int(input("digite quantos termos quer: "))
fibonaci(n)
