"""
def soma(a , b): # defenir soma
    print(f"A = {a} e B = {b}")
    s = a + b
    print(f"A soma é igual a {s}")


#Programa Principal
#soma(4, 5)  #parametros
#ou
#soma(a = 4, b = 5)
#mudar a ordem
soma(b = 4, a = 5)
#da pra fazer com varios
soma(8, 9)
#soma(2, 1)
"""

"""
#com tuplas
#empacotar e desempacotar funçoes
def contador(* num): # ele vai mandar o contador que vai pra *num que nao presisa sabes quantos numeros tem ou seja ele desempacotar o contador
    tam = len(num)
    print(f"Recebi os valores {num}")

#Tuplas e Programa principal
contador(2,1,7) # empacotar
contador(8,0)
contador(4,4,6,7,6,2)
"""

#nao é desempacotar
def dobra(list):
    #versao gunabara
    pos = 0
    while pos < len(list):
        list[pos] *= 2
        pos += 1
    #minha versao
    #pos = 0
    #for valor in list:
    #    list[pos] *= 2
    #    pos += 1


#com listas
valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)


