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

    def shatter(self, ball):
        right = Ball(ball.colour, ball.x + 1, ball.y + 1)
        self.moveBallLeft()
        return right

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
        self.paintedPins = []

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
         self.ballsToSimulate = []

    def parseSequenceOfBalls(self):
        for colour in self.sequenceOfBalls:
            ball = Ball(colour, 0, 0)
            self.ballsToSimulate.append(ball)

    def rollRandomNumber(self):
        randomNumber = random.randint(0,100)
        return randomNumber

    def paintPinAtCurrentCoordinates(self, ball):
        print("Pin grid:")
        for row in self.grid.grid:
            for pin in row:
                if ball.x == pin.x and ball.y == pin.y:
                    pin.colour = ball.colour

    def randomlyChooseBallBehaviour(self, ball):
        randomNumber = self.rollRandomNumber()
        if randomNumber < 40:
            ball.moveBallLeft()
        elif 40 < randomNumber < 80:
            ball.moveBallRight()
        else:
            self.paintPinAtCurrentCoordinates(ball)
            right = ball.shatter(ball)
            self.ballsToSimulate.append(right)

    def traverseBallOverGrid(self):
        for ball in self.ballsToSimulate:
                self.ballsToSimulate.pop(0)
                while True:
                    print(ball.x, ball.y)
                    if ball.y > self.gridSize: 
                        break
                    self.randomlyChooseBallBehaviour(ball)

    def playGame(self):
        self.parseSequenceOfBalls()
        while len(self.ballsToSimulate) > 0:
            self.traverseBallOverGrid()
        print("Grid:")
        for y in self.grid.grid:
            for i in y:
                print(i.colour,i.x,i.y)
        print("Painted pins:")
        for i in self.grid.paintedPins:
            print(i.colour,i.x,i.y)
        return self.grid.paintedPins

gamePlayer = GamePlayer(4, "RGBR")
gamePlayer.playGame()


    

