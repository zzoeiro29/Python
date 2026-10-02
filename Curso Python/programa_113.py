# minha versao
"""
while True:
    try:
        n1 = int(input("Digite um inteiro:"))
        n2 = float(input("Digite um numero real: "))
    except (ValueError, TypeError):
        print("\033[0;31m ERRO: por favor, digite um numero inteiro valido \033[m")
    else:
        print(f"O valor inteiro digitado: foi {n1} e o real {n2}")
        break
"""
# versao gunabara
def leiaInt(msg):
    while True:
        try:
            n1 = int(input(msg))
        except (ValueError, TypeError):
            print("\033[0;31mERRO: por favor, digite um numero inteiro valido \033[0;34m")
            continue
        except KeyboardInterrupt:
            print("\033[0;31m\nEntrada de dados interrompida por alguem ne\033[m")
        else:
            return n1

def leiaFloat(msg):
    while True:
        try:
            n2 = float(input(msg))
        except (ValueError, TypeError):
            print("\033[0;31m ERRO: por favor, digite um numero inteiro valido \033[m")
            continue
        except KeyboardInterrupt:
            print("\033[0;31m\nEntrada de dados interrompida por alguem ne\033[m")
        else:
            return n2

num = leiaInt("Digite um valor:")
num2 = leiaFloat("Digite um numero real:")
print(f"O valor inteiro digitado: foi {num} e o real {num2}")
