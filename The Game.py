import random
Players = int(input("Enter the number of players: "))
Board = {
    "Platforms": list(range(1, 101)),
    "Players": ()


}

Dice = (6)
Dice_number= random.randint(1, Dice)




if Players < 2:
    print("At least two players are required to play the game.")
    exit()

if Players == 2:
    Board["Players"] = ("Player 1", "Player 2")
    

            


# Player2 = (str(input("Player 2 Do you want to roll? ")), 0)
# if Player2 == "yes":
#             Player2 = (str(input("Player 2 rolled: ")), Dice_number)
    
    
    
    
    
    
    
if Players == 3:
        Board["Players"] = ("Player 1", "Player 2", "Player 3")
    
if Players == 4:
        Board["Players"] = ("Player 1", "Player 2", "Player 3", "Player 4")

        Player1 = (str(input("Enter the name of Player 1: ")), 0)
        Player2 = (str(input("Enter the name of Player 2: ")), 0)
        Player3 = (str(input("Enter the name of Player 3: ")), 0)
        Player4 = (str(input("Enter the name of Player 4: ")), 0)

        Player1 = (str(input("Player 1 Do you want to roll? ")), 0)
        Player2 = (str(input("Player 2 Do you want to roll? ")), 0)
        Player3 = (str(input("Player 3 Do you want to roll? ")), 0)
        Player4 = (str(input("Player 4 Do you want to roll? ")), 0)
        
        Player1 = (str(input("Enter the name of Player 1: ")), )
# Player2 = (str(input("Enter the name of Player 2: ")), )

Player1 = (str(input("Player 1 Do you want to roll?: ")),)
if Player1 ==("yes"):
             print ("Player 1 rolled: "), Dice_number, " and moved to position ", Player1[1] + Dice_number
            


             


