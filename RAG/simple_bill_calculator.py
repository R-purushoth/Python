# declare value for meals tax_rate and tip persentage
meal_price = 500
tax_rate = 8
tip_percentage = 10

# calculate tax , tip and total
tax = meal_price * tax_rate/100
tip = meal_price * tip_percentage /100
total = meal_price + tax + tip
print (f"Meal: ${meal_price}")
print (f"Tax: ${tax}")
print (f"Tip: ${tip}")
print (f"Total price of your meals: ${round(total,2)}" )
