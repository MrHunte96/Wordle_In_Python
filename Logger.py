import pygame

class Logger:
    def __init__(self):
        self.font = None
        self.texture = None
        self.pos = (0,0)
    
    def config(self, font, pos):
        self.font = font
        self.pos = pos

    def log(self, text : str, col : tuple):
        self.texture = self.font.render(text, False, col)
    
    def clear(self):
        self.texture = None

    def Draw(self, surface):
        if self.texture != None:
            surface.blit(self.texture, self.pos)
