def mydecorator(f):
    def wrapper():
        print("Before fn")
        f()
        print("After fn ")
    return wrapper

@mydecorator
def printName():
    print('Antony')

printName()
