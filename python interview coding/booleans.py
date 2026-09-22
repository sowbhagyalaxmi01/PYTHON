#Write a Python program that returns True if a product is in stock and False otherwise.
stock_available = True
print(stock_available)


#: Check whether a customer can access a premium service based on subscription status.
premium_subscription = True
print(premium_subscription)

#: Check whether a coupon is valid when the coupon code matches and the order value meets the minimum amount.
coupon_code = "SAVE10"
entered_code = "SAVE10"
order_value = 1000
minimum_amount = 500

valid = entered_code == coupon_code and order_value >= minimum_amount

print(valid)


#Determine whether free delivery should be applied using Boolean conditions.
order_value = 600
minimum_amount = 500

free_delivery = order_value >= minimum_amount

print(free_delivery)

#Check whether a user qualifies for a product warranty based on purchase amount and warranty status.
purchase_amount = 1000
warranty_active = True

eligible = purchase_amount >= 500 and warranty_active

print(eligible)

#Determine whether a service request can be accepted when the customer is active and payment is completed.
customer_active = True
payment_completed = True

accepted = customer_active and payment_completed

print(accepted)

#Check whether a product is eligible for a return using purchase days and return policy status.
purchase_days = 10
return_days = 30
return_policy_active = True

eligible = purchase_days <= return_days and return_policy_active

print(eligible)

#Check whether a product is eligible for a return using purchase days and return policy status.
purchase_days = 10
return_days = 30
return_policy_active = True

eligible = purchase_days <= return_days and return_policy_active

print(eligible)


#: Determine whether a customer gets a premium discount if they are a member or their purchase exceeds a threshold.
member = False
purchase_amount = 2000
threshold = 1500

discount = member or purchase_amount > threshold

print(discount)

#Check whether a product launch can proceed when development is complete, testing is passed, and approval is received.
development_complete = True
testing_passed = True
approval_received = True

launch = development_complete and testing_passed and approval_received

print(launch)

#Create Boolean variables for payment_success, stock_available, and address_valid, then calculate whether an order can be placed.
payment_success = True
stock_available = True
address_valid = True

order_can_be_placed = payment_success and stock_available and address_valid

print(order_can_be_placed)

#Check whether a service booking is valid based on available slots and customer payment status.
slots_available = True
payment_completed = True

booking_valid = slots_available and payment_completed

print(booking_valid)

#Determine whether a support ticket should be marked urgent using priority and customer plan.
priority = "high"
customer_plan = "premium"

urgent = priority == "high" and customer_plan == "premium"

print(urgent)

#Accept a product rating and return whether the product qualifies as highly rated.
rating = 4.5

highly_rated = rating >= 4

print(highly_rated)

#Validate a service registration using username, email, and password conditions.
username = "laxmi"
email = "laxmi@gmail.com"
password = "abc12345"

valid = username != "" and "@" in email and len(password) >= 8

print(valid)

#Check whether a user is eligible for a free trial based on account status and previous trial usage.
account_active = True
previous_trial_used = False
eligible = account_active and not previous_trial_used
print(eligible)


## AND → both must be True
# a and b
# # OR → at least one must be True
# a or b
# # NOT → reverses True/False
# not a
# # Comparison
# a == b
# a != b
# a > b
# a < b
# a >= b
# a <= b