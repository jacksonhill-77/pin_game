from pin_game import PinGrid
from pin_game import GamePlayer

def checkListItemsAreUnique(x):
    if len(set(x)) == len(x):
        return True

def testPinsAreUnique():
    grid = PinGrid(20) 
    gridPins = []
    for row in grid.grid:
        for pin in row:
            coordinates = (pin.x,pin.y)
            gridPins.append(coordinates)
    assert checkListItemsAreUnique(gridPins) == True

def testFinalPinCoordinates():
    grid = PinGrid(20) 
    gridPins = []
    for row in grid.grid:
        for pin in row:
            coordinates = (pin.x,pin.y)
            gridPins.append(coordinates)
    assert gridPins[len(gridPins)-1] == (19,19)

def testPinsOnlyWhiteOrRGB():
    game = GamePlayer(20, "RGBBGR")
    grid = game.grid.grid
    pinColours = []
    result = True
    for row in grid:
        for pin in row:
            colour = (pin.colour)
            if colour not in ('white','r','g','b'):
                result = False
                break
    assert result == True 






