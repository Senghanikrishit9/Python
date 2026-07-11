s = input("Enter the name :- ")
rev = ""
for i in range (len(s)-1,-1,-1):
    rev = rev + s[i]

if rev == s :
    print("palidrome ")
else :
    print("Not a palidrome")


a = "PYRrjahfff%^&@#dkjpvhg123456"

char = 0
spical = 0
apl = 0


for i in a:
    if(ord(i) >= 48 or ord(i) <= 57):
        print(f"char :- {char}")
    elif(ord(i) >= 65 or ord(i) <= 90) or (ord(i) >=97 and ord(i) <= 122):
        print(f"apl :- {apl}")
    else :
        print(f"spical :- {spical}")

