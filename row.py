from box import Box, CharState
from typing import List

class Row:
    def __init__(self, size, count):
        self.offsetX = size[0] + 5
        self.boxList : List[Box] = []
        # Initialize all boxs
        for _ in range(count):
            b = Box()
            b.Config((0,0), size, CharState.PENDING)
            self.boxList.append(b)

    def SetPos(self, pos):
        for b in self.boxList:
            b.SetPos(pos)
            pos = (pos[0] + self.offsetX, pos[1])

    def Draw(self, surface):
        for b in self.boxList:
            b.Draw(surface)