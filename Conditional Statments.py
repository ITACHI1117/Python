# Conditional statements
age = int(input("How old are you?: "))

# if and else statement

if age == 100:
    print("You are old")
elif age >= 18:
    print("You are an adult")
elif age < 0:
    print("You don't exist")
else:
    print("You are too young")
