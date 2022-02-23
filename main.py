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
    pygame.display.set_caption('Wordle')

    # Setup Font
    guessFont = pygame.font.SysFont('Consolas', 40)
    keyboardFont = pygame.font.SysFont('Consolas', 20)
    
    # Initialize Game
    myGuessTable = GuessTable(guessFont, (60,60), 5, 5)
    myGuessTable.SetPos((100,80))
    myKeyboardTable = KeyboardTable(keyboardFont, (40, 40))
    myKeyboardTable.SetPos((30,550))

    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    myGuessTable.RemoveLetter()
                elif event.key == pygame.K_RETURN:
                    myGuessTable.CheckGuess("ASDFG".upper())
                elif event.key >= pygame.K_a and event.key <= pygame.K_z:
                    myGuessTable.InsertLetter(pygame.key.name(event.key).upper())
            
        surface.fill((0,0,0))
        myGuessTable.Draw(surface)
        myKeyboardTable.Draw(surface)

        # Update screen
        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    gameLoop()