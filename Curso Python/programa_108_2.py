def metade (num):
    return num / 2

def dobro (num):
    return num * 2

def aumento (num, taxa):
    return (num * taxa/100) + num

def moeda (num = 0, moedas = "R$"):
    return f"{moedas}{num:.2f}".replace(".", ",")