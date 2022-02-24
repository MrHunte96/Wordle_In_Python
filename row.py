from box import Box, CharState
from typing import List

class Row:
    def __init__(self, size : tuple, count, font, fontcol = (255,255,255)):
        self.offsetX = size[0] + 5
        self.boxList : List[Box] = []
        # Initialize all boxs
        for _ in range(count):
            b = Box()
            b.Config(font, fontcol, (0,0), size, CharState.INACTIVE)
            self.boxList.append(b)

    def SetState(self, state : CharState):
        for b in self.boxList:
            b.SetState(state)

    def SetText(self, text : str):
        i = 0
        for b in self.boxList:
            if i < len(text):
                b.SetChar(text[i])
            else:
                b.SetChar(' ')
            i += 1

    def SetPos(self, pos):
        for b in self.boxList:
            b.SetPos(pos)
            pos = (pos[0] + self.offsetX, pos[1])

    def Reset(self):
        for b in self.boxList:
            b.Reset()

    def Draw(self, surface):
        for b in self.boxList:
            b.Draw(surface)