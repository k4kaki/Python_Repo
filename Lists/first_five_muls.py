# Type your code here
def first_five(x):
    fi_fi=[]
    for i in range(1,6):
        fi_fi.append(x*i)
    return fi_fi
    
x=int(input("Enter an integer:"))
print(first_five(x))
