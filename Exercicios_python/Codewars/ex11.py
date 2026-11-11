def rgb(r, g, b):
    resultado = ""
    for cor in (r,g,b):
        if cor < 0:
            cor = 0
        if cor > 255:
            cor = 255
        resultado += f"{cor:02X}"
    return resultado
print(rgb(0, 0, 0))
