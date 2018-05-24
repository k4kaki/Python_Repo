import os
def remove_new_lines(fname):
    flist=open(fname).readlines()
    return [s.strip('\n') for s in flist]
    
    
    
    
    
    
for f in os.listdir('.'):
    if f.endswith('.txt'):
        print(remove_new_lines(f))
