velocidade = float(input("Qual a velocidade do carro: "))
if velocidade > 80:
    print("Multado! voce execedeu o limite permitido que é de 80km/h")
    multa = (velocidade - 80) * 7
    print("Voce de deve pagar uma multa de R${:.2f}!" .format(multa))
elif velocidade == 80: #pyhon elif = else if
    print("quase...")
print("Tenha um bom dia diriga com segurança!")

