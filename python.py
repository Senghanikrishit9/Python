# Task

# 1 . tASK :-

a = 0
b= 0
n = int(input("Enter the number :-"))
 
for i in range(1,n+1):
    a = a + i
    b = b + i
    if a % 2 == 0:
        print(f"even number :- {a}")
    else:
        print(f"odd number  :- {b}")

# 2 .tASK :-

s = 1
n = int(input("Enter a number :-"))

for i in range(1,n+1):
    s = s*i
    print(s)

# 3 . TASk : -

a = 0
n = int(input("Enter the number :-"))

for i in range(1,n +1):
    a = a +i
    print(a)

# 4 .Task :-
 
n = int(input("Enter the number :-"))

for i in range(1,n+1):
    if n % i == 0:
        print(i)