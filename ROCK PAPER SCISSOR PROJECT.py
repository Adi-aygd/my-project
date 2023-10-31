print("---------------WELCOME TO ROCK,PAPER,SCISSOR----------------")
import random
exit=False
user_points=0
computer_points=0
while exit==False:
    options=["rock", "paper", "scissor"]
    user_input=input("Choose rock(🪨),paper(📰),scissor(✂),exit : ")
    computer_input=random.choice(options)
    if user_input=="exit":
        print("---GAME ENDED---")
        print("You won a total score of "+str(user_points)+" and the computer total score is "+str(computer_points))
        exit=True
    elif user_input =="rock":
        if computer_input=="rock":
            print("Your input is rock")
            print("Computer input is rock")
            print("It is a tie!!")
        elif computer_input=="paper":
            print("Your input is rock")
            print("Computer input is paper")
            print("Computer won!!")
            computer_points +=1
        elif computer_input=="scissor":
            print("Your input is rock")
            print("Computer input is scissor")
            print("You won!!")
            user_points +=1
    elif user_input =="paper":
        if computer_input=="rock":
            print("Your input is paper")
            print("Computer input is rock")
            print("You won!!")
            user_points +=1
        elif computer_input=="paper":
            print("Your input is paper")
            print("Computer input is paper")
            print("It is a tie!!")
        elif computer_input=="scissor":
            print("Your input is paper")
            print("Computer input is scissor")
            print("Computer wons!!")
            computer_points +=1
    elif user_input =="scissor":
        if computer_input=="rock":
            print("Your input is scissor")
            print("Computer input is rock")
            print("Computer won!!")
            computer_points +=1
        elif computer_input=="paper":
            print("Your input is scissor")
            print("Computer input is paper")
            print("You won!!")
            user_points+=1
        elif computer_input=="scissor":
            print("Your input is scissor")
            print("Computer input is scissor")
            print("It is a tie!!")
    elif (user_input !="rock" or user_input !="paper" or user_input !="scissor"):
        print("INVALID !!")

        
            
