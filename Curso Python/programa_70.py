print("-"*20)
print("LOJA SUPER BARATAO")
print("-"*20)
total_compra = cont_1000 = menor = cont = 0
barato = " "
while True:
    nome = str(input("Nome produto: "))
    preco = float(input("Preço: R$"))
    cont += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome
    res = " "
    total_compra += preco
    if preco > 1000:
        cont_1000 += 1
    while res not in "SN":
        res = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if res in "N":
        break
print("{:-^40}".format("FIM DO PROGRAMA"))
print(f"O total da compra foi de R${total_compra:.2f}")
print(f"Temos {cont_1000} produtos que custam mais de 1000 reais")
print(f"O produto mais barato foi o {barato} que custa R${menor}")