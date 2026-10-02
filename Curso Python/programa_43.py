peso = int(input("Digite o seu peso: "))
altura = float(input("Digite sua altura: "))
IMC = peso / (altura * altura)
print("O IMC é dessa pessoa é de {:.1f}".format(IMC) )
if IMC < 18.5:
    print("Esta abaixo do peso")
elif IMC < 25: # ou 18.5 <= IMC < 25
    print("Esta no peso ideal")
elif IMC < 30:
    print("Esta no sobrepeso")
elif IMC < 40:
    print("Esta na obsidade")
else:
    print("Esta na obsidade morbida")