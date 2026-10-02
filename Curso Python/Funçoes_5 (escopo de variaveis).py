# Escopo variaveis
"""
def teste():
    x = 8 # x tem um escopo local pq so funciona se a funçao for declarada
    print(f"Na funçao teste, n vale {n}")
    print(f"Na funçao teste, x vale {x}")

#Programa Principal
n = 2 # n tem um escopo global pq foi declarada no programa principal e nao na funçao
print(f"No programa principal, n vale {n}")
teste()
#print(f"No programa principal, x vale {x}") n funciona"
"""

def funcao():
    global n1 # faz com que o n1 global fique na funçao, neste casso tira a variavel local n1, pela global n1
    n1 = 4 # local
    print(f"N1 dentro vale {n1}")


n1 = 2 # global
funcao()
print(f"N1 fora vale {n1}")

