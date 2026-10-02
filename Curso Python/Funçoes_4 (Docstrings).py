from time import sleep # importar a funçao sleep de dentro da biblioteca
# diz oq aquilo faz ex: print
#help(print)

#Doc_strings
# faz com que quando tu pedes help pra uma funçao vai aparecer o que tu escreves para o manual da funçao, pra fazer uma docstring é """ alguma coisa """
#ex:
#resumindo é um manual para o help (serve para ajudar outros programadores no teu codigo)
def contador(i,f,p):
    """
    -> Faz uma contagem
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno

    """
    c = i
    while c <= f:
        print(f"{c}", end=" ")
        c += p # c = c + p
    print("Fim")

help(contador)
