def metade (num, formato = False):
    return num / 2 if not formato else moeda(num / 2) # ou if format is False else

def dobro (num, formato = False):
    return num * 2 if not formato else moeda(num * 2)

def aumentos (num, taxa, formato = False):
    return (num * taxa/100) + num if formato is False else moeda((num * taxa/100) + num)

def diminuir (num, taxa, formato = False):
    return num - (num * taxa/100) if formato is False else moeda(num - (num * taxa/100))

def resumo( preco, aumento, reducao):
    print("-" * 30)
    print("RESUMO DO VALOR".center(30))
    print("-" * 30)
    print(f"Preço analisado: \t{moeda(preco)}") # \t -> organizar valor
    print(f"Dobro do preço:  \t{moeda(dobro(preco))}")
    print(f"Metade do preço: \t{moeda(metade(preco))}")
    print(f"{aumento} de aumento:  \t{moeda(aumentos(preco, aumento))}")
    print(f"{reducao} de reduçao:   \t{moeda(diminuir(preco, reducao))}")
    print("-" * 30)

def moeda (num = 0 , moeda = "R$"):
    return f"{moeda}{num:.2f}".replace(".", ",")