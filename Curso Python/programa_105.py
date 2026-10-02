# minha versao
"""
def notas(* nota, sit = False):

   # -> funçao mogadora de gunabara
   # :param nota: poe varias notas
   # :param sit: valor especial pra ver se o aluno esta bem ou nao
   # :return: retorna o valor


    n = dict()
    n["total"] = len(nota)
    n["maior"] = max(nota)
    n["menor"] = min(nota)
    soma = 0
    for i in nota:
        soma += i
    n["media"] = soma/len(nota) # ou so sum(n)/len(n) era mais facil -_-
    if sit:
        if n["media"] >= 7:
            n["situaçao"] = "Boa"
        elif n["media"] >= 5:
            n["situacao"] = "Razoavel"
        else:
            n["situacao"] = "Ruim"
    return n
resp = notas(2,1,10)
help(notas)
print(resp)
"""

#versao gunabara
def notas(* n, sit = False):
    """
    funçao mogadora de gunabara
    :param nota: poe varias notas
    :param sit: valor especial pra ver se o aluno esta bem ou nao
    :return: retorna o valor

    """
    r = dict()
    r["total"] = len(n)
    r["maior"] = max(n)
    r["menor"] = min(n)
    r["media"] =  sum(n)/len(n)
    if sit:
        if r["media"] >= 7:
            r["situaçao"] = "Boa"
        elif r["media"] >= 5:
            r["situacao"] = "Razoavel"
        else:
            r["situacao"] = "Ruim"
    return r
resp = notas(2,1,10, sit=True)
help(notas)
print(resp)
