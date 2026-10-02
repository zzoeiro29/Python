Palavras = ("APRENDER", "PROGRAMAR" , "LINGUAGEM", "PYTHON",
            "CURSO","GRATIS", "ESTUDAR", "PRATICAR",
            "TRABALHAR", "MERCADO", "PROGRAMADOR", "FUTURO")
for palavra in Palavras: # for para a tupla
    print(f"\nNa palavra {palavra} temos: ", end="")
    for letra in palavra: # for letra por letra
        if letra.lower() in "aeiou": # ver se a letra é uma vogal
            print(letra.lower(), end=" ")

