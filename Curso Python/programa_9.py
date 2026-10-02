x = int(input('digite um numero da tabuada: '))
print("---------")
"""
Primeira maneira:

print( x , " x 1 = ", x * 1)
print( x , " x 2 = ", x * 2)
print( x , " x 3 = ", x * 3)
print( x , " x 4 = ", x * 4)
print( x , " x 5 = ", x * 5)
print( x , " x 6 = ", x * 6)
print( x , " x 7 = ", x * 7)
print( x , " x 8 = ", x * 8)
print( x , " x 9 = ", x * 9)
print( x , " x 10 = ",x * 10)
"""

#Segunda Maneira

print("{} x {} = {}".format( x , 1 , x * 1 ))
print("{} x {} = {}".format( x , 2 , x * 2 ))
print("{} x {} = {}".format( x , 3 , x * 3 ))
print("{} x {} = {}".format( x , 4 , x * 4 ))
print("{} x {} = {}".format( x , 5 , x * 5 ))
print("{} x {} = {}".format( x , 6 , x * 6 ))
print("{} x {} = {}".format( x , 7 , x * 7 ))
print("{} x {} = {}".format( x , 8 , x * 8 ))
print("{} x {} = {}".format( x , 9 , x * 9 ))
print("{} x {} = {}".format( x , 10 , x * 10 ))

print("-" * 9)