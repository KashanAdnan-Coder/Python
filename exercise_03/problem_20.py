"""
Write a program that checks if a customer is eligible for a discount based on their membership status and purchase amount:

If the customer is a member:
    If the purchase amount is $50 or more, print "Eligible for 10% discount".
    Otherwise, print "Eligible for 5% discount".
If the customer is not a member:
    If the purchase amount is $100 or more, print "Eligible for 5% discount".
    Otherwise, print "No discount".
"""

customer_member = input("are you a customer member: ")
purchase_amount = int(input("Enter purchase amount: "))

if customer_member.lower() == "yes" and purchase_amount >= 50:
    print("Eligible for 10% discount") 
elif customer_member.lower() == "no" and purchase_amount >= 100:
    print("Eligible for 5% discount")
else:
    print("No discount")