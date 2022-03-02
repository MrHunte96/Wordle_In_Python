import pygame

# Avaliable states for a box
class CharState:
    INACTIVE = 0
    PENDING = 1
    INCORRECT = 2
    WRONG_POS = 3
    RIGHT_POS = 4

# A container box that contain a single letter
class Box:
    # Initialize
    def __init__(self):
        self.myfont : pygame.font.Font = None
        self.fontCol = (255,255,255)
        self.character = ' '
        self.textSurface : pygame.Surface = None
        self.position = (0,0)
        self.offsetSize = (20,8)
        self.boxSize = (10,10)
        self.bgCol = (255,255,255)
        self.state = CharState.INACTIVE
        self.prevState = CharState.INACTIVE
        self.outlineWidth = 0
    
    # Config initial state
    def Config(self, font : pygame.font.Font, fontcol = (255,255,255), pos = (0,0), size = (50, 50), state : CharState = CharState.INACTIVE):
        self.SetFont(font)
        self.SetFontColor(fontcol)
        self.SetPos(pos)
        self.SetSize(size)
        self.SetState(state)

    # Set font
    def SetFont(self, font : pygame.font.Font):
        self.myfont = font
        self.SetChar('')
    
    # Set text color
    def SetFontColor(self, col):
        self.fontCol = col

    # Set size of box
    def SetSize(self, size):
        self.boxSize = size
        self.offsetSize = (size[0] / 2 - self.myfont.get_height() / 4, size[1] / 2 - self.myfont.get_height() / 2.5)

    # Set the state of the box
    def SetState(self, state : CharState):
        self.prevState = self.state
        self.state = state
        if self.state == CharState.INACTIVE:
            self.bgCol = (100,100,100) # Dark Gray
            self.outlineWidth = 1
        elif self.state == CharState.PENDING:
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

    # Revert to previous state
    def RevertState(self):
        self.SetState(self.prevState)

    # Set the letter in the box
    def SetChar(self, char):
        self.character = char
        self.textSurface = self.myfont.render(self.character, False, self.fontCol)

    # Set position of box
    def SetPos(self, pos):
        self.position = pos

    # Reset the box letter and state
    def Reset(self):
        self.SetChar(' ')
        self.SetState(CharState.INACTIVE)

    # Draw the box and it's letter
    def Draw(self, surface):
        pygame.draw.rect(surface, self.bgCol, pygame.Rect(self.position[0], self.position[1], self.boxSize[0], self.boxSize[1]), self.outlineWidth)
        surface.blit(self.textSurface,(self.position[0] + self.offsetSize[0], self.position[1] + self.offsetSize[1]))
