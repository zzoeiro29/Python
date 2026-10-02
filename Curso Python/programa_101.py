#from datetime import date
"""
def voto(cla):
    if cla < 18:
        return "NAO VOTA"
    if cla >= 18 and cla <= 65:
       return "VOTO OBRIGATORIO"
    elif cla > 65:
        return "VOTO OPCIONAL"


print("-" *30)
ano = int(input("digite em que ano voce nasceu ? "))
data = date.today().year - ano
print(f"Com {data} anos: {voto(data)}")
"""

#versao gunabara
def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 18:
        return f"Com {idade} anos: NAO VOTA"
    elif 16 <= idade < 18 or idade > 65:
        return f"Com {idade} anos: VOTO OPCIONAL"
    else:
        return f"Com {idade} anos: VOTO OBRIGATORIO"


nasc = int(input("digite em que ano voce nasceu ? "))
print(voto(nasc))