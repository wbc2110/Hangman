'''
Description:
        You must create a Hangman game that allows the user to play and guess a secret word.  
        See the assignment description for details.
    
@author: William Chen-Fung    wbc2110
'''

import random

def handleUserInputDifficulty():
    '''
    This function asks the user if they would like to play the game in (h)ard or (e)asy mode, then returns the 
    corresponding number of misses allowed for the game. 
    '''
    print("How many misses do you want? Hard has 8 and Easy has 12.")
    value = input("(h)ard or (e)asy> ")
    acceptableValues = ['e', 'h']
    while value not in acceptableValues:
        print("Invalid entry. Please enter h for hard or e for easy")
        value = input("(h)ard or (e)asy> ")
    if value is "e":
        print("Easy mode selected. You have 12 misses this game.")
        missesLeft = 12
    if value is "h":
        print("Hard mode selected. You have 8 misses this game.")
        missesLeft = 8

    return missesLeft

def getWord(words, length):
    '''
    Selects the secret word that the user must guess. 
    This is done by randomly selecting a word from words that is of length length.
    '''
    
    wordsOfCorrectLength = []
    for i in words:
        if len(i) == length:
            wordsOfCorrectLength.append(i)
    return random.choice(wordsOfCorrectLength)

def createDisplayString(lettersGuessed, missesLeft, hangmanWord):
    '''
    Creates the string that will be displayed to the user, using the information in the parameters.
    '''
    x = ' '.join(sorted(lettersGuessed))
    y = ' '.join(hangmanWord)
    return (
        f"letters you've guessed: {x}\n"
        f"misses remaining = {missesLeft}\n"
        f"{y}"
    )

def handleUserInputLetterGuess(lettersGuessed, displayString):
    '''
    Prints displayString, then asks the user to input a letter to guess.
    This function handles the user input of the new letter guessed and checks if it is a repeated letter.
    '''
    print(displayString)
    guessedLetter = input("letter> ")
    guessedLetter = guessedLetter.lower()
    while guessedLetter in lettersGuessed:
        print("You already guessed that. Please chose a different letter.")
        guessedLetter = input("letter> ")
    while len(guessedLetter) != 1:
        print("Please input only 1 letter")
        guessedLetter = input("letter> ")
    while not guessedLetter.isalpha():
        print("Please chose a letter.")
        guessedLetter = input("letter> ")
    return guessedLetter

def updateHangmanWord(guessedLetter, secretWord, hangmanWord = ""):
    '''
    Updates hangmanWord according to whether guessedLetter is in secretWord and where in secretWord guessedLetter is in.
    '''
    for i in range(len(secretWord)):
        if guessedLetter is secretWord[i]:
            hangmanWord[i] = guessedLetter
    return hangmanWord

def processUserGuess(guessedLetter, secretWord, hangmanWord, missesLeft):
    '''
    Uses the information in the parameters to update the user's progress in the hangman game.
    '''

    isInSecretWord = False
    if guessedLetter in secretWord:
        isInSecretWord = True
    else:
        missesLeft -= 1
    return [updateHangmanWord(guessedLetter, secretWord, hangmanWord), missesLeft, isInSecretWord]

def runGame(filename):
    '''
    This function sets up the game, runs each round, and prints a final message on whether or not the user won.
    True is returned if the user won the game. If the user lost the game, False is returned.
    '''

    continuePlaying = True
    gamesPlayed = 1
    numberOfGamesWon = 0
    while continuePlaying:
        length = random.randint(6, 11)
        file = open(filename, 'r')
        words = file.readlines()
        missesLeft = handleUserInputDifficulty()
        beginningMisses = missesLeft
        lettersGuessed = []
        secretWord = getWord(words, length)
        gameWon = False
        numberOfRounds = 0
        hangmanWord = list("_" * (len(secretWord)-1))
        while missesLeft > 0 and not gameWon:
            displayString = createDisplayString(lettersGuessed, missesLeft, hangmanWord)
            guessedLetter = handleUserInputLetterGuess(lettersGuessed, displayString)
            lettersGuessed.append(guessedLetter)
            [hangmanWord, missesLeft, inWord] = processUserGuess(guessedLetter, secretWord, hangmanWord, missesLeft)
            if not inWord:
                print(f"You missed: {guessedLetter} not in word")
            if '_' not in hangmanWord:
                gameWon = True
            numberOfRounds += 1
        if gameWon:
            print(f"You correctly guessed the word: {secretWord}")
            numberOfGamesWon += 1
        elif missesLeft <= 0:
            print(
                f"You're hung!!\n"
                f"The word is {secretWord}")
        print(f"You made {numberOfRounds} guesses with {beginningMisses - missesLeft} misses.")
        x = input("Do you want to play again? y or n> ")
        while x not in ["y", "n"]:
            x = input("Invalid input. Please enter y to keep playing or n if you would like to stop> ")
        if x is "n":
            continuePlaying = False
        if x is "y":
            gamesPlayed += 1

    print(f"You won {numberOfGamesWon} game(s) and lost {gamesPlayed - numberOfGamesWon}.")

if __name__ == "__main__":
    '''
    Running Hangman.py should start the game, which is done by calling runGame, therefore, we have provided you this code below.
    '''
    runGame('lowerwords.txt')
