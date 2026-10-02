import programa_108_2
n = int(input("Digite um preço: R$"))
print(f"A metade de {programa_108_2.moeda(n)} é {programa_108_2.moeda(programa_108_2.metade(n))}")
print(f"O dobro de {programa_108_2.moeda(n)} é {programa_108_2.moeda(programa_108_2.dobro(n))}")
print(f"Aumentando 10%, temos {programa_108_2.moeda(programa_108_2.aumento(n, 10))}")