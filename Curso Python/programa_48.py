soma = 0
cont = 0
for c in range (1,501,2):
    if ( c % 3 == 0):
        soma += c # soma = soma + c , acumulador
        cont+=1 # cont = cont + 1
print("soma é: ",soma)
print("A quantidade de numeros é: ",cont)


