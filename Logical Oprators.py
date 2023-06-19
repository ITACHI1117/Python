# Logical Oprators (and, or not)

temp = int(input("what is the temp outside?: "))

if not(0 <= temp <= 30):
    print("The temp is good today!")
    print("Go out")
elif not(temp < 0 or temp > 30):
    print("The temp is bad today ")
    print("stay inside")
    