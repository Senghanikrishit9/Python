# Task

n = int(input("Enter the number :-"))

s = 0
for i in range(1,n):
    if n % i == 0:
        s = s + i

if s == n:
    print("perfect number")
else:
    print("looser")



n = int(input("Enter the number :-"))
count = 0

for i in range(n,n+1):
    if  n % i == 2:
        count = count + 1
if count == 2:
    print("prime number")
else:
    print("not a prime number")


s = input("Enter the name :-")
rev = ""
for i in range(len(s)-1,-1,-1):
    rev = rev + s[i]

if rev == s:
    print("palidrome")
else :
    print("Not palidrome")
    

       