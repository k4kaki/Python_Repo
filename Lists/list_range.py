#This will give you an error as you are incrementing it as integer but the increment never
#takes in float types, that's the reason it will give you an error
my_list = []
for x in range(4,30,3.0):
    my_list.append(x)
print(my_list)
