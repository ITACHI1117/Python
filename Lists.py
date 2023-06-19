# lists: is used to store multiple items within a single variable

food = ["pizza", "ham-burgers", "hot-dog", "sapgetti"]

food[0] = "sushi"

food.append("ice-cream")
food.remove("hot-dog")
food.pop()
food.insert(0, "cake")
food.sort()
# food.clear()

for i in food:
    print(i, end=",")


