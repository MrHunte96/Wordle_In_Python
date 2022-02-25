from typing import List
from row import Row
from box import Box, CharState

class GuessTable:
    NUM_OF_LETTERS = 5
    MAX_GUESS_TRIES = 5
    def __init__(self, font, boxSize, numofletters, maxguesstries):
        GuessTable.NUM_OF_LETTERS = numofletters
        GuessTable.MAX_GUESS_TRIES = maxguesstries
        self.ended = False
        self.guessStr = ''
        self.guessNum = 0
        self.guessTable : List[Row] = []
        for _ in range(maxguesstries):
            self.guessTable.append(Row(boxSize, numofletters, font))
        self.guessTable[self.guessNum].SetState(CharState.PENDING)

    def SetPos(self, pos):
        for row in self.guessTable:
            row.SetPos(pos)
            pos = (pos[0], pos[1] + row.boxList[0].boxSize[1] + 5)
    
    def Draw(self, surface):
        for row in self.guessTable:
            row.Draw(surface)

    def CheckGuess(self, answer : str) -> Row:
        if self.ended:
            self.__Clear()
            return

        letterCount = [0] * 26
        for c in answer:
            letterCount[ord('Z') - ord(c)] += 1

        correctCount = 0
        # Check if all letters are filled
        if len(self.guessStr) == GuessTable.NUM_OF_LETTERS:
            i = 0
            for c in self.guessTable[self.guessNum].boxList:
                if c.character == answer[i]:
                    c.SetState(CharState.RIGHT_POS)
                    letterCount[ord('Z') - ord(c.character)] -= 1
                    correctCount += 1
                else:
                    c.SetState(CharState.INCORRECT)
                    if letterCount[ord('Z') - ord(c.character)] > 0:
                        for a in answer:
                            if c.character == a:
                                c.SetState(CharState.WRONG_POS)
                                letterCount[ord('Z') - ord(a)] -= 1
                                break
                i += 1
            # Reset guess
            self.guessNum += 1
            self.guessStr = ''
        # All Correct
        if correctCount == GuessTable.NUM_OF_LETTERS or self.guessNum >= GuessTable.MAX_GUESS_TRIES:
            self.ended = True
        else:
            self.guessTable[self.guessNum].SetState(CharState.PENDING)
        return self.guessTable[self.guessNum - 1]
        

    def InsertLetter(self, letter : str):
        if len(self.guessStr) < GuessTable.NUM_OF_LETTERS:
            self.guessTable[self.guessNum].boxList[len(self.guessStr)].SetChar(letter)
            self.guessStr += letter

    def RemoveLetter(self):
        if len(self.guessStr) > 0:
            self.guessStr = self.guessStr[0:len(self.guessStr)-1]
            self.guessTable[self.guessNum].boxList[len(self.guessStr)].SetChar(' ')

    def __Clear(self):
        self.ended = False
        self.guessStr = ''
        self.guessNum = 0
        for r in self.guessTable:
            r.Reset()
        self.guessTable[self.guessNum].SetState(CharState.PENDING)
        
