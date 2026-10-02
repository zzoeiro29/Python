# minha versao sem listas (meio que strings sao listas) kkkk
"""
expre = str(input("Digite a sua expresao: "))
contp_esquerda = contp_direita = contp = 0
Questao = False
for i, v in enumerate(expre):
    if expre[i] == "(":
        contp += 1
        contp_esquerda += 1
    if contp >= 1:
        if expre[-1] == ")" :
            contp_direita += 1
            Questao = True
        elif expre[-1] != ")":
            Questao = False
if Questao and contp_esquerda == contp_direita:
    print("Sua expressao é valida")
else:
    print("Sua expressao é invalida")
"""
#com listas versao gunabara
expre = str(input("Digite a sua expresao: "))
pilha = [] # lista vazia
for simb in expre: # strings tambem sao listas indiretamente ent basicamente ele vai a cada simbolo e verificar pelo numero de indices
    if simb == "(": # se tiver "(" na pilha
        pilha.append("(") # ele adiciona
    elif simb == ")": # se nao tiver
        if len(pilha) > 0: # ele ve se a pilha tem o "(" porque se nao tiver nao teria sido maior que 0
            pilha.pop() # e remove o ultimo elemento que nao é "(" ou ")"
        else: # se nao
            pilha.append(")") #ele adiciona um ")"
            break # fim dos pares "(" e ")" e volta ao inicio
if len(pilha) == 0:
    print("Sua expressao é valida")
else:
    print("Sua expressao é invalida")


