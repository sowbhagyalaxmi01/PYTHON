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