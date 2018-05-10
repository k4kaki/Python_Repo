def fact(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fact(n-1)*n
gen=(fact(i) for i in range(10))
try:
    while True:
        print(next(gen))
except StopIteration:
    print("Iterations reached Maximum")
else:
    print("Everything went fine")
finally:
    print("YOYO done with the things")
