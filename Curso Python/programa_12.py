x = float(input("Qual o preço do produto? R$ "))
t = x - (x * 0.05) # ou x - (x*5/100)
print("O produto que custava {}, na promoçao com desconto de 5% vai custar R${:.2f}".format(x, t))