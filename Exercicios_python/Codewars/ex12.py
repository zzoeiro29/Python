def solution(s):
    espaco = " "
    frase = ""
    for i in s:
        if i.isupper():
            frase += espaco
        frase += i
    return frase
print(solution("Hello World"))