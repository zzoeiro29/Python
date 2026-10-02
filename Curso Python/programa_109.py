import programa_109_2
n = int(input("Digite um preço: R$"))
print(f"A metade de {programa_109_2.moeda(n)} é {programa_109_2.metade(n, True)}")
print(f"O dobro de {programa_109_2.moeda(n)} é {programa_109_2.dobro(n, True)}")
print(f"Aumentando 10%, temos {programa_109_2.aumento(n, 10, True)}")
print(f"Reduzindo 13%, temos {programa_109_2.diminuir(n, 13, True)}")