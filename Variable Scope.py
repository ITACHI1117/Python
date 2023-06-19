# variable scope = The region a variable is recognized
# A variable is only available from inside a region it is created
# A global and locally scoped version of a variable can be created

name = "Bro"


def display_name():
    name = "Code"
    print(name)


display_name()
print(name)
