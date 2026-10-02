x = float(input("Primeira nota do aluno: "))
y = float(input("Segunda nota do aluno: "))
media = (x + y) / 2
print("Tirando {} e {}, a media do aluno é de {}".format(x, y, media))
print("O aluno esta aprovado" if media >= 7 else "O aluno esta em recuperaçao" if media > 5 else "Reprovado otário")
#outra maneira
""" 
if media >= 7: 
    print("O aluno esta aprovado")
elif media > 5: #outra maneira 7 > media >= 5 ou media >= 5 and media < 7
    print("O aluno esta em recuperaçao")
else:
    print("Reprovado otário")
"""
