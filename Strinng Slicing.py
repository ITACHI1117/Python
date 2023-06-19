# String Slicing: use to create a substring by extracting elements from a string
# indexing[] or slice()
# [start:stop:step]

name = "Aj Joe"

first_name = name[:2]
last_name = name[3:]
funky_name = name[::3] #whatch here again
reversed_name = name[::-1]
#
print(reversed_name)

website1 = "http://ajjoe.com"
website2 = "http://google.com"
website3 = "http://wiki.com"


slice = slice(7,-4)
print(website1[slice])
print(website2[slice])
print(website3[slice])