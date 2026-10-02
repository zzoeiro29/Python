#minha versao
"""
lista_n = list()
for c in range(0, 5):
    n = int(input("Digite um valor: "))
    if c == 0:
        print("Adicionado ao final da lista")
        lista_n.insert(c, n)
    else:
        if n > lista_n[0]:
            print("Adicionado na posiçao 1")
            lista_n.insert(c , n )
        elif n < lista_n[0]:
            print("Adicionado na posiçao 0")
            lista_n.insert( 0 , n)
print("-=" * 30 )
print("Os valores digirado em ordem foram" , lista_n)
"""
#versao gunabara

lista_n = []
for c in range(0, 5):
    n = int(input("Digite um valor: "))
    if c == 0 or n > lista_n[-1]:
        lista_n.append(n)
        print("Adicionado ao final da lista")
    else:
        pos = 0
        while pos < len(lista_n):
            if n <= lista_n[pos]:
                lista_n.insert(pos, n)
                print(f"Adicionado na posiçao {pos}º da lista")
                break
            pos += 1
print("-=" * 30 )
print("Os valores digirado em ordem foram" , lista_n)