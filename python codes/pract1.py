num1=5
num2=10
print(num1+num2)

Math = int((input("Enter your marks")))

if (Math > 1 and Math <=49):
    print("Below Average")
if (Math > 50 and Math <= 69):
    print(" Your grade is B-")
elif (Math > 59 and Math <= 79):
    print("Your grade is B")
elif (Math > 79 and Math <= 89):
    print("Your grade is B+")
elif(Math > 89 and Math <=100):
    print("Your grade is A")
else:
    print("Invalid Marks")
    
    
#for loops in python.
fruit=["Oranges","Apple","Banana","Cherry"]
for i in fruit:
    print(i)
    
#looping  through a string
for i in "Banana":
    print(i)
for i in range(100):
    print(i)
    
for j in range(100):
    print(j)