def one_to_2D(some_list, r, c):
    new_array=[]
    k=0
    for i in range(r):
        sb_ar=[]
        for j in range(c):
            sb_ar.append(some_list[k])
            k=k+1
        new_array.append(sb_ar)
    return new_array
print(one_to_2D([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 4, 4))
