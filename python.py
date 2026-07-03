# TASK

# 1 . Check whether a number is postive or nagtive 
 
num = int(input("Enter your number :-"))
if num >= 0:
    print("you enter the postive number")
else:
    print("you enter the negative number")


# 2 . Check whether a number is divided by 3

num = int(input("Enter your number :-"))
if (num % 3 == 0):
    print("Enter number is divided by 3")
else:
    print("Enter number is not divided by 3")

# 3 . Ask for age and print  whether  the user  is a child  or adult


age = int(input("Enter your age :-"))

if (age >=18):
    print("you are adult")
else :
     print("you are child")

# 4 . Print "hello"  if the user Enter the name


name = input("enter your name :-")

print(f"hello :- {name}")