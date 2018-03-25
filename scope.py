def fun1():
        def fun2():
                print('x inside thw fun2 is ',x)
        x=7
        fun2()
        print('x inside the fun1 is',x)
        
x=5
print('x in the main program iss',x)
fun1()
