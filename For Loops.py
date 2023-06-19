import time

# for loops  a statment that will execute its block of code a limited amount of time
for i in range(10):
    print(i + 1)  # +1 is to make the loop stop at 10

for i in range(50, 100 + 1, 2):  # +1 is to make the loop stop at 10 (2 is to add i by 2)
    print(i)

for i in "Ajogu Joseph":  # count all the strings
    print(i)

for seconds in range(10, 0, -1):  # count from 10 to o (-1 to minus seconds by 1)
    print(seconds)
    time.sleep(1)  # wait on second before minusing 1
print("Happy new year!!!")
