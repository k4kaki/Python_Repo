list_1 = ["dog", 3, "cat" , 25, 2.4]
list_2 = ["car", 25, "dog" , 43]
count = 0
for item in list_1:
    if item in list_2:
        count = count + 1
print (count)
