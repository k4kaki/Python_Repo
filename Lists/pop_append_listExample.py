my_list = [12, "cat", 3.4, "dog", 62]
new_list = []
for k in range(5):
    if k % 2:
        m = my_list.pop(k)
        new_list.append(m)
print(new_list)
