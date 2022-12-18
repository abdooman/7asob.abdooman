import imp


import random
name = input("please enter your name: ")
print("Hello "+ name + " good luck")

names_list = ["Sara", "Ahmad", "Omar", "Abdullrhman", "Ali"]

word = random.choice(names_list) 
print("the name is: ")
guesses = ''

turns = 12 

while turns > 0:

    failed = 0

    for char in word :
        if char in guesses:
            print(char)

        else:
            print("_")
            failed += 1

    if failed == 0:
        print("Good job")
        print("the name is: ", word)
        break

    guess = input("guess a character:")
    
    guesses += guess

    if guess not in word:
       turns -=1 
       print("worng guess, try agin")
       print("you have", + turns, "more guesses")

       if turns == 0:
        print("You loose")