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

    def checkIfBallAtEnd(self, ySize):
        if self.y == ySize:
            return True

    def rollRandomNumber(self):
        randomNumber = random.randint(0,100)
        return randomNumber

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
        self.paintedPins = []
        self.newBallStartingPins = [Pin(0,0)]

class GamePlayer:

    def __init__(self,gridSize, sequenceOfBalls):
         self.gridSize = gridSize
         self.sequenceOfBalls = sequenceOfBalls
         self.grid = PinGrid(gridSize)
         self.newBallStartingPins = self.grid.newBallStartingPins
         self.listOfStartingPins = []

    def rollRandomNumber(self):
        randomNumber = random.randint(0,100)
        return randomNumber

    def simulateBallTravel(self):
        ball = Ball("red", 0, 0)
        for i in range(self.gridSize):
            randomNumber = self.rollRandomNumber()
            if randomNumber < 40:
                ball.moveBallLeft()
            elif 40 < randomNumber < 80:
                ball.moveBallRight()
            else:
                ball.moveBallLeft()
                right = Ball(ball.colour, ball.x + 1, ball.y + 1)
                self.listOfStartingPins.append(right)
            print(ball.x,",",ball.y)
        print("-------")
        for i in self.listOfStartingPins:
            print(i.x,i.y)
    # def parseSequenceOfBalls(self):
    #     ballInstance = Ball()
    #     for b in self.sequenceOfBalls:
    #         simulateBallTravel(ballInstance)


gamePlayer = GamePlayer(20, "RGB")
gamePlayer.simulateBallTravel()
# print(gamePlayer.grid.grid)

    

