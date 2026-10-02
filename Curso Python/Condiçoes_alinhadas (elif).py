nome = str(input("Qual o seu nome? "))
if nome == "Gustavo":
    print("nigger")
elif nome == "Pedro" or nome == "Maria" or nome == "Paulo":
    print(" seu nome é normal ")
elif nome in "Ana Claudia Jessica Juliana": #in é se esta dentro
    print("Seu nome femenino arriegua")
else:
    print(" seu nome é legal ")
print("Tenha um bom dia, {}".format(nome))