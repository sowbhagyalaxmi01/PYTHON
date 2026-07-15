# loops are used to execute a block of code repeatedly until condition meets.
# use:without loops,you would have to write same code multiple times.

# type of loops:
# 1.for loop-used to iterate over a sequence (like str,list,tuple,etc)
# 2.while loop-ecutes set of statements until condition True.

#for loop:
# 1.Using range()
for i in range(5): #for i in range(2, 6)#for i in range(2, 11, 2)#for i in range(1, 6)
    print(i)
#2.Loop through a String
name = "Python"
for ch in name:
    print(ch)
#3.Loop through a List
fruits = ["Apple", "Mango", "Banana"]
for fruit in fruits:
    print(fruit)
#Loop through a Tuple
numbers = (10, 20, 30)
for num in numbers:
    print(num)
#  Loop through a Set
colors = {"Red", "Blue", "Green"}
for color in colors:
    print(color)
#Loop through a Dictionary
student = {
    "name": "Ram",
    "age": 20
}
for key in student:
    print(key)


#while loop:
i = 1
while i <= 5:
    print(i)
    i += 1
#infinte loop
while True:
    print("Hello")


# Loop Control Statements
# 1.break-stop the loop immediately
for i in range(1, 6):
    if i == 4:
        break
    print(i)
 # 2. continue-Skips the current iteration.
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
# 3.pass-Does nothing. Used as a placeholder.
for i in range(5):
    pass

# nested loop:
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

# else with Loops
# the else block runs only if the loop finishes normally (without break).
for i in range(1, 4):
    print(i)
else:
    print("Loop completed")
#else does not execute when break stopped the loop. 