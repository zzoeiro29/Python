def Permutacoes(palavra):
    if len(palavra) == 1:
        return [palavra]  # caso base: só há uma permutação
    resultado = []
    for i in range(len(palavra)):
        letra = palavra[i]
        resto = palavra[:i] + palavra[i+1:] # a palavra sem a letra da posição i
        for p in Permutacoes(resto):
            resultado.append(letra + p)  # letra + p
    return resultado

palavra = (input("Digite uma palavra: "))
print(Permutacoes(palavra))