# Python Print statement
# In the print is keyword in python. Use print satement 
# and variable, values etc...
print ("My name is Purushoth")
print ("I am 22 years old")
print ("I am learning Python")
print ("My goal is to become a software developer")
print ("=" * 85) # This will print "=" 85 times

# Variables and data types
# Variables are used to store data in python.
# In python, we don't need to declare the variable type. 
# Python automatically detects the data type of the variable.

#Example of variables and data types

name = "Purushoth" # String
age = 22 # Integer
height = 5.9 # Float
married = False # Boolean

# Want know the data type of the variable, use type() function
print ("My name is", name, "and my data type is", type(name))
print ("My age is", age, "and my data type is", type(age))
print ("My height is", height, "and my data type is", type(height))
print ("Am I married?", married, "and my data type is", type(married))
print ("=" * 85)

# Get input from user
# In python, we can get input from user using input() function.
# Example of getting input from user
name = input("Enter your name: ")
age = input("Enter your age: ")
print ("My name is", name, "and I am", age, "years old.")

# Operators in Python
# In python, we have different types of operators.
# Example of operators in python

# 1. Arithmetic Operators
# In this operators are used to perform arithmetic operations. 
# like addition, subtraction, multiplication, division etc...
a = 10
b = 5
print ("Addition of a and b is", a + b) # Addition
print ("Subtraction of a and b is", a - b) # subtraction
print ("Multiplication of a and b is", a * b) # multiplication
print ("Division of a and b is", a / b) # division
print ("Modulus of a and b is", a % b) # Modulus
print ("Exponent of a and b is", a ** b) # Exponent here a is base and b is exponent
print ("Floor division of a and b is", a // b) # Floor division is used to get the quotient of the division without the remainder.
print ("=" * 85)

# 2. Comparison Operators
# In this operators are used to compare two values.
x = 10
y = 5
print ("Is x equal to y?", x == y) # Equal to
print ("Is x not equal to y?", x != y) # Not equal to
print ("Is x greater than y?", x > y) # Greater than
print ("Is x less than y?", x < y) # Less than
print ("Is x greater than or equal to y?", x >= y) # Greater than or equal to
print ("Is x less than or equal to y?", x <= y) # Less than or equal to
print ("=" * 85)

# 3. Logical Operators
# In this operators are used to combine conditional statements.
a = True
b = False
print ("a and b is", a and b) # and operator if the both are true then it will return true otherwise false
print ("a or b is", a or b) # or operator if any one of the condition is true then it will return true otherwise false
print ("=" * 85)

# 4. Assignment Operators
# In this operators are used to assign values to variables.
x = 5
print ("x is", x)
print ("x += 2 is", x + 2) # x = x + 2
print ("x -= 2 is", x - 2) # x = x - 2
print ("x *= 2 is", x * 2) # x = x * 2
print ("x /= 2 is", x / 2) # x = x / 2
print ("x %= 2 is", x % 2) # x = x % 2
print ("=" * 85)

# 5. Ternary Operator
# In this operator is used to evaluate a condition and return a value based on the condition.
age = 22
result = "You are eligible to vote" if age >= 18 else "You are not eligible to vote"
print (result)
print ("=" * 85)

# 6. Identity Operator
# In this operator is used to compare the memory location of two objects.
#  is and is not are the identity operators in python.

list1 = [1, 2, 3]

if 4 in list1:
    print ("2 is present in the list")
else:
    print ("2 is not present in the list")

print ("=" * 85)
