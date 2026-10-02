l1 = [1,2,3,4,5,7]
l2 = [5,6,7,8]
l3 = []

for n in l1:
    if n in l2:
        l3.append(n)
print(l3)