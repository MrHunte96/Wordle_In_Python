from box import Box, CharState
from typing import List

# A Row in the guessing table
# A row consist of multiple boxes
class Row:
    def __init__(self, size : tuple, count, font, fontcol = (255,255,255)):
        self.offsetX = size[0] + 5
        self.boxList : List[Box] = []
        # Initialize all boxs
        for _ in range(count):
            b = Box()
            b.Config(font, fontcol, (0,0), size, CharState.INACTIVE)
            self.boxList.append(b)

    # Set state of all boxes
    def SetState(self, state : CharState):
        for b in self.boxList:
            b.SetState(state)

    # Set boxes character with a string
    def SetText(self, text : str):
        i = 0
        for b in self.boxList:
            if i < len(text):
                b.SetChar(text[i])
            else:
                b.SetChar(' ')
            i += 1

    # Set position of row
    def SetPos(self, pos):
        for b in self.boxList:
            b.SetPos(pos)
            pos = (pos[0] + self.offsetX, pos[1])

    # Reset all box status
    def Reset(self):
        for b in self.boxList:
            b.Reset()

    # Draw all boxes
    def Draw(self, surface):
        for b in self.boxList:
            b.Draw(surface)