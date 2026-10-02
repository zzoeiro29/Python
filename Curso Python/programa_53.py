frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras) #join vai juntar as palavras separadas
inverso = ''

# ou inverso = junto [::-1]
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

print("O inverso de {} é {} ".format(junto,inverso))
if inverso == junto:
   print("é um palindromo")
else:
    print("nao é um palindromo")