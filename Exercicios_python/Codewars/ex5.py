def count_bits(n):
    binario = ""
    while n > 0:
        resto = n % 2
        binario += str(resto)
        n = n // 2
    return binario.count("1")
print(count_bits(10))
