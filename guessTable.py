from typing import List
from row import Row
from box import Box, CharState

# Grid that display the user guesses
class GuessTable:
    # Static variables
    NUM_OF_LETTERS = 5
    MAX_GUESS_TRIES = 6

    # Initialize the grid
    def __init__(self, font, boxSize, numofletters, maxguesstries):
        GuessTable.NUM_OF_LETTERS = numofletters
        GuessTable.MAX_GUESS_TRIES = maxguesstries
        self.guessStr = ''
        self.guessNum = 0
        self.guessTable : List[Row] = []
        for _ in range(maxguesstries):
            self.guessTable.append(Row(boxSize, numofletters, font))
        self.guessTable[self.guessNum].SetState(CharState.PENDING)

    # Set position of grid (top-left)
    def SetPos(self, pos):
        for row in self.guessTable:
            row.SetPos(pos)
            pos = (pos[0], pos[1] + row.boxList[0].boxSize[1] + 5)
    
    # Draw all the rows of boxes
    def Draw(self, surface):
        for row in self.guessTable:
            row.Draw(surface)

    # Check if the current guessing row is filled
    def CheckIfFilled(self) -> bool:
        return len(self.guessStr) == GuessTable.NUM_OF_LETTERS

    # Check if the current guessing row contains the correct word
    def CheckGuess(self, answer : str) -> bool:
        # Set up a list to count the number of letter occurance
        letterCount = [0] * 26
        for c in answer:
            letterCount[ord('Z') - ord(c)] += 1

        correctCount = 0
        i = 0
        # Loop all the character in the guessing row
        for c in self.guessTable[self.guessNum].boxList:
            # If the letter matches the answer
            if c.character == answer[i]:
                c.SetState(CharState.RIGHT_POS)
                letterCount[ord('Z') - ord(c.character)] -= 1
                correctCount += 1
            else:
                c.SetState(CharState.INCORRECT)
                # Check if the answer still contains the guessed letter
                if letterCount[ord('Z') - ord(c.character)] > 0:
                    c.SetState(CharState.WRONG_POS)
                    letterCount[ord('Z') - ord(c.character)] -= 1
            i += 1
        return correctCount == GuessTable.NUM_OF_LETTERS
    
    # Get the string of the row
    def GetWord(self) -> str:
        return self.guessStr

    # Get the row (list of boxes)
    def GetRow(self) -> Row:
        return self.guessTable[self.guessNum]

    # Add a letter to the current guess
    def InsertLetter(self, letter : str):
        if len(self.guessStr) < GuessTable.NUM_OF_LETTERS:
            self.guessTable[self.guessNum].boxList[len(self.guessStr)].SetChar(letter)
            self.guessStr += letter

    # Remove a letter to the current guess
    def RemoveLetter(self):
        if len(self.guessStr) > 0:
            self.guessStr = self.guessStr[0:len(self.guessStr)-1]
            self.guessTable[self.guessNum].boxList[len(self.guessStr)].SetChar(' ')

    # Increment current guess index and update UI
    def NextGuess(self):
        self.guessNum += 1
        self.guessStr = ''
        if self.guessNum < self.MAX_GUESS_TRIES:
            self.guessTable[self.guessNum].SetState(CharState.PENDING)
            return True
        else:
            return False

    # Clear all the letters and status of all the rows
    def Clear(self):
        self.guessStr = ''
        self.guessNum = 0
        for r in self.guessTable:
            r.Reset()
        self.guessTable[self.guessNum].SetState(CharState.PENDING)
        
