def somar( a = 0, b = 0 , c = 0): # c = 0 é um parametro opcional
    soma = a + b + c
    return soma # retorna um resultado, mais nada

#resp = somar( 3, 2 , 4)
#print(resp)
#ou
#print(somar(3,2,4))

#gurdar returns em variaveis
r1 = somar(3,2,5)
r2 = somar(2,2,)
r3 = somar(6)
print(f"Os resultados foram {r1} e {r2} e {r3}")