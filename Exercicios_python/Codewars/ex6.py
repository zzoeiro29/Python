def is_isogram(string):
    string = string.lower()
    palavra = True
    for letra in string:
        if string.count(letra) > 1:
            palavra = False
    if string == "":
        palavra = True
    return palavra
print(is_isogram("dasf"))
