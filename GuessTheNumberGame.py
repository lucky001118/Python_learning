import random
''' 
        # ABOUT THE GAME #
    ->Computer will genrate the any number from 1 to 100 
    ->you have to guess what is that number
    ->Computer will give you the hints like
        -->it can say number is greater then the actual number in the case of you ented lesser number, so next turm you have to enterd lesser no.
        -->it can say number is less then the actual number in the case of you enterd grater number, so next time you have to enter bigger no.

        # ABOUT THE POINT DISTRIBUTION #
    ->If you guess the number in the very first time you get 100(full) points.
    ->If you guess at the 2nd time then you got 90 points 
    ->Hance every wrong guess you loss the 10 points 
'''
def userEnter():
    userGuess = int(input("Guess the number: "))
    return userGuess
def userInfo():
    print()
    print("*************************************************************")
    print("\t Your Information")
    userName = input("Enter your name: ")
    userName = userName.capitalize()     #--->capital first latter
    gameId = input("Enter the game id: ")
    userInfoList = [userName,gameId]
    return userInfoList
def computerGenrateRandom():
    computerGenratedNumber = random.randint(1,100)
    #print(computerGenratedNumber)
    return computerGenratedNumber
def theWinnerOfGame(userInformation,yourPoint):
    userInformation = userInformation
    userName = userInformation[0]
    userGameId = userInformation[1]
    userGamePoint = yourPoint
    print("      ========================================")
    print("\n \t\t Results ")
    print(" \t\t---------")
    print("Name: ",userName," \t GameId: ",userGameId," \t Score: ",userGamePoint)
    print("Yoy have been won the match.")
    print()
    print("      =========================================\n")
    print("*************************************************************")
def TheGame():
    computerGenratedNumber = computerGenrateRandom()
    userGuess = -1
    yourPoint = 100
    while computerGenratedNumber!=userGuess:
        userGuess = userEnter()
        if userGuess<0:
            print("You have intered the negative number,numer is between the 1 to 100.")
        elif computerGenratedNumber>userGuess and userGuess>0 and userGuess<101:
            print("The number is grater then your guessed number.")
        elif computerGenratedNumber<userGuess and userGuess>0 and userGuess<101:
            print("The number is less then the your enterd number.")
        elif userGuess>100:
            print("You entered the bigger number then 100,you have to guess only between 1 to 100.")
        yourPoint=yourPoint-10
    return yourPoint

    #function calling
userInformation = userInfo()
#print(userInformation)
yourPoint=TheGame()
theWinnerOfGame(userInformation,yourPoint)
