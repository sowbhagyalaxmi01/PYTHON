with open("day32.txt", "w") as file:
    file.write("I am learning Python")


with open("day32.txt", "r") as file:
    data = file.read()

print(data)    


with open("day32.txt", "a") as file:
    file.write("\nI am learning file handling")


with open("day32.txt", "a") as file:
    file.write("\nToday I learned append")    


with open("day32.txt", "r") as file:
    line1 = file.readline()
    print(line1)

    line2 = file.readline()
    print(line2)    


with open("day32.txt", "r") as file:
    lines = file.readlines()

print(lines)    