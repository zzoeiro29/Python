def make_readable(seconds):
    horas = seconds // 3600
    restante = seconds % 3600
    minutos = restante // 60
    segundos = restante % 60
    return(f"{horas:02d}:{minutos:02d}:{segundos:02d}")
print(make_readable(3601))