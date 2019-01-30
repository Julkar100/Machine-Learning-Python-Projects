# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 16:49:15 2018

@author: CodersMine
"""


"""
strange thing i came to know while using file function
since we open the file in read mode 
and print it using file.read() function 
and then when we save file.read in a variable 
then it saves nothing in that

similarly 
when we save the file first in variable and then 
without opening a new file we try to print that 
it prints a blank space only


it is so because of the file pointer remains at
the end of file and while reading or saving 
it saves the file from that part only
since there is nothing left so it saves or prints 
nothing  
and to solve this we have to reload the file pointer 

"""
file=open("essay.txt",'r')
#print(file.read())
lines=file.read()
print(lines)

lines=lines.split()
"""
file=open("essay.txt",'r')
#print(file.read())
lines=file.read()
print(lines)

lines=lines.split()


words ending with [.] are listed in the essay
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if(lines[i][j]=='.'):
            print(lines[i])
"""    
for i in range(len(lines)):
    lines[i]=lines[i].replace('.','\n')
    print(lines[i])
    
lines=' '.join(lines)  
print(lines)
file.close()
file=open("Converted.txt",'w')
file.write(lines)
file.close()
"""
now we have converted a file that has only fullstops 
to a file having each line separated with a new line /n 


"""