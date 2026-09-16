#1.	Write a Python program to print the company name, product name, and service name on separate lines
print("Company name: Amazon\nProduct name: Laptop\nService name: Google Drive")#by using \n nextline in one print statment

print("Company name: Amazon")
print("Product name: Laptop")
print("Service name: Google Drive")

#2.	Write a Python program that prints a formatted message using print() with multiple arguments.
name="sowbhagya"
course="btech"
print("my name is",name,"and i am pursing",course)#multiple arg
print("My name is", "Laxmi")#2 arg


#3.	Write a Python program to print the following output exactly: Product: AI Resume Builder | Status: Active.
a="AI Resume Builder"
b="Active"
print("product:",a,"|","status:",b)


#4.	Write a Python program that takes a user's name and prints a personalized welcome message
name=input("enter a name:")
print("welcome",name)


#5.	Write a Python program to read a product name, price, and quantity from the user and display them
a=input("enter product name:")
b=input("enter price:")
c=input("enter quantity:")
print("product name:",a)
print("price",b)
print("qunatity",c)


#6.	Write a Python program that calculates the total price of a product using price and quantity entered by the user
a=int(input("enter price:"))
b=int(input("enter quantity:"))
print("total price=",a*b)


#7.	Write a Python program to swap two variables without using a third variable.
a=2
b=3
a,b=b,a
print("a=",a,"b=",b)

#8.	Write a Python program to create variables for customer_name, product_name, quantity, and price, then display an invoice line.
# Invoice line = one item/charge in the bill(details of one product.)
customer_name = "Sowbhagya"
product_name = "Laptop"
quantity = 1
price = 50000
print(customer_name, "bought", quantity, product_name, "for", price)
#Invoice = complete bill(the complete bill, which can contain multiple products and a total.)
customer_name = "Sowbhagya"
product1 = "Laptop"
quantity1 = 1
price1 = 50000
product2 = "Mouse"
quantity2 = 2
price2 = 1000
total = (quantity1 * price1) + (quantity2 * price2)
print("INVOICE")
print("Customer:", customer_name)
print(product1, quantity1, price1)
print(product2, quantity2, price2)
print("Total:", total)


#9.	Write a Python program that checks the type of each of these values: 100, 99.99, 'Python', True.
a=100
b=99.99
c="python"
d=True
print(type(a),type(b),type(c),type(d))
print(type(a), "\n", type(b), "\n", type(c), "\n", type(d))#bu using \n


#10.Write a Python program that stores a service name and service fee in variables and prints them in a readable format.
service_name = "Internet Service"
service_fee = 500
print("Service Name:", service_name)
print("Service Fee:", service_fee)