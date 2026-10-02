# listas = []
# tuplas = ()
# dicionarios = {}
#  Listas sao variaveis compostas que podem ser mudadas (mutaveis) diferente das tuplas
num = [2,5,9,1]
num[2] = 3
#num4[4] = 7 nao da
num.append(7) # .append = adiciona no final
#num.sort() # .sort = organiza a lista por ordem menor pro maior
num.sort(reverse=True) # .sort(reverse=true) = vai organizar a lista por ordem inversao do maior pro menor
num.insert(2, 2)  # .insert ( posiçao , algo ) = insere numa posiçao espesifica um numero por exemplo mas ele n deleta o numero que estava nessa posiçao ele so a ocupa
#num.pop(0) # .pop = elimina um indice da lista escolhido
if 4 in num:
    num.remove(4) # .remove = remove o primeiro numero do indice a encontrar
else:
    print("Nao achei o 4")
print(num)
print(f"Essa lista tem {len(num)} elementos")
