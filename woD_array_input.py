# Type your code here
def twoD_array(m,n):
    twoD=[]
    
    for i in range(m):
        some=[]
        for j in range(n):
            k=input("Enter element:")
            some.append(k)
        twoD.append(some)
    return twoD
m=int(input("Enter val for #ROWS:"))
n=int(input("Enter val for #COLUMNS:"))
print(twoD_array(m,n))
