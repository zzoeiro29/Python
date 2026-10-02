def metade (num, formato = False):
    return num / 2 if not formato else moeda(num / 2) # ou if format is False else

def dobro (num, formato = False):
    return num * 2 if not formato else moeda(num * 2)

def aumento (num, taxa, formato = False):
    return (num * taxa/100) + num if formato is False else moeda((num * taxa/100) + num)

def diminuir (num, taxa, formato = False):
    return num - (num * taxa/100) if formato is False else moeda(num - (num * taxa/100))

def moeda (num = 0, moedas = "R$"):
    return f"{moedas}{num:.2f}".replace(".", ",")