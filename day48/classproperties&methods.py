class Student:
    
    def __init__(self, name, age):
        self.name = name       # property
        self.age = age         # property

    def study(self):           # method
        print(self.name, "is studying")


# Objects / Instances
s1 = Student("Rahul", 20)
s2 = Student("Priya", 21)

# Access properties
print(s1.name)
print(s1.age)

print(s2.name)
print(s2.age)

# Call method
s1.study()
s2.study()