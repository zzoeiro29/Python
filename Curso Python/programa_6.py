n = int(input("digite um numero: "))
#minha versao
#print("o dobro é de {} vale {} ".format(n, n*2)) #dobro
#print("o triplo é de {} vale {} ".format(n, n*3)) #tiplo
#print("a raiz quadrada de {} vale {} ".format(n, n ** (1/2))) #raiz quadrada ** (1/2)

#outra versao
d = n *2
t = n *3
r = n ** (1/2) # raiz quadrada

print("o dobro é de {} vale {} ".format(n, d)) #dobro
print("o triplo é de {} vale {}. \nA raiz quadrada de {} vale {:.2f} ".format(n, t, n ,r)) #tiplo e raiz quadrada

#\n serve pra quebrar a linha q nem no c++
#outra forma de raiz quadrada é (com a funçao power):
#print("a raiz quadrada de {} vale {} ".format(n, pow(n,(1/2))) #raiz quadrada pow(n,(1/2)
