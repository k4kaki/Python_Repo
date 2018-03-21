def my_fun(m):
    x = []
    for k in range(len(m)):
        if m[k] % 3 == 0 and m[k] % 2:
            x.insert(k, m[k])
    return x
 
values = [2, 9, 16, 3, 24, 13, 15]
print(my_fun(values))
