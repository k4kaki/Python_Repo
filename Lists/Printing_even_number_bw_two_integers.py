# Type your code here
def a_b(x,y):
    a_b=[]
    for i in range(x,y):
        if not(i%2):
            a_b.append(i)
    return(a_b)
x=int(input("Enter a positive integer:"))
y=int(input("Enter another positive integer:"))
print(a_b(x,y))
