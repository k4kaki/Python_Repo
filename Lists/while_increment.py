def my_fun(m, increment):
    x = 0
    while x < len(m):
        m[x] = m[x] + increment
        x = x + 1
    return m 

values = [4, 3, 7]
print(my_fun(values, 2))
