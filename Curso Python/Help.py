from time import sleep # importar a funçao sleep de dentro da biblioteca
# diz oq aquilo faz ex: print
#help(print)

def contador(i,f,p):
    c = i
    while c <= f:
        print(f"{c}", end=" ")
        c += p # c = c + p
    print("Fim")


help(contador)
