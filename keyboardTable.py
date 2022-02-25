from tkinter import font
from box import CharState, Box
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
    
    def UpdateCheckedRow(self, row : Row):
        for box in row.boxList:
            def func(b : Box):
                if b.state != CharState.RIGHT_POS or (b.state == CharState.WRONG_POS and box.state != CharState.RIGHT_POS):
                    b.SetState(box.state)
            self.__FindKeyAndApply(box.character, func)

    def SetPos(self, pos):
        self.row1.SetPos((pos[0], pos[1]))
        self.row2.SetPos((pos[0] + self.keySize[0] * 0.5, pos[1] + self.keySize[0] + 5))
        self.row3.SetPos((pos[0] + self.keySize[0] * 1.7, pos[1] + (self.keySize[0] + 5) * 2))

    def KeyDown(self, key):
        def func(box : Box):
            box.SetState(CharState.PENDING)
        self.__FindKeyAndApply(key, func)

    def KeyUp(self, key):
        def func(box : Box):
            if box.state == CharState.PENDING:
                box.RevertState()
        self.__FindKeyAndApply(key, func)

    def __FindKeyAndApply(self, key, function):
        for box in self.row1.boxList:
            if box.character == key:
                function(box)
                return
        for box in self.row2.boxList:
            if box.character == key:
                function(box)
                return
        for box in self.row3.boxList:
            if box.character == key:
                function(box)
                return

    def Reset(self):
        for box in self.row1.boxList:
            box.SetState(CharState.INACTIVE)
        for box in self.row2.boxList:
            box.SetState(CharState.INACTIVE)
        for box in self.row3.boxList:
            box.SetState(CharState.INACTIVE)

    def Draw(self, surface):
        self.row1.Draw(surface)
        self.row2.Draw(surface)
        self.row3.Draw(surface)