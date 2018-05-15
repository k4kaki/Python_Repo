# Type your code here
def file_dict_milk_bread(sample):
    file_read=open(sample,'r')
    out_dict={}
    milk=[]
    bread=[]
    data=file_read.readlines()
    for i in data:
        j=i.split()
        if j[0]=='m':
            milk.append([float(x) for x in j[1:]])
        else:
            bread.append([float(x) for x in j[1:]])
    out_dict['milk']=milk
    out_dict['bread']=bread
    return out_dict
print(file_dict_milk_bread('sample'))
