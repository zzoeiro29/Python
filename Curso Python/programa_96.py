def area(largura,comp):
    a = largura * comp
    print(f"A area de um terreno {largura} x {comp} é de {a}m")
print()
print("  Controle de Terrenos  ")
print("-" * 40)
l = float(input("LARGURA (m): "))
c = float(input("COMPRIMENTO (m): "))
area(l,c)