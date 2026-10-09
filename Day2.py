# Welcome to learn python of day two

# Decision Making statement
# conditions statements are used to perform different actions based on different conditions.
# 1. if statement

age = int (input ("Enter your age: ")) 
if  age >= 18:
    print ("you are eligible to vote")

print ("=" * 85)

# 2. if else statement --> in this condition statement we can check two conditions. 
# if the condition is true then it will execute the if block otherwise it will execute the else block.
age = int (input ("Enter your age: "))
if  age >= 18:
    print ("you are eligible to vote")
else:
    print ("you are not eligible to vote")

print ("=" * 85)

# 3. if elif else statement --> in this condition statement we can check multiple conditions.

# calcualte student grade based on marks
math_marks = 88
physics_marks = 92
chemistry_marks = 85

average_marks = (math_marks + physics_marks + chemistry_marks) / 3

if average_marks >= 90:
    print ("Your grade is A")
elif average_marks >= 80:
    print ("Your grade is B")
elif average_marks >= 70:
    print ("Your grade is C")
elif average_marks >= 60:
    print ("Your grade is D")
else:
    print ("Your grade is F")

# 4. Nested if statement --> in this condition statement we can check multiple conditions inside another condition.
year = int(input("Enter your age: "))
month = int(input("Enter month (1-12): "))
total_months = year *12 + month
age=total_months / 12

if age < 0:
    print("Invalid age entered.")
elif age >=0 and age < 1:
    print("You are a infant.")
elif age >=1 and age <=3:
    print("You are a toddler.")
elif age >=4 and age <=12:
    print("You are a children.")
elif age >=13 and age <=19:
    print ("You are a teenager.")
elif age >=20 and age <=29:
    print ("you are a young.")
elif age >=30 and age <= 49:
    print ("you are adult.")
elif age >=50 and age <= 64:
    print ("you are a middle-aged.")
elif age >=65 and age <= 74:
    print ("you are a senior Citizen.")
elif age >=75 and age <= 85:
    print ("you are a Old Age.")
elif age >=86 and age <= 99:
    print ("you are a very Old Age.")
else:
    print ("you are a Centenarian.")
