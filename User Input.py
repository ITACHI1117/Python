# User Input

name = input("what is your name?: ")
age = int(input("how old are you?: "))
height = float(input("How tall are you?: `"))

print("Hello " + name)
print("You are  " + str(height) + " cm tall")
print("You are " + str(age) + " year old") # cannot conactinate int with string so the int has to be converted back to a string