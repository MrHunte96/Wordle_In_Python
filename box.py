from turtle import bgcolor
import pygame

class CharState:
    PENDING = 0
    INCORRECT = 1
    WRONG_POS = 2
    RIGHT_POS = 3

class Box:
    myfont = None
    textCol = (255, 255, 255)

    def __init__(self):
        self.character = ' '
        self.textSurface = Box.myfont.render(self.character, False, Box.textCol)
        self.position = (0,0)
        self.offsetSize = (20,8)
        self.boxSize = (10,10)
        self.bgCol = (255,255,255)
        self.state = CharState.PENDING
        self.outlineWidth = 0

    def Config(self, pos = (0,0), size = (50, 50), state : CharState = CharState.PENDING):
        self.SetPos(pos)
        self.SetSize(size)
        self.SetState(state)

    def SetSize(self, size):
        self.boxSize = size
        self.offsetSize = (size[0] / 2 - 11, size[1] / 2 - 15)

    def SetState(self, state : CharState):
        self.state = state
        if self.state == CharState.PENDING:
            self.bgCol = (200,200,200) # White
            self.outlineWidth = 2
        elif self.state == CharState.INCORRECT:
            self.bgCol = (200,200,200) # White
            self.outlineWidth = 0
        elif self.state == CharState.WRONG_POS:
            self.bgCol = (204,204,0) # Yellow
            self.outlineWidth = 0
        elif self.state == CharState.RIGHT_POS:
            self.bgCol = (32,204,32) # Green
            self.outlineWidth = 0

    def SetChar(self, char):
        self.character = char
        self.textSurface = Box.myfont.render(self.character, False, Box.textCol)

    def SetPos(self, pos):
        self.position = pos

    def Reset(self):
        self.SetChar(' ')
        self.SetState(CharState.PENDING)

    def Draw(self, surface):
        pygame.draw.rect(surface, self.bgCol, pygame.Rect(self.position[0], self.position[1], self.boxSize[0], self.boxSize[1]), self.outlineWidth)
        surface.blit(self.textSurface,(self.position[0] + self.offsetSize[0], self.position[1] + self.offsetSize[1]))