nome = str((input("Digite o seu nome: "))).strip()
print("Analisando o seu nome...")
print("Seu nome em maiusculas é:" , nome.upper()) #poe em letra maiuscula
print("Seu nome em minusculas é:" , nome.lower()) #poe em letra minuscula
print("Seu nome tem ao todo :" , len(nome)-nome.count(" "))
#print("Seu nome primeiro nome é {} e tem {} letras".format(nome, nome.find(" "))) # encontra o primeiro nome
separa = nome.split()
print("Seu nome primeiro nome é {} e tem {} letras".format(separa[0],len(separa[0]) ))