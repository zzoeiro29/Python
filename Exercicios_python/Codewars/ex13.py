def dig_pow(n, p):
    resultado = 0
    cont = 0
    for digito in str(n):
        resultado += int(digito) ** (p + cont)
        cont += 1
    k = resultado // n
    if resultado % n == 0:
        return k
    return -1
print(dig_pow(41, 5))