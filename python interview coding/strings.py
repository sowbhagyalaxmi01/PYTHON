#26.	Write a Python program to take a product name and print its first character, last character, and length.
product = input("Enter product name: ")

print("First character:", product[0])
print("Last character:", product[-1])
print("Length:", len(product))

#27.	Write a Python program to extract the first five characters of a service description using string slicing.
service = input("Enter service description: ")
print(service[:5])

#28.	Write a Python program to print the last three characters of an order ID using negative indexing.
order_id = input("Enter order ID: ")
print(order_id[-3:])


#29.	Write a Python program to reverse a product name using string slicing.
product = input("Enter product name: ")
print(product[::-1])


#30.	Write a Python program to check whether a customer email contains '@'.
email = input("Enter email: ")

if "@" in email:
    print("Contains @")
else:
    print("Does not contain @")


#31.	Write a Python program to convert a product name to uppercase and lowercase.
product = input("Enter product name: ")

print("Uppercase:", product.upper())
print("Lowercase:", product.lower())


#32.	Write a Python program to remove leading and trailing spaces from a customer-entered product name.
product = input("Enter product name: ")

product = product.strip()

print(product)


#33.	Write a Python program to replace the word 'Basic' with 'Premium' in a service plan name.
plan = input("Enter service plan: ")

plan = plan.replace("Basic", "Premium")

print(plan)
#34.	Write a Python program to count how many times the letter 'a' appears in a product description.
description = input("Enter product description: ")

count = description.count("a")

print("Number of a:", count)

#35.	Write a Python program to find the position of the word 'AI' in a service description.
description = input("Enter service description: ")

position = description.find("AI")

print("Position:", position)


#36.Write a Python program to split a comma-separated list of product names into separate values.
products = "Laptop,Mobile,Keyboard,Mouse"

result = products.split(",")

print(result)


# 37.	Write a Python program to join three service names into one string separated by ' | '.
service1 = "Cleaning"
service2 = "Repair"
service3 = "Delivery"

result = " | ".join([service1, service2, service3])

print(result)

# 38.	Write a Python program to check whether a product code starts with 'PRO'.
code = "PRO12345"

print(code.startswith("PRO"))

# 39.	Write a Python program to check whether a service code ends with '2026'.
code = "SERVICE2026"

print(code.endswith("2026"))

# 40.	Write a Python program to capitalize the first letter of each word in a customer name.
name = "hunaji sowbhagya laxmi"

result = name.title()

print(result)


# 41.	Write a Python program to format a customer invoice using an f-string with customer name, product, quantity, and total.
name = "Hunaji"
product = "Laptop"
quantity = 2
total = 100000

print(f"Customer: {name}")
print(f"Product: {product}")
print(f"Quantity: {quantity}")
print(f"Total: ₹{total}")


# 42.	Write a Python program to generate a product summary using the format() method.
product = "Laptop"
price = 50000
quantity = 2

result = "Product: {}, Price: {}, Quantity: {}".format(product, price, quantity)

print(result)

# 43.	Write a Python program to display a price with exactly two decimal places using string formatting.
price = 125.5

print(f"{price:.2f}")

# 44.	Write a Python program to mask a customer phone number so that only the last four digits are visible.
phone = "9876543210"

result = "*" * 6 + phone[-4:]

print(result)


# 45.	Write a Python program to extract the domain name from an email address such as 'user@company.com'.
email = "user@company.com"

domain = email.split("@")[1]

print(domain)


# 46.	Write a Python program to check whether a given string is a palindrome using slicing.
word = "madam"

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


# 47.	Write a Python program to count the number of words in a service description.
description = "We provide fast home cleaning service"

words = description.split()

print(len(words))


# 48.	Write a # Python program to remove all spaces from a product code.
code = "PRO 2026 ABC"

result = code.replace(" ", "")

print(result)


# 49.	Write a Python program to create a URL-friendly product slug from a product name.
product = "Best Laptop 2026"

slug = product.lower().replace(" ", "-")

print(slug)


# 50.	Write a Python program to compare two product names after converting them to lowercase and removing extra spaces.
product1 = "  Gaming Laptop  "
product2 = "gaming laptop"

p1 = product1.strip().lower()
p2 = product2.strip().lower()

print(p1 == p2)