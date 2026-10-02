frase = "Curso em Video python"
n = "2"
#print(frase[3]) escolher indice []
#print(frase[3:13]) #escolhe de que indice quer começar e acabar :
#print(frase[13:]) #começa em 13 e vai ate ao final
#print(frase[1:15:2]) #começa do primeiro indice dps vai ate ao 15 indice pulando de 2 em 2
#print(frase[1::2]) #começa do primeiro indice dps vai ate ao ultimo indice pulando de 2 em 2

#maneira de escrever texto grande

#print("""
#Num fim de tarde tranquilo à beira-mar,
#o som das ondas parecia conversar com o vento.
#As pessoas caminhavam sem pressa,
#deixando para trás o peso do dia.
#Havia algo de especial naquele momento —
#como se o tempo desacelerasse
#só para permitir que todos respirassem mais fundo.
#Às vezes, é nesses instantes simples
#que encontramos a verdadeira paz,
#longe do ruído e perto do essencial.""")

#---- PALAVRAS CHAVE ------

#count()
#print(frase.count('o')) # count = conta quantas vezes tem o minusculo na frase

#Lower()
#print(frase.lower().find("video")) # o lower vai diminuir o v da frase pra o find encontra o v minusculo e mostre o indice

#casefold()
#print(frase.casefold()) #casefold = é tipo um lower mas mais agressivo, usado para outros idiomas

#upper()
#print(frase.upper().count('O')) # upper = deixa a letra maiuscula , deste caso esta a contar quantas vezes tem o maiusculo na frase

#len()
#print(len(frase)) # len = conta o numero de indices da frase

#sptri()
#print(len(frase.strip())) #sptri = remove os espaços indesejados da direita e esquerda variaçoes rstrip e lstrip

#lsptri()
#print(len(frase.lstrip())) #lsptri = remove os espaços indesejados da esquerda

#rsptri()
#print(len(frase.rstrip())) #rsptri = remove os espaços indesejados da direita

#sptri(caracter)
#print(len(frase.strip(-))) #sptri(caracter) = remove caracteres especificos

#replace()
#print(frase.replace('python', 'Android')) # replace = troca palavras, nao muda indices

#in
#print("Curso" in frase) # in = verifica se algo esta dentro da frase ou esta em algo vai devolver true se tiver e se n tiver é false

#find()
#print(frase.find("de")) # find = vai encontrar a posiçao de onde começa a palavra ou frase e vai dizer o indice

#rfind()
#print(frase.rfind("o")) # rfind = Igual ao find, mas busca da direita

#index()
#print(frase.index("o")) #index = ele é como o find, so que nao retorna -1 quando da erro

#rindex()
#print(frase.rindex("o")) #rindex = ele é como o rfind, so que nao retorna -1 quando da erro

#split()
#dividido = frase.split() #split = separa as palavras em indices separados
#print(dividido[2][3])

#rsplit()
#dividido = "a,b,c".rsplit(",", 1) #rsplit = separa as palavras em indices separados mas é da direita para a esquerda
#print(dividido)

#splitlines()
#dividido = "a\nb".splitlines() #splitlines = separa as palavras em indices separados mas separa a quebra de linha (ou a outra linha) tambem
#print(dividido)

#join(unir)
#print(",".join(frase)) #join = uma lista de strings com um separador ex: ","

#partition(sep)
#print(frase.partition("o")) #partition = divide em 3 partes

#rpartition(sep)
#print(frase.rpartition("o")) #rpartition = igual so que da direita para a esquerda

#capitalize()
#print("hello word".capitalize()) #capitalize = deixa a primeira letra em maiuscula

#Title()
#print(frase.title()) # title = titulo, deixa Cada palavra com a inicial maiúscula

#swpacase()
#print(frase.swapcase()) #swapcase = Inverte maiúsculas/minúsculas

#startwith()
#print(frase.startswith("Curso")) #startwith() = verifica se a frase ou palavra começa pela primeira palavra da frase ou prefixo, e devolve true ou false

#endswith()
#print(frase.endswith("python")) #endstwith() = verifica se a frase ou palavra começa pela ultima palavra da frase ou sufixo, e devolve true ou false (é o contrario do startwith)

#center()
#print(frase.center(30)) #center() = centralisa n caracteres

#ljust()
#print(frase.ljust(30)) # ljust() = alinha ha esquerda n caracteres sem perder os espaços

#rjust()
#print(frase.rjust(30)) # rjust() = alinha ha direita n caracteres sem perder os espaços

#zfill()
#print(n.zfill(4)) # zfill() = prenche com zeros ha esquerda


#Verificaçoes booleanas com o is...

#isalpha()
#print(frase.isalpha()) # isalpha() = restorna True se tiver so letras (neste caso tem letras e espaços entao é false)

#isdigit()
#print(frase.isdigit()) # isdigit() = restorna True se tiver so digitos(numeros) basicamente

#isnumeric()
#print(frase.isnumeric()) # isnumeric() = restorna True se tiver so valores numericos basicamente numeros de todas as formas diferente do isdigit()

#isdecimal()
#print(frase.isdecimal()) # isdecimal() = restorna True se tiver so valores entre 0 e 9

#isalnum()
#print(frase.isalnum()) # isalnum() = restorna True se tiver so numeros e/ou letras

#isupper()
#print(frase.isupper()) # isupper() = restorna True se todas as letras forem maiosculas

#islower()
#print(frase.islower()) # islower() = restorna True se todas as letras forem minuculas

#istitle()
#print(frase.istitle()) # istitle() = restorna True se tiver formato em Title

#isidentifier()
#print(frase.isidentifier()) # isidentifier() = restorna True se o que ta escrito pudesse ser uma variavel ou funçao

#isprintable()
#print(frase.isprintable()) # isprintable() = restorna True se rodos os caracteres sao imprimiveis

#isascii()
print(frase.isascii()) # isascii() = restorna True se rodos os caracteres sao em ascii (assentos por exemplo nao sao)
