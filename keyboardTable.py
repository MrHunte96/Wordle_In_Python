from tkinter import font
from row import Row

class KeyboardTable:
    def __init__(self, font, keySize : tuple) -> None:
        self.keySize = keySize
        self.row1 : Row = Row(self.keySize, 10, font)
        self.row1.SetText("QWERTYUIOP")
        self.row2 : Row = Row(self.keySize, 9, font)
        self.row2.SetText("ASDFGHJKL")
        self.row3 : Row = Row(self.keySize, 7, font)
        self.row3.SetText("ZXCVBNM")

    def SetPos(self, pos):
        self.row1.SetPos((pos[0], pos[1]))
        self.row2.SetPos((pos[0] + self.keySize[0] * 0.5, pos[1] + self.keySize[0] + 5))
        self.row3.SetPos((pos[0] + self.keySize[0] * 1.7, pos[1] + (self.keySize[0] + 5) * 2))

    def KeyDown(self, key):
        pass

    def KeyUp(self, key):
        pass
    
    def Draw(self, surface):
        self.row1.Draw(surface)
        self.row2.Draw(surface)
        self.row3.Draw(surface)