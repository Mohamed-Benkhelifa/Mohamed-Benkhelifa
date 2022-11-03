import random

print("The Rock Paper Scissors Game")
scissors = 1
paper = 3
rock = 2
user_input = 0

while user_input != -1:
    user_input = int(input("enter 2 to choose rock, 3 to choose paper, 1 to choose scissors or -1 to quit the game: "))
    computer_choice = random.randint(1,4)
    if user_input != -1:
        if user_input == 1:
            print("you chose scissors")
        elif user_input == 3:
            print("you chose paper")
        elif user_input == 2:
            print("you chose rock")
        if computer_choice == 1:
            print("computer chose scissors")
        elif computer_choice == 3:
            print("computer chose paper")
        elif computer_choice == 2:
            print("computer chose rock")

        #scissors
        if user_input == 1 and computer_choice == 1:
            print("it's a tie")
        elif user_input == 1 and computer_choice == 2:
            print("sorry you lose")
        elif user_input == 1 and computer_choice == 3:
            print("Congrats you win")

        #rock
        if computer_choice == 2 and user_input == 1:
            print("congrats you win")
        elif computer_choice == 2 and user_input == 2:
            print("it's a tie")
        elif computer_choice == 2 and user_input == 3:
            print("sorry you lose")

        #paper
        if computer_choice == 3 and user_input == 1:
            print("sorry you lose")
        elif computer_choice == 3 and user_input == 2:
            print("congrats you win")
        elif computer_choice == 3 and user_input == 3:
            print("it's a tie")
    
    if user_input == -1:
        print("")

print("Goodbye")