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
