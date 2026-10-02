from random import randint #ou choice
from time import sleep #tempo de espera
print("--" * 20)
print("vou pensar em um numero de 0 a 5. Adivinhe")
print("--" * 20)
x = int(input("Em que numero eu pensei? ")) # x é o jogador
print("Processando...")
sleep(2)
computador = randint(0,5) #faz o computador "pensar" ou sortear os numeros inteiros
if x == computador:
    print("Perdi fahhhh! Es um skibidi")
else:
    print("Ganhei! Eu pensei no numero {} e nao no {}".format(computador,x))


