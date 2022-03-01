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

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    myGuessTable.RemoveLetter()
                    myLogger.clear()
                elif event.key == pygame.K_RETURN:
                    myLogger.clear()
                    if gameEnded:
                        gameEnded = False
                        myGuessTable.Clear()
                        myKeyboardTable.Reset()
                        answer = FindRandomWord(wordlist)
                    elif myGuessTable.CheckIfFilled():
                        if myGuessTable.GetWord() in wordlist:
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
                elif event.key >= pygame.K_a and event.key <= pygame.K_z:
                    myGuessTable.InsertLetter(pygame.key.name(event.key).upper())
                    myKeyboardTable.KeyDown(pygame.key.name(event.key).upper())
            elif event.type == pygame.KEYUP:
                if event.key >= pygame.K_a and event.key <= pygame.K_z:
                    myKeyboardTable.KeyUp(pygame.key.name(event.key).upper())
            
        surface.fill((0,0,0))
        DrawLogo(surface, logoTex)
        myGuessTable.Draw(surface)
        myKeyboardTable.Draw(surface)
        myLogger.Draw(surface)

        # Update screen
        pygame.display.update()

    pygame.quit()

def FindRandomWord(wordlist : List[str]):
    r = Random()
    ans = wordlist[r.randint(0, len(wordlist)-1)]
    print ( "Answer : [", ans, "]")
    return ans

def DrawLogo(surface : pygame.Surface, logo : pygame.Surface):
    surface.blit(pygame.transform.scale(logo, (200,100)), (150,-10))

if __name__ == '__main__':
    gameLoop()