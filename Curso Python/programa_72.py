#minha versao
Contagem = ("zero", "um", "dois", "tres", "quatro",
            "cinco", "seis", "sete", "oito", "nove",
            "dez", "onze", "doze", "treze", "quatorze",
            "quinze", "dezasseis","dezassete", "dezoito",
            "dezanove", "vinte")
"""
x = int(input("Digite um numero entre 0 e 20: "))
while x > 20 or x < 0:
    x = int(input("Digite um numero entre 0 e 20:"))
"""
#outra maneira do while
"""
while True:
    x = int(input("Digite um numero entre 0 e 20: "))
    if 0 <= x <= 20:
        break
print("Tente novamente. ", end="")
print(f"Voce digitou o numero {Contagem[x]}")
"""

#desafio
while True:
    x = int(input("Digite um numero entre 0 e 20: "))
    if x < 0 or x > 20:
        print("Tente novamente. ", end="")
    if 0 <= x <= 20:
        print(f"Voce digitou o numero {Contagem[x]}")
        opcao = str(input("Deseja continuar? [S/N] ")).upper()
        if opcao == "N":
            print("Volte sempre!")
            break





