print("gerador de PA")
print("-=" * 10)
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razao PA: "))
#termo = primeiro nao sei pra que
cont = 1
mais = 10
total = 0
cont_termos = 0
while mais != 0:
    total += mais #total = total + mais
    while cont <= total:
        print(primeiro, end= " --> ")
        primeiro += razao
        cont += 1
    print("Pausa")
    mais = int(input("Quantos termos voce quer mostrar mais? "))
print("Total de termos mostrados: {}".format(total))



