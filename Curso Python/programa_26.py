frase = str(input("Digite uma frase: ")).strip().upper()
print("A letra {} apareceu {} vezes na frase".format(frase[0], frase.count("A")))
print("A primeira letra {} apareceu na posiçao {}".format(frase[0] , len(frase[0]))) #  len(frase[0] ou frase.find("A")+1
print("A ultima letra {} apareceu na posiçao {}".format(frase[0] , frase.rfind("A")+1)) # rfind vai  começar a ler da direita para esquerda