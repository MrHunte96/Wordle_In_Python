from random import Random, random
import pygame
from guessTable import GuessTable
from keyboardTable import KeyboardTable
from Logger import Logger
from typing import List

def gameLoop():
    # Init Pygame
    pygame.init()
    pygame.font.init() 

    # Setup window
    surface = pygame.display.set_mode((512,768))
    pygame.display.set_caption('myWordle')
    logoTex = pygame.image.load("Logo1.png", "Logo")

    # Setup Font
    guessFont = pygame.font.SysFont('Consolas', 40)
    keyboardFont = pygame.font.SysFont('Consolas', 20)
    logFont = pygame.font.SysFont('Consolas', 20)
    
    # Initialize Game
    myGuessTable = GuessTable(guessFont, (60,60), 5, 6)
    myGuessTable.SetPos((90,80))
    myKeyboardTable = KeyboardTable(keyboardFont, (40, 40))
    myKeyboardTable.SetPos((30,550))
    myLogger = Logger()
    myLogger.config(logFont, (150, 500))
    gameEnded = False

    # Initialize word list
    wordlist : List[str] = []
    with open("sgb-words.txt", 'r') as f:
        wordlist = f.readlines()
    for i in range(len(wordlist)):
        wordlist[i] = wordlist[i][0:GuessTable.NUM_OF_LETTERS].upper()
    
    # Choose a word
    answer = FindRandomWord(wordlist)

    run = True
    while run:
        # Get Events
        for event in pygame.event.get():
            # Handle "X" button
            if event.type == pygame.QUIT:
                run = False
            
            # Handle Key Down Event
            elif event.type == pygame.KEYDOWN:
                # Check if key is backspace
                if event.key == pygame.K_BACKSPACE:
                    # Remove letter from table
                    myGuessTable.RemoveLetter()
                    myLogger.clear()
                # Check if key is return
                elif event.key == pygame.K_RETURN:
                    myLogger.clear()
                    # Check if game already ended
                    if gameEnded:
                        gameEnded = False
                        myGuessTable.Clear()
                        myKeyboardTable.Reset()
                        answer = FindRandomWord(wordlist)
                    # If not, check if table is filled fully to check answer
                    elif myGuessTable.CheckIfFilled():
                        # Check if word entered is a valid word from the list
                        if myGuessTable.GetWord() in wordlist:
                            # Check if the word entered is correct
                            if myGuessTable.CheckGuess(answer):
                                # Correct Answer
                                myKeyboardTable.UpdateCheckedRow(myGuessTable.GetRow())
                                myLogger.log("Correct!", (0,200,0))
                                gameEnded = True
                            else:
                                #Wrong Answer
                                myKeyboardTable.UpdateCheckedRow(myGuessTable.GetRow())
                                if not myGuessTable.NextGuess():
                                    gameEnded = True
                                    myLogger.log("Failed to guess the word!", (200,0,0))
                        else:
                            myLogger.log("Word not in list!", (200,200,200))
                
                # Check if key up is from a to z
                elif event.key >= pygame.K_a and event.key <= pygame.K_z:
                    # Add key press letter to table
                    myGuessTable.InsertLetter(pygame.key.name(event.key).upper())
                    # Inform keyboard UI
                    myKeyboardTable.KeyDown(pygame.key.name(event.key).upper())

            # Handle Key Up Event
            elif event.type == pygame.KEYUP:
                # Check if key up is from a to z
                if event.key >= pygame.K_a and event.key <= pygame.K_z:
                    # Inform keyboard UI
                    myKeyboardTable.KeyUp(pygame.key.name(event.key).upper())
        
        # "Clear" screen
        surface.fill((0,0,0))
        # Drawing to screen
        DrawLogo(surface, logoTex)
        myGuessTable.Draw(surface)
        myKeyboardTable.Draw(surface)
        myLogger.Draw(surface)

        # Update screen
        pygame.display.update()

    # Quit Pygame
    pygame.quit()

# Returns a random word from the list of words
def FindRandomWord(wordlist : List[str]):
    r = Random()
    ans = wordlist[r.randint(0, len(wordlist)-1)]
    print ( "Answer : [", ans, "]")
    return ans

# Draws game Logo
def DrawLogo(surface : pygame.Surface, logo : pygame.Surface):
    surface.blit(pygame.transform.scale(logo, (200,100)), (150,-10))

# Main Function
if __name__ == '__main__':
    gameLoop()