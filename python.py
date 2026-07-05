# 1 . If else-statment

# TASK :-

# 1
gen = input ("please tell  your gender in (M or F) :- ")

if gen == "M" or gen =="m" :
    print("Hello Sir")
elif gen == "F" or gen == "f" :
    print("Hello Mam")
else :
    print("Hello Sir/Mam")


# 2

year = int(input("Enter the year :- "))

if year % 100 == 0 or  year % 4 == 0 :
    print("leap year")
elif year % 100 != 0 and year % 4 == 0 : 
    print("leap year")
else : 
    print("Not a leap year")


# 3

tem = int(input("Enter your temperature :-"))
 
if tem <= -5 or tem <= 5:
    print("its very cold")
elif tem <= 6 or tem <= 18:
    print("its cold") 
else :
    print("its hot")

