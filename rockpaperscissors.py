 



from random import randint


option = ["rock", "paper", "scissors"]
computer = option[randint(0,2)]
player = False
while player == False:
    player = input("rock, paper, scissors")
    if player == computer:
        print("tie!")
    elif player == "rock":
        if computer == "paper":
            print("You lose!", computer, "beats", player)
        else:
            print("You win!", player, "beats", computer)
    elif player == "paper":
        if computer == "scissors":
            print("You lose!", computer, "beats", player)
        else:
            print("You win!", player, "beats", computer)
          
    elif player == "scissors":
        if computer == "rock":
            print("You lose", computer, "beats", player)
        else:
            print("You win!", player, "beats", computer)
    else:
        print("That's not a valid play!")
    
player = False
computer = option[randint(0,2)]
