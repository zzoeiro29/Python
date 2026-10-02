casa = float(input("Digite o valor da casa que quer comprar: R$ "))
salario = float(input("Digite o valor do salario do comprador: R$"))
anos = int(input("Digite quantos anos vai precisar: "))
prestacao = casa / (anos * 12)
print("Para pagar uma casa de R${} em {} anos a prestacao sera de R${:.2f} reais".format(casa, anos, prestacao))
if (salario * 0.30) * (anos * 12) >= casa:
    print("gg, o emprestimo foi aceito")
else:
    print("\033[31mse fudeu o emprestimo foi negado")