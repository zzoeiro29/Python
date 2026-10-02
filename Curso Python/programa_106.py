from time import sleep
#lista global
c = ("\033[m", # 0 - sem cores
     "\033[0;30;41m", #1 - vermelho
     "\033[0;30;42m", #2 - verde
     "\033[0;30;43m", #3 - amarelo
     "\033[0;30;44m",) #4 - azul

def ajuda(com):
    titulo(f"Acessando o manual do comando {com}", 4) # funçao dentro de funçao
    print(c[3], end="")
    help(com)
    print(c[0], end="")
    sleep(2)

def titulo(msg, cor=0): # cor = 1 é vermelho
    tam = len(msg)
    print(f"{c[cor]} " , end="") # c = lista , c[indice cor]
    print("-"*tam)
    print(f"{msg}")
    print("-"*tam)
    print(f"{c[0]} ", end="")
    sleep(1)
#Programa Principal
comando = ""
while True:
    titulo("Sistema de ajuda PyHELP", 2)  #mensagem do titulo
    comando  = str(input("Funçao ou Biblioteca: "))
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)
titulo("ATE LOGO", 1)

