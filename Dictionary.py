# dictonary = A changeable unordered collection of unique key:value pairs
#            Fast beacuse they use hashing, allow us to access a value quickly

capitals = {'USA': 'Washington Dc',
            'India': 'New Dehli',
            'China': 'Benji',
            'Russia': 'Moscow'}

capitals.update({'Germany': 'Berlin'})  # adding new key value pair
capitals.update({'USA': 'Las Vegas'})  # updating a key value pair
capitals.pop('China')  # remove a key value pair
# capitals.clear()

print(capitals['Russia'])
print(capitals.get('Germeny'))
print(capitals.keys())  # display the keys only
print(capitals.values())  # display the values only
print(capitals.items())  # display all the key value pairs

for key, value in capitals.items():
    print(key, value)  # another method of displaying all the key value pairs
