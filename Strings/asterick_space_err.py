# Type your code here
def asterick_space(n):
    for i in range(n):
        if i==0:
            print('*'*n)
        else:
            for j in range(n-i):
                if j==0 or j==n-i-1:
                    print('*',end='')
                else:
                    print(" ")
n=int(input("Enter a number :"))
asterick_space(n)
