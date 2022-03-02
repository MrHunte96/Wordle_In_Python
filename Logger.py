import pygame

# Simple text drawer
class Logger:
    def __init__(self):
        self.font :pygame.font.Font = None
        self.texture = None
        self.pos = (0,0)
    
    # Initialize the font and position
    def config(self, font : pygame.font.Font, pos : tuple):
        self.font = font
        self.pos = pos

    # Set the text to draw
    def log(self, text : str, col : tuple):
        self.texture = self.font.render(text, False, col)
    
    # Clear the text
    def clear(self):
        self.texture = None

    # Draw the text on screen
    def Draw(self, surface : pygame.Surface):
        if self.texture != None:
            surface.blit(self.texture, self.pos)
