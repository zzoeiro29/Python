# Tupla = ()
# listas = []
# dicionarios = {}
# Tuplas sao variaveis compostas que NAO podem ser mudadas (imutaveis)
lanche = ("Hamburger" , "suco" , "Pizza" , "pudim", "Batata Frita") #Tupla é entre parentises, mas n é presiso
#lanche = "Hamburger" , "suco" , "Pizza" , "pudim" #Tupla é entre parentises, mas n é presiso
print(sorted(lanche)) #sorted = organizado , mostra por ordem alfabenica nota: ele nao mudou a tupla em si so ordenou
#print(lanche)
#print(len(lanche))

#maneiras diferentes com o for:
#1º
#for cont in range( 0, len(lanche) ):
#    print(f"Eu vou comer {lanche[cont]} na posiçao {cont}")

#2º
#for comida in lanche: # for para itens
#    print(f"Eu vou comer {comida}")

#3º
#for pos, comida in enumerate(lanche):
#    print(f"Eu vou comer {comida} na posiçao {pos}")
#print("comi pra caralho")

# com numeros tuplas
a = ( 2, 5, 4)
b = (5, 8, 1, 2)
c = b + a # vai juntar as tuplas
#print (c.count(5)) #quantas vezes esta aparecer o numero 5
print(c)
print(c.index(5, 1)) # index = ve a posiçao, tambem tem o deslocamneto

pessoa = ("gustavo", 39, "M", 99, 88)
del(pessoa) # del = apaga uma variavel, consegue apagar uma tupla inteira, mas n 1 item da tupla


