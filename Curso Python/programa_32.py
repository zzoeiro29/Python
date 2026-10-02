from datetime import date #biblioteca data
ano = int(input("Que ano quer analisar? Coloque 0 para analisar o ano atual: "))
if ano == 0: #0 é para 2026 que nao é bissexto
    ano = date.today().year #o ano atual configurado na maquina
if ano % 4 == 0 and ano % 100 != 0 or ano %400 == 0:
    print("O ano {} é bissexto".format(ano))
else:
    print("O ano {} nao é bissexto".format(ano))
