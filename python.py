# 1 . Loops

# 1. print "hello world" n times

n = int(input("Enter your number :-"))

for i in range(n):
    print(f"hello world :- {i} times")

# 2. print natural number  form  1 to n

n = int(input("Enter the number :-"))

for i in range(1,n+1):
    print(i)
 
# 3.  Reversed for loop  - print  n down to 1


n  = int(input("Enter your number :-"))

for i in range(n,0,-1):
    print(i)

# 4 . miltipilation task

n = int(input("Enter the number :-"))

for i in range(1,11,):
    print(f"{n} x {i} = { n* i}")