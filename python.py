# 1 . Loops

# 1. you spoat an accident ahead - youimmediately stop and 
# take  a U-Trun. loop ends completely

for i in range(1,11):
    if i == 6:
        break
    print(f"Stop number :- {i}")


# 2 . One signal is broken - you can skip it and keep driving 
# to the next one. loops skip  this iteration.


for i in range(1,16):
    if i == 10:
        continue
    print(f"total signal taken :- {i}")


# 3 . You crossed  all signals with no problems you reached home 
# safely . Runs only when loop finishes without any break

for i in range(1,11):
    if i == 12:
        break
    print(i)
else :
    print(f"total  signals crossed without any problems {i}")