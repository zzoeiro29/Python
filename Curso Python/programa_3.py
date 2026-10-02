#sem o int vai dar errado pq ele vai encarar como string e n int
#nome = tipo( input (texto) )
n1 = int(input("digite um numero: "))
n2 = int(input("digite outro numero: "))
s = n1 + n2
# type diz qual o tipo da variavel print(type(n1))
# outra forma print("soma entre:",n1,"e",n2,"vale:", s)
#versao do format
print("soma entre: {} e {} vale {}" .format(n1,n2,s))