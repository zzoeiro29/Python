cont = soma = 0
while True: # ciclo infinito
    x = int(input("digite um numero: [999 para parar]: "))
    if x == 999:
        break
    soma += x
    cont += 1
print(f"voce digitou {cont} numeros e a soma entre eles foi {soma}")  #f string