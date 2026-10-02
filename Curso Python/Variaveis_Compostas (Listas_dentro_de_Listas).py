"""
teste = list()
teste.append("gustavo")
teste.append(40)
galera = list()
galera.append(teste[:]) # copia [:]
teste[0] = "maria"
teste[1] = 22-
galera.append(teste[:])
print(galera)
"""

"""
galera = [["joao" , 19] , ["Ana" , 13] , ["joaquim" , 14]  , ["Maria" , 45]  ]
#print(galera[2][1])
for p in galera:
    print(f"{p[0]} tem {p[1]} anos")
"""

galera = list()
dado = list()
totalmai = totalmen = 0
for c in range(0, 3):
    dado.append(str(input("Nome:")))
    dado.append(int(input("Idade:")))
    galera.append(dado[:]) # copia se nao eles ficam inteligados as listas
    dado.clear() # limpa a lista

for p in galera:
    if p[1] >= 21:
        print(f"{p[0] } é maior que idade")
        totalmai += 1
    else:
        print(f"{p[0]} é menor que idade")
        totalmen += 1
print(f"Temos {totalmai} maiores de idade e {totalmen} menores de idade")