def find_outlier(integers):
    contp = 0
    conti = 0
    for i in integers:
        if i % 2 == 0:
            contp += 1
        else:
            conti += 1
    if contp > conti:
        for i in integers:
            if i % 2 == 1:
                return i
    elif conti > contp:
        for i in integers:
            if i % 2 == 0:
                return i
print(find_outlier([2,6,8,10,3]))