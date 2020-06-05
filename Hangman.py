'''
Description:
        You must create a Hangman game that allows the user to play and guess a secret word.  
        See the assignment description for details.
    
@author: William Chen-Fung    wbc2110
'''

#I did not make nearly as much progress tonight as I thought I would. There are a couple places where I am just stuck but I want to try and figure it out before I just ask you to get me out of the hole. I know you wanted to see where I was at the end of the night. Let me know if you see any glaring issues or if there is something obvious that I am missing. I really appreciate you looking at this for me. 

#Testing to see how Git works.


import random

def handleUserInputDifficulty():
    '''
    This function asks the user if they would like to play the game in (h)ard or (e)asy mode, then returns the 
    corresponding number of misses allowed for the game. 
    '''
    length = random.randrange(5, 10, 1)
    file = open('lowerwords.txt', 'r')
    words = file.readlines()
    print("How many misses do you want? Hard has 8 and Easy has 12.")
    value = input("(h)ard or (e)asy> ")
    try:
        if value is "e":
            print("Easy mode selected. You have 12 misses this game.")
            missesLeft = 12
        if value is "h":
            print("Hard mode selected. You have 8 misses this game.")
            missesLeft = 8
        else:
            raise ValueError
    except ValueError:
        print("Invalid entry... Please enter h for hard or e for easy")
        handleUserInputDifficulty()
    '''
    I am trying to do some recursion on line 32 but I haven't thought about 
    how I exactly want to implement everything.
    '''
    pass

def getWord(words, length):
    '''
    Selects the secret word that the user must guess. 
    This is done by randomly selecting a word from words that is of length length.
    '''
    
    wordsOfCorrectLength = []
    for i in words:
        if len(i) == length:
            wordsOfCorrectLength = wordsOfCorrectLength.append(i)
    secretWord = random.choice(wordsOfCorrectLength)
    return secretWord
    pass 




def createDisplayString(lettersGuessed, missesLeft, hangmanWord):
    '''
    Creates the string that will be displayed to the user, using the information in the parameters.
    '''
    
    x = ''.join(sorted(lettersGuessed)) #This is supposed to order the letters in alphabetical order
    x = x.replace("", " ")[1:-1]
    y = ""
    y = y.join(hangmanWord)
    y = y.replace("", " ")[1:-1]
    n1 = '\n'
    displayString = (
        f"letters you've guessed: {x}{n1}"
        f"misses remaining = {missesLeft}{n1}"
        f"{y}"
    )
    return displayString
    pass


def handleUserInputLetterGuess(lettersGuessed, displayString):
    '''
    Prints displayString, then asks the user to input a letter to guess.
    This function handles the user input of the new letter guessed and checks if it is a repeated letter.
    '''
    #I still need to figure out how to layout the hangmanWord and incorporate the correct letters that have already been guessed.  
    
    #Your Code Here
    pass 




def updateHangmanWord(guessedLetter, secretWord, hangmanWord):
    '''
    Updates hangmanWord according to whether guessedLetter is in secretWord and where in secretWord guessedLetter is in.
    '''

    hangmanWord = list("_" * len(secretWord))  # I need to make this so it doesnt reset every time. I might
    #add this as a line to the actual game function
    count = 0
    for i in secretWord:
        for j in lettersGuessed:
            if i is j:
                hangmanWord[count] = j
        count += 1
    pass 

#this just updates hangmanWord and I havent really gotten a chance to think about how to implement it.


def processUserGuess(guessedLetter, secretWord, hangmanWord, missesLeft):
    '''
    Uses the information in the parameters to update the user's progress in the hangman game.
    '''
    
    #Your Code Here
    pass 


#This function seems similar to the createDisplayString function except this would be run between turns in one game. I have not really given this function much thought yet. 

def runGame(filename):
    '''
    This function sets up the game, runs each round, and prints a final message on whether or not the user won.
    True is returned if the user won the game. If the user lost the game, False is returned.
    '''
    
    #Your Code Here
    pass 



if __name__ == "__main__":
    '''
    Running Hangman.py should start the game, which is done by calling runGame, therefore, we have provided you this code below.
    '''
    runGame('lowerwords.txt')
