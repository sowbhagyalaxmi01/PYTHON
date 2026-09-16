# 11.Write a Python program to calculate the final bill amount after applying a percentage discount to a product price.
#Discount means the customer gets money reduced from the original price.
price=60000
discount=20
discount_amount=price*discount/100
final_amount=price-discount_amount
print("final_bill_amount=",final_amount)


#12.Write a Python program to calculate GST for a service fee and display the final amount.
#gst is added to service_fee(GST is an extra tax, so it is added to the original fee.)
service_fee=24000
Gst=6
gst_amount=service_fee*Gst/100
final_amount=service_fee+gst_amount
print("GST amount =", gst_amount)
print("Final amount =", final_amount)


#13.Write a Python program to calculate the monthly subscription cost for a service from a yearly subscription price
#Yearly subscription ÷ 12 = Monthly subscription
yearly_subscription_price=12000
months=12
monthly_subscription=yearly_subscription_price/months
print(" monthly subscription cost:",monthly_subscription)



#14.Write a Python program that calculates the average rating from five customer ratings
#Parentheses make Python add all 5 ratings first, then divide the total by 5 to get the correct average(BODMAS) and if parth then it calculates division for e/5 following oof bodmas
a=int(input("enter customer 1 rating:"))
b=int(input("enter customer 2 rating:"))
c=int(input("enter customer 3 rating:"))
d=int(input("enter customer 4 rating:"))
e=int(input("enter customer 5 rating:"))
print((a+b+c+d+e)/5)


#15.Write a Python program to calculate profit or loss from cost price and selling price.
cp=12000
sp=15000
if sp>cp:
    print("profit=",sp-cp)
else:
    print("loss=",cp-sp)    



#16.Write a Python program to calculate the percentage increase in a product's price.    
product_price=26000
increased_by=2000
print("percentage increase=",increased_by/product_price*100)


#17.Write a Python program to convert an integer product ID stored as a string into an integer and add 100 to it.
product_ID="101"
print(int(product_ID)+100)


#18.Write a Python program that accepts a string price such as '1499.50', converts it to a float, and calculates a 10% discount
price = "1499.50"
price = float(price)
discount = price * 10 / 100
print("discount =", discount)#discount amount for price after discount:print(price - discount)


#19.Write a Python program to convert total minutes of customer support usage into hours and remaining 
minutes = 150
hours = minutes // 60
remaining = minutes % 60
print("hours =", hours)
print("remaining minutes =", remaining)


#20.Write a Python program to calculate the area and perimeter of a rectangular product package.
length=23
breadth=45
print("area=",length*breadth)
print("perimeter=",2*(length*breadth))


#21.Write a Python program to calculate compound growth of monthly users for one year using a given growth rate
users = 1000
growth_rate = 10
users = users * (1 + growth_rate / 100) ** 12#formula:Final = Initial × (1 + rate/100)^months
print(users)

#22.Write a Python program that uses arithmetic operators to calculate subtotal, discount, tax, and final bill.
total = 25000
discount = 10
tax = 230
discount_amount = total * discount / 100
subtotal = total - discount_amount#Original price − discount = Subtotal
final_bill = subtotal + tax
print("discount =", discount_amount)
print("subtotal =", subtotal)#Subtotal means the amount you have before adding tax or other extra charges.
print("tax =", tax)
print("final bill =", final_bill)



#23.Write a Python program to check whether a product price is greater than a given budget using comparison operators
product_price=5600
budget_price=5000
if product_price>budget_price:
    print("greater")
else:
    print("not greater") 


#24.Write a Python program to check whether a customer is eligible for a service based on age and a minimum score.
age = 20
score = 60
minimum_score = 35

if age >= 18 and score >= minimum_score:
    print("eligible")
else:
    print("not eligible")  



# 25.Write a Python program to determine whether a user qualifies for a premium plan using multiple conditions with and/or.
age = 22
score = 65
premium_member = True

if (age >= 18 and score >= 70) or premium_member:
    print("Qualifies for premium plan")
else:
    print("Does not qualify")