#dictionary{} are used to store data value in key:value pairs and are unordered ,mutable,dompt allow duplicates.


#Create a dictionary with keys "name", "college", and "city" and print it.
#print(student["name"])
# or
#print(student.get("name"))

student={
    "name":"sowbhagya",
    "college":"Gnit",
    "city":"hyderabad"
}
print(student["name"])
print(student.get("college"))
print(student["city"])


#Print the value of the key "college".
student={
    "name":"sowbhagya",
    "college":"Gnit",
    "city":"hyderabad"
}
print(student.get("college"))


#Add a new key "course" with value "Python".
student={
    "name":"sowbhagya",
    "college":"Gnit",
    "city":"hyderabad"
}
student.update({"course":"python"})#student["course"]="python"
print(student)

#Remove the "city" key.
student={
    "name":"sowbhagya",
    "college":"Gnit",
    "city":"hyderabad"
}
student.pop("city")#pop removes item
print(student)


#Check if the key "name" exists.
student={
    "name":"sowbhagya",
    "college":"Gnit",
    "city":"hyderabad"
}
if "name" in student:
    print("yes")
else:
    print("no")

   


#Print all the keys.
student={
    "name":"sowbhagya",
    "college":"Gnit",
    "city":"hyderabad"
}
print(student.keys())


#Print all the values.
student={
    "name":"sowbhagya",
    "college":"Gnit",
    "city":"hyderabad"
}
print(student.values())


#Print all key-value pairs using a loop.
student={
    "name":"sowbhagya",
    "college":"Gnit",
    "city":"hyderabad"
}
for key,value in student.items():#without loop print(student.items())  
    print(key,value)

         
#Count the number of key-value pairs.
student={
    "name":"sowbhagya",
    "college":"Gnit",
    "city":"hyderabad"
}
print(len(student))










