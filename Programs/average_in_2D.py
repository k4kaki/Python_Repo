# Type your code here
def average(array):
    sum_=0
    k=0
    for i in array:
        for j in range(len(i)):
            sum_=sum_+int(i[j])
            k=k+1
            print(k)
    return sum_/k
array=input("Enter a 2D array:")
print(average(array))