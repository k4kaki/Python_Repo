fp=open('details.txt','r')
emps=fp.readlines()
emps=[emp.strip('\n') for emp in emps]
emps=[emp.split(':') for emp in emps]
header=emps.pop(0)
emps=[ dict (zip(header,emp)) for emp in emps ]
print(emps[:])
fp.close()

