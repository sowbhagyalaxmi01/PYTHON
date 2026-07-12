# Student Management System

# int
student_id = 6658

# str
name = "Sowbhagya"

# float
cgpa = 9.0

# bool
is_placed = False

# list
subjects = ["Python", "SQL", "DSA"]

# tuple
grades = ("A", "A+", "B+")

# set
skills = {"Python", "SQL", "Python", "Git"}

# dict
student = {
    "ID": student_id,
    "Name": name,
    "CGPA": cgpa,
    "Placed": is_placed
}

# None
phone = None

print("----- Student Details -----")
print("ID:", student_id)
print("Name:", name)
print("CGPA:", cgpa)
print("Placed:", is_placed)
print("Subjects:", subjects)
print("Grades:", grades)
print("Skills:", skills)
print("Phone:", phone)

print("\nDictionary:")
for key, value in student.items():
    print(key, ":", value)

# List operations
subjects.append("AI")
subjects.remove("SQL")

# Set operation
skills.add("HTML")

# Dictionary update
student["CGPA"] = 9.10

print("\nUpdated Subjects:", subjects)
print("Updated Skills:", skills)
print("Updated Dictionary:", student)

# Membership
print("\nPython in skills?", "Python" in skills)

# Boolean condition
if student["CGPA"] >= 8:
    print("Excellent Student")
else:
    print("Needs Improvement")

# Type conversion
print("\nType Conversion")
print(int(9.8))
print(float(student_id))
print(str(student_id))
print(bool(name))