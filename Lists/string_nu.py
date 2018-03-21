def my_fun(a):
    a[0] = 'new value:'     
    a[1] = a[1] + 1      

x = ['old value:', 99]
my_fun(x)
print (x[0], x[1])
