num1 = int(input("digite um numero inteiro: "))
num2 = int(input("digite outro numero inteiro: "))
primo = 2
mmc = 1
while num2 != 1 or num1 != 1:
    if num1 % primo == 0 or num2 % primo == 0:
        mmc = mmc * primo
        if num1 % primo == 0:
            num1 = num1 // primo
        if num2 % primo == 0:
            num2 = num2 // primo
    else:
        primo = primo + 1
print("MMC:", mmc)