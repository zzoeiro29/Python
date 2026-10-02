x = int(input("Digite um numero inteiro: "))
print("Escolha uma das bases para a conversao: ")
print("[ 1 ] converter para binario")
print("[ 2 ] converter para octal")
print("[ 3 ] converter para hexadecimal")
opcao = int(input("Sua opcao: "))
if opcao == 1:
    print("{} convertido para binario é igual a {} ".format(x,bin(x)[2:]) ) #bin = binario
elif opcao == 2:
    print("{} convertido para octal é igual a {} ".format(x, oct(x)[2:])) #oct = octal
elif opcao == 3:
    print("{} convertido para hexadecimal é igual a {} ".format(x, hex(x)[2:])) # hex = hexadecimal
else:
    print("se é burro?")