"""
Write a program that takes the total amount of a purchase as input and applies a discount:

If the amount is less than $100, no discount.
If the amount is between $100 and $500, apply a 10% discount.
If the amount is more than $500, apply a 20% discount.
Print the final amount after the discount.

"""

total_amount = int(input("Enter your total amount: "))
if total_amount <= 100:
    print("no discount")
elif total_amount > 100 and total_amount <= 500:
    discount = 10 
    print("You got 10% discount for this purchase")
elif total_amount > 500:
    discount = 20 
    print("You got 20% discount for this purchase")

discount_amount = total_amount * (discount / 100)

print(f"Your discount is : ${round(total_amount - discount_amount)}")