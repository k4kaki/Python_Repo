def my_fun(my_list,s,e):
    del (my_list[s:e])
 
values = [2, 9, 16, 3, 24, 13, 15]
my_fun(values,-6,-4)
my_fun(values,2,4)
print(values)
