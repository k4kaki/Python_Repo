# Type your code here
def sum_ascii(n):
    sum=0
    for i in range(len(n)):
        sum=sum+ord(n[i])
    return sum
n=input("Enter a string: ")
print(sum_ascii(n))
        
