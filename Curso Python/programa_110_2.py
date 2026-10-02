def resumo( preco, aumento, reducao):
    print("-" * 30)
    print("RESUMO DO VALOR".center(30))
    print("-" * 30)
    print(f"Preço analisado: \t{moeda(preco)}") # \t -> organizar valor
    print(f"Dobro do preço:  \t{moeda(preco * 2)}")
    print(f"Metade do preço: \t{moeda(preco/2)}")
    print(f"{aumento} de aumento:  \t{moeda(preco + preco * (aumento/100))}")
    print(f"{reducao} de reduçao:   \t{moeda(preco - preco * (reducao / 100))}")
    print("-" * 30)

def moeda (num = 0 , moeda = "R$"):
    return f"{moeda}{num:.2f}".replace(".", ",")