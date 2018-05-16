
def multiple_of(x):



    def multiple(y):

        return x*y



    return multiple



c1 = multiple_of(5)  # 'c1' is a closure

c2 = multiple_of(6)  # 'c2' is a closure



print(c1(4))

print(c2(4))
