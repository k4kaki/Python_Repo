# Type your code here
def a_b(x,y):
    a_b=[]
    for i in range(y,x-1,-1):
        if(i%2):
            a_b.append(i)
    return(a_b)

x=int(input("Enter a number: "))
y=int(input("Enter another Number: "))
print(a_b(x, y))
