# Program to access a global variable inside a function
x=10
def show():
    print(x)
show()    

#problem 2 usage of local variable
x=10
def change():
    x=20
change()
print(x)    


#use of global keyword
x=10
def change():
    global x
    x=20
change()
print(x)       


#count usage to change global
count=0 #global
def increase():
    global count#usecof g;obal and Without global, Python would treat an assignment to count as creating a local variable.
    count+=1
increase()
increase()    
increase()
print(count)


#adding  global variable
score=50
def add_score():
   global score
   score+=10
add_score()
add_score()
print(score)

#subract global variable
balance=1000
def withdraw():
    global balance
    balance-=200
withdraw()
withdraw()
print(balance)    


#increase temp by 5
temperature=25
def increase_temp():
    global temperature
    temperature+=5
increase_temp()
print(temperature)


#add 50 points to bonus
points=100
def bonus():
    global points
    points+=50
bonus()    
bonus()    
bonus()    
print(points)


#double value by global variable
value=10
def double_value():
    global value
    value*=2
double_value()
double_value()
print(value)    


#total add 10 each time
total=0
def add():
    global total
    total+=10
add() 
add() 
add() 
add() 
add() 
print(total)

#increase and reset
count=0
def increment():
    global count
    count+=1
def reset():
    global count
    count=0
increment()
increment()
increment()
reset()
increment()
print(count)    


#square number
number=5
def square():
    global number
    number**=2
square()
print(number)    

#discount and price
price=100
def discount():
    global price
    price-=20
discount()
discount()   
print(price)

#depoist and withdraw funtions
balance=1000
def deposit(amount):
    global balance
    balance+=amount
def withdraw(amount):
    global balance
    balance-=amount
deposit(500)
withdraw(200)
deposit(300)
print(balance) 


#creating 3 funtions 
total=100
def add(x):
    global total
    total+=x
def subtract(x):
    global total
    total-=x
def multiply(x):
    global total
    total*=x    
add(50)
subtract(30)
multiply(2)
print(total)        


#Global + Multiple Functions + Parameters
balance=5000
def deposit(amount):
    global balance
    balance+=amount
def withdraw(amount):
    global balance
    balance-=amount
def apply_bonus(percent):
    global balance
    balance+=(balance * percent / 100)    
deposit(1000)
withdraw(500)
apply_bonus(10)
print(balance)

#global variable + local variable with the same name.
score=100
def game():
    score=50
    print(score+20)
game()
print(score)    

#global + local variable + function parameter
count = 10
def update(count):
    count += 5#you don't need global when you're only creating/using a local variable.
    print(count)
update(20)
print(count)

#global variable + local variable + parameter + multiple functions + global
value=10
def change(value):
    value+=5
    print(value)
def update():
    global value
    value *=2
change(20)
update()
print(value)        



