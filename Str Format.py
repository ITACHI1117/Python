# str.format() = optional method that gives users more control when displaying output

number = 1000
animal = "dog"
item = "box"

print("The {} jumped over the {}".format(animal, item))
print("The {1} jumped over the {0}".format(animal, item))  # positional arguments (the same arguments can be used)
print("The {animal} jumped over the {item}".format(animal="cow",
                                                   item="box"))  # keyword argument (the same arguments can be used)
print("The number pi is {}".format(number))

text = "The {} jumped over the {}"
print(text.format(animal, item))

name = "Bro"
print("hello my name is {}".format(name))
print("hello my name is {:10} nice to meet you".format(name))

print("The number pi is{: 3.3f}".format(number))
print("The number  is {:,}".format(number))
print("The number  is {:b}".format(number))  # binary
print("The number  is {:o}".format(number))
print("The number  is {:X}".format(number))
