import sys
from projeto_115.lib.Menu import *
from time import sleep
from projeto_115.lib.Menu.arquivo import *

arq = "curso.txt"
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(["Ver pessoas cadastradas", "cadastrar nova pessoa", "Sair "])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabealho("NOVO CADASTRO")
        nome = str(input("Nome: "))
        idade = leiaInt("Idade: ")
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabealho("Tchau -_-")
        sys.exit() # sair do porgrama
    else:
        print("\033[0;31mErro: Digite uma opcao valida\033[m")
    sleep(2)


