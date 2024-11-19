#Rock-Paper-Scissor game
import random
#Game rules and points 
'''
    --> "Wining rules"
1) Rock bits the Scissor
2) Scissor bits the Paper
3) Paper bits the Rock

    --> "Points for win and loss"
1> If you won you got 10 points and computer got 0 point
2> If you loss you got 0 point and computer got 10 points
3> If match is drawn then both are got 5 points
'''
def computerChoiseMethod():
    #logic for the computer choosing random choise
    ComputerChoiseSet = ["Rock","Paper","Scissor"]
    computerChoise = random.choice(ComputerChoiseSet)
    return computerChoise
def userChoiseMethod():
        #use choise
    userChoise = input("Enter the choise: ")
    userChoise = userChoise.capitalize()
    return userChoise
userPoints = 0
computerPoints = 0
bestOfFive = 0

def gameLogics(userPoints,computerPoints,bestOfFive):
    while bestOfFive<5:
        print()
        computerChoise = computerChoiseMethod()
        #print(computerChoise)
        userChoise = userChoiseMethod()
        if computerChoise=="Rock" and userChoise=="Rock":
            print("Computer selected ",computerChoise," Both are win for this turm.")
            userPoints = userPoints+5
            computerPoints = computerPoints+5
        elif computerChoise=="Rock" and userChoise=="Paper":
            print("Computer selected ",computerChoise," you are win for this turm")
            userPoints = userPoints+10
        elif computerChoise=="Rock" and userChoise=="Scissor":
            print("Computer selected ",computerChoise," Computer is win for this turm.")
            computerPoints = computerPoints+10
        elif computerChoise=="Paper" and userChoise=="Rock":
            print("Computer selected ",computerChoise," Computer is win for this turm.")
            computerPoints = computerPoints+10
        elif computerChoise=="Paper" and userChoise=="Paper":
            print("Computer selected ",computerChoise," Both are win for this turm.")
            userPoints = userPoints+5
            computerPoints = computerPoints+5
        elif computerChoise=="Paper" and userChoise=="Scissor":
            print("Computer selected ",computerChoise," You are win for this turm")
            userPoints = userPoints+10
        elif computerChoise=="Scissor" and userChoise=="Rock":
            print("Computer selected ",computerChoise," You are win for this turm")
            userPoints = userPoints+10
        elif computerChoise=="Scissor" and userChoise=="Paper":  
            print("Computer selected ",computerChoise," Computer is win for this turm.")
            computerPoints = computerPoints+10
        elif computerChoise=="Scissor" and userChoise=="Scissor":
            print("Computer selected ",computerChoise," Both are win for this turm")
            userPoints = userPoints+5
            computerPoints = computerPoints+5
        else:
            print("You have entered wrong spelling of invailid word!, please check and reenter.")
            bestOfFive = bestOfFive-1
        bestOfFive = bestOfFive+1
    bothPoints = [userPoints,computerPoints]
    return bothPoints
    
def decision(userPoints,computerPoints):
    print()
    print("=================================================")
    print()
    print("\t Score ")
    print("User Points are ",userPoints)
    print("Computer Points are ",computerPoints)
    if computerPoints>userPoints:
        print("You loss the match!")
    elif userPoints>computerPoints:
        print("Congratulations, you won the match!")
    else:
        print("The match is drawn!")

#calling the functions
bothPoints = gameLogics(userPoints,computerPoints,bestOfFive)
decision(bothPoints[0],bothPoints[1])