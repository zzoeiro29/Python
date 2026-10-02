#print("\033[1;33;44m Ola mundo \033[m") exemplo 1
""" exemplo 2
a = 3
b = 5
print("O valores sao \033[32m{}\033[m e \033[31m{}\033[m ".format(a,b))
"""

nome = "Guanabara"
cores = {"limpa" : "\033[m"
        ,"azul" : "\033[34m"
        , "amarelo" : "\033[33m"
        , "pretoebranco" : "\033[7;30m" }
#print("é um prazer te conhecer, {}{}{}! ".format ("\033[4;34m" ,nome,"\033[m"))
print("é um prazer te conhecer, {}{}{}! ".format (cores["amarelo"] ,nome, cores["azul"]))