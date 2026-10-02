from modulo.coisas import numeros
num = int(input("Digite um valor: "))
fat = numeros.factorial(num)
print(f"O fatorial de {num} é {fat}")
print(f"O dobro de {num} é {numeros.dobro(num)}")