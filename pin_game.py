"""
ask user for size of pin grid based number of pins on one edge of equilateral triangle
input: string containing only rgb letters denoting coloured balls

grid is a list of lists. 
user input = n 
length of lists = 1+1...n
number of lists = n

e.g. ball is at level 2, pin 1
when it goes to the next level, you carry across its placement as either 
the number of the previous pin 'p' or p+1

store the current pin number as a variable

game runner
- input grid
- input balls and colours
    ball
    - colour
    - method: shatter
    - x 
    - y 

    pin grid 
        pin 
        - colour
        - x
        - y
"""

import random

class Pin:
    def __init__(self, x, y):
        self.colour = "white"
        self.x = x
        self.y = y

class Ball:

    def __init__(self, colour, x, y):
        self.colour = colour
        self.x = x
        self.y = y 

    def moveBallLeft(self):
        self.y += 1

    def moveBallRight(self):
        self.x += 1
        self.y += 1

    def shatter(self):
        left = Ball(self.colour, self.x, self.y + 1)
        right = Ball(self.colour, self.x + 1, self.y + 1)
        return left, right

    def checkIfBallAtEndOfGrid(self, ySize):
        if self.y == ySize:
            return True

    def randomlyChooseBallAction(self):
        randomNumber = random.randint(0,1)
        if randomNumber < 0.2:
            self.shatter()
        elif 0.6 < randomNumber < 0.8:
            self.moveBallLeft()
        else:
            self.moveBallRight()

class PinGrid:
    def __init__(self,gridSize):
        self.gridSize = gridSize
        self.grid = []
        for y in range(gridSize):
            pinList = []
            width = y + 1
            for x in range(width):
                pin = Pin(x, y)
                pinList.append(pin)
            self.grid.append(pinList)

class GamePlayer:
    def __init__(self,gridSize, sequenceOfBalls):
         self.gridSize = gridSize
         self.sequenceOfBalls = sequenceOfBalls
         self.grid = PinGrid(gridSize)
            

    def simulateBallTravel(self):
        ball.randomlyChoose

    def parseSequenceOfBalls(self):
        ball = Ball()
        for ball in self.sequenceOfBalls:
            simulateBallTravel(ball)


gamePlayer = GamePlayer(5, "RBG")
# print(gamePlayer.grid.grid)

    

