# data types

# first_name = "bros"
# last_name = "bras"
# full_name = first_name +" "+ last_name
# print("Hello " + full_name)

# age = 22
# age += 1
# print(age)
# print(type(age))
# print("Your age is: " + str(age))

# height = 350.5
# print("Your height is: " + str(height)+"cm")
# print(height)

# human = True
# print("Are you a Human " + str(human))
# print(human)


# multiple assigment

# name = "joe"
# age = 21
# attractive = True

# name, age, attractive = "Bro", 21, True
#
# print(name)
# print(age)
# print(attractive)
#
#
# aj = emma = bless  = debbi = 30
# print(aj)


# String methods

# name = "bro Code"
# print(len(name)) #Length method
# print(name.find("o"))
# print(name.capitalize()) #if there is any space or additional words it wont captialze
# print(name.upper())
# print(name.lower())
# print(name.isdigit())
# print(name.isalpha())
# print(name.count("o"))
# print(name.replace("o","a"))
# print(name*3)


# TypeCasting = Coverting the data type of a value to another data type

# x = 1
# y = 2.0
# z = "3"
#
# x = float(x)
# y = int(y)
# z = int(z)
#
# print(x)
# print(y)
# print(z*3)

# User Input

# name = input("what is your name?: ")
# age = int(input("how old are you?: "))
# height = float(input("How tall are you?: `"))
#
# print("Hello " + name)
# print("You are  " + str(height) + " cm tall")
# print("You are " + str(age) + " year old") # cannot conactinate int with string so the int has to be converted back to a string

# math functions
# import math
#
# pi = 3.14
# x = 1
# y = 2
# z = 3
#
# print(round(pi))
# print(math.ceil(pi))
# print(math.floor(pi))
# print(abs(pi))
# print(pow(pi,2))
# print(math.sqrt(pi))
# print(max(x,y,z))
# print(min(x,y,z))


# String Slicing: use to create a substring by extracting elements from a string
# indexing[] or slice()
# [start:stop:step]

# name = "Aj Joe"
#
# first_name = name[:2]
# last_name = name[3:]
# funky_name = name[::3] #whatch here again
# reversed_name = name[::-1]
# #
# print(reversed_name)

# website1 = "http://ajjoe.com"
# website2 = "http://google.com"
# website3 = "http://wiki.com"
#
#
# slice = slice(7,-4)
# print(website1[slice])
# print(website2[slice])
# print(website3[slice])


# Conditional statements
# age = int(input("How old are you?: "))
#
# # if and else statement

# if age == 100:
#     print("You are old")
# elif age >= 18:
#     print("You are an adult")
# elif age < 0:
#     print("You don't exist")
# else:
#     print("You are too young")


# Logical Oprators (and, or not)

# temp = int(input("what is the temp outside?: "))
#
# if not(temp >= 0 and temp <= 30):
#     print("The temp is good today!")
#     print("Go out")
# elif not(temp < 0 or temp > 30):
#     print("The temp is bad today ")
#     print("stay inside")


# while Loops a statment that will execute its block of code a unlimited amount of time
# name = ""
# while len(name) == 0:
#     name = input("Enter your name: ")
# print("Hello "+name)
#
# second_name = None
# while not second_name :
#     second_name = input("Enter your second name: ")
# print("Hello "+second_name)

# for loops  a statment that will execute its block of code a limited amount of time
# for i in range(10):
#     print(i+1) #+1 is to make the loop stop at 10

# for i in range(50,100+1,2):  #+1 is to make the loop stop at 10 (2 is to add i by 2)
#      print(i)

# for i in "Ajogu Joseph": # count all the strings
#     print(i)

# import time
# for seconds in range(10,0,-1): # count from 10 to o (-1 to minus seconds by 1)
#     print(seconds)
#     time.sleep(1) # wait on second before minusing 1
# print("Happy new year!!!")

# Nested loops

# rows = int(input("How many rows: "))
# columns = int(input("How many columns: "))
# symbol = input("Enter a symbol to use: ")
#
# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end="") #(end="" prevents coursor from moving to the next line in the terminal)
#     print()

# Loop control Statements: use to change a loop execution from its normal sequence

# break: used to terminate the loop entirely
# continue: skips to the next iteration of the loop
# pass: does nothing, acts as a placeholder

# while True:
#     name = input("enter your name")
#     if name !="":
#         break

# phone_number = "123-456-789"
#
# for i in phone_number:
#     if i == "-":
#         continue
#     print(i, end=" ")


# for i in range(1,21):
#     if i == 13:
#         pass
#     else:
#         print(i)


# lists: is used to store multiple items within a single variable

# food = ["pizza","ham-burgers","hot-dog","sapgetti"]
#
# food[0] = "sushi"
#
# food.append("ice-cream")
# food.remove("hot-dog")
# food.pop()
# food.insert(0,"cake")
# food.sort()
# food.clear()
#
# for i in food:
#     print(i, end=",")


# 2D lists = lists of lists (multi Dimensional lits)

# drinks = ["coffe", "soda","tea"]
# dinner = ["pizza","ham","hotdog"]
# dessert = ["cake", "icecream"]
#
# food = [drinks,dinner,dessert]
#
# print(food[1][0]) # this will print the second list and the first item in that list


# tuple = collection which is oderded and unchangeable
# used tp group toghter related data

