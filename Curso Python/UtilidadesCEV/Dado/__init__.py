def leiaDinheiro(msg):
    while True:
        num = str(input(msg)).replace(",",".")
        if num.isalpha() or num.strip() == "":
            print(f"\033[0;31mERRO: \"{num}\" é um preço invalido! \033[m")
        else:
            num = float(num)
            return num