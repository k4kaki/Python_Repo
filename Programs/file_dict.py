def file_dict(sample):
    out_dict={}
    file_read=open(sample,'r')
    data=file_read.readlines()
    for i in data:
        j=i.split(',')
        out_dict[str(j[0])]=[float(x) for x in j[1:]]
    return out_dict
print(file_dict('sample'))
