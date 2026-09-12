#File modes
#Read a file

f = open("day20/funtions.py", "r")
print(f.read())
f.close()


#Read only a certain number of character(reads upto particular lines mentioned in read())
f = open("day20/funtions.py", "r")
print(f.read(5))
f.close()


#Read one line(read line())
f = open("day20/funtions.py", "r")
print(f.readline())
f.close()


#Read all lines(readlines()) returns line as list
f = open("day20/funtions.py", "r")
print(f.readlines())
f.close()


#write file(the whole content will be replaced by now write content)
f = open("demofile.txt", "w")
f.write("Hello Python!")
f.close()


#+append to file(add to existing content)If you don't want to remove the existing content, use:"a"
f = open("demofile.txt", "a")
f.write("\nNew line")
f.close()


#CREATE a File
f = open("myfile.txt", "x")
f.close()


#Create Using "w"
f = open("myfile.txt", "w")
f.close()

#Mode	If file doesn't exist	If file exists
# x	Creates                   	Error
# w	Creates                 	Overwrites


#DELETE a File(os module used to delete file)
import os
os.remove("myfile.txt")


#Check Whether File Exists Before Deleting
import os

if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
else:
    print("The file does not exist")



#Delete a Folder(os.rmdir() only removes an empty directory)
import os
os.rmdir("myfolder")    


#Professional Way: with open()(Because Python automatically closes the file after the with block.)
with open("demofile.txt", "r") as f:
    print(f.read())



#file cursor
# 1.tell()
# tell() tells you the current position of the cursor.    
f = open("demo.txt", "r")

print(f.tell())

f.close()


#hello world
#2. read() moves the cursor
f = open("demo.txt", "r")
print(f.tell())   # 0
f.read(5)
print(f.tell())   # 5
f.close()


#3. seek()
#seek() is used to move the cursor to a particular position.
f = open("demo.txt", "r")
f.seek(0)#begging
print(f.read())
f.close()