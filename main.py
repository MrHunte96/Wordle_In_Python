from random import Random, random
import pygame
from guessTable import GuessTable
from keyboardTable import KeyboardTable
from typing import List

def gameLoop():
    # Init Pygame
    pygame.init()
    pygame.font.init() 

    # Setup window
    surface = pygame.display.set_mode((512,768))
    pygame.display.set_caption('myWordle')

    # Setup Font
    guessFont = pygame.font.SysFont('Consolas', 40)
    keyboardFont = pygame.font.SysFont('Consolas', 20)
    
    # Initialize Game
    myGuessTable = GuessTable(guessFont, (60,60), 5, 6)
    myGuessTable.SetPos((100,80))
    myKeyboardTable = KeyboardTable(keyboardFont, (40, 40))
    myKeyboardTable.SetPos((30,550))

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
                elif event.key == pygame.K_RETURN:
                    if myGuessTable.GetWord() in wordlist:
                        checkedRow = myGuessTable.CheckGuess(answer)
                        if checkedRow != None:
                            myKeyboardTable.UpdateCheckedRow(checkedRow)
                        else:
                            myKeyboardTable.Reset()
                            answer = FindRandomWord(wordlist)
                elif event.key >= pygame.K_a and event.key <= pygame.K_z:
                    myGuessTable.InsertLetter(pygame.key.name(event.key).upper())
                    myKeyboardTable.KeyDown(pygame.key.name(event.key).upper())
            elif event.type == pygame.KEYUP:
                if event.key >= pygame.K_a and event.key <= pygame.K_z:
                    myKeyboardTable.KeyUp(pygame.key.name(event.key).upper())
            
        surface.fill((0,0,0))
        myGuessTable.Draw(surface)
        myKeyboardTable.Draw(surface)

        # Update screen
        pygame.display.update()

    pygame.quit()

def FindRandomWord(wordlist : List[str]):
    r = Random()
    ans = wordlist[r.randint(0, len(wordlist)-1)]
    print ( "Answer : [", ans, "]")
    return ans

if __name__ == '__main__':
    gameLoop()