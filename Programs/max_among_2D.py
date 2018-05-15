def max_among_2D(array):
    max_=0
    for i in array:
        for j in range(len(i)-1):
            if i[j] > i[j+1]:
                if int(i[j])%2 == 0:
                    max_=i[j]
            else:
                if int(i[j+1])%2 == 0:
                    max_==i[j+1]
    return max_
array=input("Enter a 2D array:")
print(max_among_2D(array))