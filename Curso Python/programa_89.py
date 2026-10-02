#minha versao que esta correta!
"""
inicial = []
final = []
nota = []
nota_final = []
media = cont = 0
while True:
    nome = str(input("Digite seu nome: ")).strip()
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    #adiciona cont, nome na lista incial
    inicial.append(cont)
    inicial.append(nome)
    #adciona as nota1, nota2 na lista inicial das notas
    nota.append(nota1)
    nota.append(nota2)
    #copia a lista da nota pra nota_final
    nota_final.append(nota[:])
    #media
    media = (nota1 + nota2) / 2
    #adiciona a media a lista incial
    inicial.append(media)
    #copia a lista incial pra final
    final.append(inicial[:])
    #limpa a lista incial
    inicial.clear()
    #limpa a lista das notas
    nota.clear()
    cont += 1
    res = str(input("Quer continuar? [S/N] ")).upper()
    if res == "N":
        break

print("-="*40)
print(f"{"No.":<3}", "NOME", f"{"Media":>12}")
print("-"*25)
for c in final:
    print(f"{c[0]:<3}{c[1]:<1}{c[2]:>15}")
    cont += 1
print("-"*25)
while True:
    mostrar = int(input(("Mostrar notas de qual aluno? (999 interromper): ")))
    if mostrar == 999:
        break
    elif mostrar in final[mostrar]:
        print(f"Notas de {final[mostrar][1]} sao {nota_final[mostrar]} ")
print("ACABOU CARALHO")
"""
#versao gunabara
ficha = list()
while True:
    nome = str(input("Digite seu nome: ")).strip()
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    res = str(input("Quer continuar? [S/N] ")).upper()
    if res == "N":
        break
print("-="*30)
print(f"{"No.":<4}", f"{"NOME":<10}", f"{"Media":>8}")
print("-"*25)
for i, a in enumerate(ficha):
    print(f"{i:<4}{a[0]:<10}{a[2]:>8.1f}")
print("-"*25)
while True:
    mostrar = int(input(("Mostrar notas de qual aluno? (999 interromper): ")))
    if mostrar == 999:
        break
    elif mostrar <= len(ficha) - 1:
        print(f"Notas de {ficha[mostrar][0]} sao {ficha[mostrar][1]} ")
print("ACABOU CARALHO")