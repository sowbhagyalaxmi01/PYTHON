#string is a data type that stores a sequence of characters and enclosed by ' ' or " " or """ """
    # name="hello world"
#   Ordered (characters have positions/indexes)
#   Immutable (cannot be changed after creation)
#   Supports indexing and slicing
#   Can contain letters, numbers, symbols, and spaces

# Basic operators:
#   1.Indexing(postion of string and starts with 0 indexing)
#     eg:str="hello world"
#      ch=str[0]#h
#      print(ch)
#      text="python"
#       print(text[0])#p
#       print(text[3])#h

#   2.slicing(to find substring)
#     str[start idx:end idx] #ending idx not included
#     eg:str="hello world"
#        print(str[1:4])#ell
#        print(str[:5])#str[0:5]#hell
#        print(str[6:])#str[5:len(str)]
#   3.negative slicing(slice starts from end of string and right to left from -1)
#      eg:b="letter"
#         print(b[-5:-2])#ett
#   4.Concatenation(combine of string by +operators)
    #  eg: a="hello"
    #      b="world"
    #      print(a+b)#helloworld
    #      print(a+" "+b)#hello world
    # 5.length of str(len())
    #    eg: str1="apna"
    #        print(len(str1))#4
       
       