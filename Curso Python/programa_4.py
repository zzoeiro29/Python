algo = input('Digite algo: ')

print('O tipo primitivo desse valor é ', type(algo)) #tipo
print('Só tem espaços?', algo.isspace()) #espaços
print('É um número?', algo.isnumeric()) #numero
print('É alfabético?', algo.isalpha()) #letra
print('É alfanumérico?', algo.isalnum()) #numero e letra
print('Está em maiúsculas?', algo.isupper()) #M
print('Está em minúsculas?', algo.islower()) #m
print('Está capitalizada?', algo.istitle()) #tem maiusculas ou minusculas é capitalizado
