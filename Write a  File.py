text = "have a good one\n bro"
with open('test.txt', 'a') as file:  # w for writing the file (a) for appending
    file.write(text)
