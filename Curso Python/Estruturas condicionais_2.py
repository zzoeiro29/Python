n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
m = ( n1+n2 ) /2
#if normal
#if m >= 10:
#    print("passou")
#else:
#    print("nao passou")

#if simplificado
print("passou" if m >= 10 else "nao passou")
print("seu aluno tirou na media de: {:.1f}".format(m))
