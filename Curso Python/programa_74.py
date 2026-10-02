from random import randint
#minha versao
"""
valores = (randint(0,10) , randint(0,10) ,
           randint(0,10), randint(0,10),
           randint(0,10) )
maior = 0
menor = valores[0]
print("Os valores sorteados foram: " , end="")
for n in valores:
    print( n , end=" ")
#print("Os valores sorteados foram: ", valores)
for c in valores:
    if c > maior:
        maior = c
    elif c < menor:
        menor = c
print(f"\nO maior valor sorteado foi {maior}")
print(f"O menor valor sorteado foi {menor}")
"""
#versao gunabara
valores = (randint(0,10) , randint(0,10) ,
           randint(0,10), randint(0,10),
           randint(0,10) )
print("Os valores sorteados foram: " , end="")
for n in valores:
    print( n , end=" ")
#print("Os valores sorteados foram: ", valores)
print(f"\nO maior valor sorteado foi {max(valores)}") # max = maior
print(f"O menor valor sorteado foi {min(valores)}") # min = maior

