# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 17:34:56 2018

@author: CodersMine


1.opening the file essay as txt in read mode

problem was that it contains fullstops but the line is not splitted

2. during the shortening of line we have to make them as list
 so to decrease the load on pc and separate single lines

3. split will make them as different list items

4. using a loop we iterated through every line in the list 
   and replaced the fullstop with endline
   
5. since all the lines are filtered then we join them again with a ' 'space

6. we made it string again

7. printing it again will show us each line in different row

8. closing the previous file

9. writing the converted file back to a new file

10. closing the file and thats it


there is an short way also to do this 

since, the lines read by the read() function 
are in the form of string so we can directly use the 
replace fn in that and remove all the . with \n

"""



"""
file=open("essay.txt",'r')
#print(file.read())
lines=file.read()
#print(lines)

lines=lines.split()

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
file=open("essay.txt",'r')
#print(file.read())
lines=file.read()
#print(lines)
lines=lines.replace('.','\n')
print(lines)
file.close()
file=open("Converted.txt",'w')
file.write(lines)
file.close()







