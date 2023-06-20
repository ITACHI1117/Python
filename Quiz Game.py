def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------------------------")
        print(key)
        for i in options[0][question_num - 1]:
            print(i)
        guess = input("Enter a (A,B,C or D)")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess) # gettting the answewr from the dictonary key
        question_num += 1


    display_score(correct_guesses, guesses)


def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0


def display_score(correct_guesses, guesses):
    print("-----------------------------")
    print("RESULTS")

    print("Answers:", end="")
    for i in questions:
        print(questions.get(i), end="")
    print()

    print("Guesses:", end="")
    for i in guesses:
        print((i + " "), end="")
    print()

    scroe = int((correct_guesses / len(questions)) * 100)
    print("Your Score is: " + str(scroe) + "%")


def play_again():
    responce = input("Play again? (Y/N)")
    responce = responce.upper()

    if responce == "Y":
        return True
    else:
        return False


questions = {
    "Who created Python?: ": "A",
    "What year was python created?: ": "B",
    "Python is tribute to which comedy group?: ": "C",
    "Is the Earth round?: ": "D",
} # dictionary

options = [["A. Guido van Rossum", "B Elon Musk", "C Bill Gates", "D. MArk ZuckerBurg"],
           ["A. 1989", "B 1991", "C 2000", "D. 2016"],
           ["A. Lonely Island", "B Smosh", "C Monty Python", "D. SNL"],
           ["A. True", "B False", "C sometimes", "D. What's Earth"]], # List

new_game()
while play_again():
    new_game()

print("Byee")

