print("="*10 , "Lojas GUANABARA" , "="*10 )
preco = int(input("Preço das compras: R$"))
print("Formas de pagamento")
print(" [ 1 ] à vista dinheiro/cheque")
print(" [ 2 ] à vista cartao")
print(" [ 3 ] 2x no cartao")
print(" [ 4 ] 3x ou mais no cartao")
opcao = int(input("Qual a opcao: "))
if opcao == 1:
    desconto = preco - (preco * 0.1)
    print("Sua compra de R$ {} vai custar R$ {} no final ".format(preco,desconto))
elif opcao == 2:
    desconto = preco - (preco * 0.05)
    print("Sua compra de R$ {} vai custar R$ {} no final ".format(preco, desconto))
elif opcao == 3:
    parcela = preco / 2
    print("voce parcelou em 2x de {} sem juros".format(parcela))
    print("Sua compra de R$ {} vai custar R$ {} no final ".format(preco, preco))
elif opcao == 4:
    parcela = int(input("Quanto quer parcelar? "))
    juros = preco + (preco * 0.2)
    juros2 = juros / parcela
    print("voce parcelou em {}x com juros de {:.2f} ".format(parcela,juros2))
    print("Sua compra de R$ {} vai custar R$ {} no final ".format(preco, juros))
else:
    print("Escolheu errado otário")