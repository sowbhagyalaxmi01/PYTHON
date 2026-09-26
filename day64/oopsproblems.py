
# ============================================================
# 1. CLASS AND OBJECT
# ============================================================
# Question:
# Create a class Student with name and age.
# Create an object and print the student's name and age.

class Student:
    pass

student = Student()
student.name = "Ravi"
student.age = 20

print(student.name)
print(student.age)


# ============================================================
# 2. __init__() METHOD
# ============================================================
# Question:
# Create a Student class using __init__().
# Store name and marks and print them.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

student = Student("Ravi", 85)

print(student.name)
print(student.marks)


# ============================================================
# 3. self KEYWORD
# ============================================================
# Question:
# Create a Product class with name and price.
# Use self to store and print the values.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

product = Product("Laptop", 50000)

print(product.name)
print(product.price)


# ============================================================
# 4. METHOD
# ============================================================
# Question:
# Create a Calculator class with an add() method.

class Calculator:
    def add(self, a, b):
        return a + b

calculator = Calculator()

print(calculator.add(10, 20))


# ============================================================
# 5. MULTIPLE METHODS
# ============================================================
# Question:
# Create a Calculator class with methods:
# add(), subtract(), multiply(), divide().

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

calculator = Calculator()

print(calculator.add(10, 5))
print(calculator.subtract(10, 5))
print(calculator.multiply(10, 5))
print(calculator.divide(10, 5))


# ============================================================
# 6. RECTANGLE AREA
# ============================================================
# Question:
# Create a Rectangle class with length and width.
# Create a method to calculate area.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rectangle = Rectangle(10, 5)

print(rectangle.area())


# ============================================================
# 7. PRODUCT TOTAL PRICE
# ============================================================
# Question:
# Create a Product class with name, price, and quantity.
# Calculate the total price.

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity

product = Product("Pen", 20, 5)

print(product.total_price())


# ============================================================
# 8. BANK ACCOUNT
# ============================================================
# Question:
# Create a BankAccount class.
# Store account holder name and balance.
# Display the details.

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def display(self):
        print("Name:", self.name)
        print("Balance:", self.balance)

account = BankAccount("Ravi", 10000)

account.display()


# ============================================================
# 9. DEPOSIT
# ============================================================
# Question:
# Create a BankAccount class with a deposit() method.
# Add the deposited amount to the balance.

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

account = BankAccount(10000)

account.deposit(5000)

print(account.balance)


# ============================================================
# 10. WITHDRAW
# ============================================================
# Question:
# Create a BankAccount class with a withdraw() method.
# Withdraw money only if sufficient balance is available.

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")

account = BankAccount(10000)

account.withdraw(3000)

print(account.balance)


# ============================================================
# 11. BASIC INHERITANCE
# ============================================================
# Question:
# Create a parent class Animal.
# Create a child class Dog that inherits from Animal.

class Animal:
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")


dog = Dog()

dog.eat()
dog.bark()


# ============================================================
# 12. VEHICLE AND CAR
# ============================================================
# Question:
# Create a Vehicle class with a drive() method.
# Create a Car class that inherits from Vehicle.

class Vehicle:
    def drive(self):
        print("Vehicle is driving")


class Car(Vehicle):
    pass


car = Car()

car.drive()


# ============================================================
# 13. INHERITANCE WITH __init__()
# ============================================================
# Question:
# Create a Person class with name and age.
# Create a Student class that inherits from Person.
# Add marks to Student.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks


student = Student("Ravi", 20, 85)

print(student.name)
print(student.age)
print(student.marks)


# ============================================================
# 14. super()
# ============================================================
# Question:
# Create a Person class with name and age.
# Create a Student class that uses super().
# Add marks to Student.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks


student = Student("Ravi", 20, 85)

print(student.name)
print(student.age)
print(student.marks)


# ============================================================
# 15. PRIVATE VARIABLE
# ============================================================
# Question:
# Create a class BankAccount with a private balance variable.

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def display_balance(self):
        print(self.__balance)


account = BankAccount(10000)

account.display_balance()


# ============================================================
# 16. GETTER AND SETTER
# ============================================================
# Question:
# Create a Student class with a private marks variable.
# Use getter and setter methods.

class Student:
    def __init__(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        self.__marks = marks


student = Student(80)

print(student.get_marks())

student.set_marks(90)

print(student.get_marks())


# ============================================================
# 17. METHOD OVERRIDING
# ============================================================
# Question:
# Create a parent class Animal with a sound() method.
# Override the sound() method in Dog.

class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


dog = Dog()

dog.sound()


# ============================================================
# 18. MULTIPLE CHILD CLASSES
# ============================================================
# Question:
# Create a parent class Animal.
# Create Dog and Cat child classes.
# Give each child class its own sound() method.

class Animal:
    pass


class Dog(Animal):
    def sound(self):
        print("Dog barks")


class Cat(Animal):
    def sound(self):
        print("Cat meows")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()


# ============================================================
# 19. POLYMORPHISM
# ============================================================
# Question:
# Create different classes with the same method name.
# Call the same method for different objects.

class Dog:
    def sound(self):
        print("Dog barks")


class Cat:
    def sound(self):
        print("Cat meows")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()


# ============================================================
# 20. POLYMORPHISM WITH AREA
# ============================================================
# Question:
# Create Circle and Rectangle classes.
# Both should have an area() method.

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


circle = Circle(5)
rectangle = Rectangle(10, 5)

print(circle.area())
print(rectangle.area())


# ============================================================
# 21. EMPLOYEE ANNUAL SALARY
# ============================================================
# Question:
# Create an Employee class with name and monthly salary.
# Calculate annual salary.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12


employee = Employee("Ravi", 30000)

print(employee.annual_salary())


# ============================================================
# 22. SHOPPING CART
# ============================================================
# Question:
# Create a ShoppingCart class.
# Add products and calculate the total price.

class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, name, price):
        self.products.append((name, price))

    def total(self):
        total = 0

        for name, price in self.products:
            total += price

        return total


cart = ShoppingCart()

cart.add_product("Laptop", 50000)
cart.add_product("Mouse", 1000)
cart.add_product("Keyboard", 2000)

print(cart.total())


# ============================================================
# 23. LIBRARY
# ============================================================
# Question:
# Create a Library class.
# Add books and display the books.

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            print(book)


library = Library()

library.add_book("Python")
library.add_book("Data Science")
library.add_book("Machine Learning")

library.display_books()


# ============================================================
# 24. ELECTRONIC PRODUCT WITH super()
# ============================================================
# Question:
# Create a Product class with name and price.
# Create an ElectronicProduct class that inherits from Product.
# Add warranty using super().

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ElectronicProduct(Product):
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty = warranty


product = ElectronicProduct("Laptop", 50000, 2)

print(product.name)
print(product.price)
print(product.warranty)


# ============================================================
# 25. STUDENT RESULT
# ============================================================
# Question:
# Create a Student class with name and marks.
# Create a method to determine whether the student passed or failed.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def result(self):
        if self.marks >= 40:
            print("Pass")
        else:
            print("Fail")


student = Student("Ravi", 75)

print(student.name)
print(student.marks)

student.result()
