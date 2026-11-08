def add_binary(a,b):
    soma = a + b
    n = ""
    while soma > 0:
        resto = soma % 2
        n = str(resto) + n
        soma = soma // 2
    return n
print(add_binary(1,1))