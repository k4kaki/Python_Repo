def fb(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fb(n-1)+fb(n-2)
def fib_gen(n):
    yield fb(n)
x='Y'
n=0
while x == 'Y':
    x=input("Enter whether to continue or not'Y/N':")
    print(next(fib_gen(n)))
    n+=1

