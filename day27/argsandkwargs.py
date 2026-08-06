#Combining *args and **kwargs
#You can use both *args and **kwargs in the same function.

#The order must be:
# 1.regular parameters
# 2.*args
# 3.**kwargs

#print all orders
def my_function(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")

#Sum marks and print details
def student(name,*marks,**details):
  total=0
  for mark in marks:
    total+=mark
  print("Name:",name)
  print("Total:",total)

  for key,value in details.items():
    print(key,":",value)

student("Anu",80,60,60,50,age=20,city="hyd")    


#Find average
def average(name,*marks,**info):
  total=0
  for mark in marks:
    total+=mark
  print("name:",name)
  print("average:",total/len(marks))
  print(info)

average("trisha",60,34,67,87,branch="cse",year=4)    

#Employee details
def employee(emp_id,*skills,**details):
  print("Employee ID:",emp_id)

  print("Skills:")
  for skill in skills:
    print(skill)

  print("Details:")
  for key,value in details.items():
    print(key,value)

employee(101,"python","dsa","sql",name="sri",salary="35000")


#Trace this call
#Python reads from left to right:
def demo(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

demo(10, 20, 30, 40, x=50, y=60)
#assigns:a = 10
# b = 20
# args = (30, 40)
# kwargs = {
#     "x": 50,
#     "y": 60
# }
#output:10
# 20
# (30, 40)
# {'x': 50, 'y': 60}