# student = ("Bro",21,"male")
#
# print(student.count("Bro"))
# print(student.index("male"))
#
# for x in student:
#     print(x)
#
# if "Bro" in student:
#     print("Bro is here!")


# Set: Collection which is unordered, unindexed. No duplicate values

# utensils = {"fork","spoon","kinfe"}
# dishes = { "bowl","spoon","plate","cup"}

# utensils.add("napkin")
# utensils.remove("fork")
#  utensils.clear()
# utensils.update(dishes)
# dinner_table = utensils.union(dishes)

# for x in dinner_table:
#     print(x)

# print(dishes.difference(utensils))
# print(utensils.intersection(dishes))

# dictonary = A changeable unordered collection of unique key:value pairs
#            Fast beacuse they use hashing, allow us to access a value quickly

# capitals = {'USA':'Washington Dc',
#             'India': 'New Dehli',
#             'China':'Benji',
#             'Russia':'Moscow'}
#
# capitals.update({'Germany':'Berlin'}) # adding new key value pair
# capitals.update({'USA':'Las Vegas'}) # updating a key value pair
# capitals.pop('China') # remove a key value pair
# # capitals.clear()
#
# print(capitals['Russia'])
# print(capitals.get('Germeny'))
# print(capitals.keys()) # display the keys only
# print(capitals.values()) # display the values only
# print(capitals.items()) #display all the key value pairs
#
# for key, value in capitals.items():
#     print(key,value) # another method of displaying all the key value pairs


# index operator []: gives access to a sequence's element (str,list,tuples)

# name = "joey joe!"

# if(name[0].islower()):
#     name = name.capitalize()

# first_name = name[:4].upper()
# last_name = name[5:]
# last_character = name[-1]
#
# print(name)
# print(first_name)
# print(last_name)
# print(last_character)


# functions
# def hello(name):
#     print("hello@! "+ name)
#
# name = input("enter Your name: ")
# hello(name)

# return statments:

# def multiply(number1, number2):
#     return  number1 * number2
#
# x = multiply(6,8)
# print(x)


# KEYWORD ARGUMENTS = arguments preceded by an identifier when we pass them to a function
# The order of the arguments dose'nt matter , nunlike positional arguments
# Python know the names of the arguments that our function recieves

# def hello(first, middle, last):
#     print("Hello " + first + " " + middle + " " + last)
#
# hello(last="CODE", middle="Dude", first="BRO")
#
#
# # POSITIONAL ARGUMENTS
# def hello(first, middle, last):
#     print("Hello " + first + " " + middle + " " + last)
# hello("CODE", "Dude", "BRO")


# nested functions calls

# num = input("enter a whole positive number: ")
# num = float(num)
#
# print(round(abs(float(input("enter a whole positive number: ")))))

# variable scope = The region a variable is recognized
# A variable is only available from inside a region it is created
# A global and locally scoped version of a variable can be created

# name = "Bro"
# def display_name():
#     name = "Code"
#     print(name)
#
# display_name()
# print(name)

# *args = parameter that will pack all arguments into a tuple useful so that a function can accept a varying ammount
# of arguments

# def add(*stuff):
#     sum = 0
#     stuff = list(stuff)
#     stuff[0] =0
#     for i in stuff:
#         sum += i
#     return sum
#
#
# print(add(1, 2, 3, 4, 5, 6))

# **kwargs = parameter that will pack all arguments into a dictionary useful so that a function can accept a varying
# amount of keyword arguments

# def hello(**kwargs):
#     print("Hello "+kwargs['first']+" "+kwargs['last'])
#     print("Hello", end=" ")
#     for key, value in kwargs.items():
#         print(value, end=" ")
#
# hello(title="Mr.",first="Bro", middle="danny", last="Jane")


# str.format() = optional method that gives users more control when displaying output

number = 1000
animal = "dog"
item = "box"

# print("The {} jumped over the {}".format(animal, item))
# print("The {1} jumped over the {0}".format(animal, item)) #positional arguments (the same arguments can be used)
# print("The {animal} jumped over the {item}".format(animal="cow", item="box")) #keyword argument (the same arguments can be used)
# print("The number pi is {}".format(number))


# text = "The {} jumped over the {}"
# print(text.format(animal,item))
#
# name = "Bro"
# print("hello my name is {}".format(name))
# print("hello my name is {:10} nice to meeet you".format(name))
#
#
# number = 1000
# print("The number pi is{: 3.3f}".format(number))
# print("The number  is {:,}".format(number))
# print("The number  is {:b}".format(number)) # binary
# print("The number  is {:o}".format(number))
# print("The number  is {:X}".format(number))


# Random method

# import random
# x = random.randint(1,6)
# y = random.random()
#
# mylist = ['rock','paper','sissors']
# z = random.choice(mylist)
#print(z)

# cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
#
# random.shuffle(cards)
# print(cards)


#exception handling: an exception is an event dected during excution that interrupt the flow of a program

# try:
#    numerator = int(input("Enter a number to divide: "))
#    denominator = int(input("Enter a number to divide by: "))
#    result = numerator / denominator
#
# except ZeroDivisionError as e:
#     print(e)
#     print("You cant divide by zero")
#
# except ValueError as e:
#     print(e)
#     print("Enter numbers only")
#
# except Exception as e:
#     print(e)
#     print("Something went wrong")
# else:
#     print(result)
# finally:
#     print("Executed")