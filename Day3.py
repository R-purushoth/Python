"""# looping continues until the user enters a valid input

# print 1 to 10 in loop mode
i = 1
while i <= 10:
    print (i)
    i+=1
print ("loop end..")

print ("=" * 85)


# print numbers 1 to 10 in reverse order
x = 10
while  x  >= 1 :
    print (x)
    x -= 1
print ("loop ended..")


# for Loop 

s1 = "KNACK"
s2 = "FORGEA"

result = []

for i in range (len(s1)):
    print (s1[i]+s2[i], end="")
#print (result)

print ()

for a,b in zip (s1,s2):
    result += a+b
result += "A"
print (result)

print ("=" * 85)

name = ["Purushoth" , "Kishore Kumar" , "Manjunath" ]
for i in name:
    print (i)

for i in range (len (name [0])):
    print (i)


print ("=" * 85)


"""
# Looping Statement Examples

# print 1 - 10 by using for loop..
for i in range (1, 11):
    print (i)

print ("Loop end...")
# print 1-10 by using while loop..

i = 1
while (i <= 10):
    print (i)
    i+=1

print ("Loop End...")

# print even number in between 1 - 20 by using for loop
for i in range (2, 21, 2):
    print (i)

print ("Loop End...")

# print odd number in between 1 - 20 by using for loop..
for i in range ( 1 , 20 , 2):
    print (i)
print ("=" * 85)

# print Even number in between 1 - 20 by using while loop. 

i = 2
while (i <= 20):
    if (i % 2 == 0 ):
        print (i)
        i += 2
print ("Loop end..")

# print Odd number in between 1 - 20 by using while loop

i = 1
while (i <= 20):
    if (i % 2 != 0):
        print (i)
