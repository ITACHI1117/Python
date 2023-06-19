# KEYWORD ARGUMENTS = arguments preceded by an identifier when we pass them to a function
# The order of the arguments dose'nt matter , nunlike positional arguments
# Python know the names of the arguments that our function recieves

def hello(first, middle, last):
    print("Hello " + first + " " + middle + " " + last)


hello(last="CODE", middle="Dude", first="BRO")
