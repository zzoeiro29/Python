""" minha maneira
print("="*10)
print("10 TERMOS DE UM PA")
print("="*10)
p_term = int(input("Primeiro termo: "))
Razao =  int(input("Razao: "))
for c in range(p_term,10*Razao,Razao ):
    print(c , "->" , end=" ")
print("FIM")
"""
#outra maneira
print("="*10)
print("10 TERMOS DE UM PA")
print("="*10)
p_term = int(input("Primeiro termo: "))
Razao =  int(input("Razao: "))
decimo =  p_term + (10-1) * Razao
for c in range(p_term,decimo + Razao ,Razao ):
    print(c , "->" , end=" ")
print("FIM")