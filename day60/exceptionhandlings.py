#Exception Handling
# If data.txt doesn't exist, Python gives:
# FileNotFoundError
# Instead of allowing the program to stop, we can handle it.
# used Exception handling prevents expected runtime errors from unnecessarily crashing your program.
#withexception handling
# Program
#   ↓
# Error occurs
#   ↓
# Handle the error
#   ↓
# Program continues safely



#Common File Errors
# Error	           Meaning
# FileNotFoundError	File doesn't exist
# FileExistsError	File already exists
# PermissionError	You don't have permission
# IsADirectoryError	Expected file but got directory
# NotADirectoryError	Expected directory but got file
# UnicodeDecodeError	Problem decoding text


# 3types:
# try     → try the operation
# except  → handle the error
# finally → always execute

#1. try and except
try:
    f = open("abc.txt", "r")
    print(f.read())
except:
    print("File not found")#If abc.txt doesn't exist:File not found.The program doesn't crash.


#Use the Specific Error
#instead of except: it's better to specify the expected exception:
try:
    f = open("abc.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("File not found")


# 3.finally
# finally runs whether an error occurs or not.
try:
    f = open("abc.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("File not found")
finally:
    print("Finished")
# If the file doesn't exist:
# File not found
# Finished
# If it exists:
# file contents
# Finished



#. with open() + Exception Handling
try:
    with open("abc.txt", "r") as f:
        data = f.read()
        print(data)

except FileNotFoundError:
    print("File not found")


#Easy Memory Trick
# try
#  ↓
# "Try this file operation"
# except
#  ↓
# "Something went wrong"
# finally
#  ↓
# "Do this anyway"    