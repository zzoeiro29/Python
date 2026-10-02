from time import sleep
#minha versao
"""
def maior(* num): #desempacotar
    print("Analisando valores...")
    for i in num:
        print(i, end=' ')
        sleep(0.3)
    print(f" Foram informados {len(num)} valores ao todo")
    print(f"O maior valor informado foi {max(num)}")  #max é o maximo
    print("-" * 30)
    sleep(1.5)
print("-"*30)
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior(0)
"""
#versao gunabara
def maior(* num): #desempacotar
    print("-" * 30)
    cont = maiores = 0
    print("Analisando valores...")
    for valor in num:
        print(f"{valor}", end=' ')
        sleep(0.3)
        if cont == 0:
            maiores = valor
        else:
            if valor > maiores:
                maiores = valor
        cont += 1
    print(f" Foram informados {len(num)} valores ao todo")
    print(f"O maior valor informado foi {maiores}")  #max é o maximo
    sleep(1.5)
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior(0)